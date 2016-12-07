import numpy
import sys
import math
import os
import cv2

from Intersections import infill
from Intersections import infill_grid
from Plane import Plane
from Line import Line
from Line import equall
from Vert import Vert
from Vert import magnitude2v
from Vert import magnitude1v
from Vert import add
from Vert import sub
from Vert import mult
from Vert import div
from Vert import equalv
from Vert import dot
from Support import support
from optparse import OptionParser
from pancake import pancake

extrude = 2.0

#########################
# I/O
#########################

def processPancake(imgurl, rad, tol1, tol2, epsilon, white, imagetoggle, flip):
	img = pancake(imgurl, rad, tol1, tol2, epsilon, white, imagetoggle, flip)

	allperims = []
	
	isPerim = True
	for i in img:
		perims = []

		for p in i:
			lines = []

			plen = len(p)
			if plen > 2:
				i=0
				while i < (plen-1):
					v1 = Vert(float(p[i][0][0]), float(p[i][0][1]), 1.0)
					v2 = Vert(float(p[i+1][0][0]), float(p[i+1][0][1]), 1.0)
					lines.append(Line(v1, v2, Vert(0.0, 0.0, 1.0)))
					i+=1

				if (isPerim==False):
					v1 = Vert(float(p[i][0][0]), float(p[i][0][1]), 1.0)
					v2 = Vert(float(p[0][0][0]), float(p[0][0][1]), 1.0)
					lines.append(Line(v1, v2, Vert(0.0, 0.0, 1.0)))

				perims.append(lines)
		allperims.append(perims)
		isPerim = False

	return allperims

#########################
# GCode Printing
#########################

# GCode printing for perimeters
def gcode_perim(gcode, ls, n, first, fill):
	global extrude
	i = 0

	if fill:
		slow = 2000
		fast = 2200

		for line in ls:
			line.n.z = 0
			m = magnitude1v(line.n)
	else:
		slow = 2000
		fast = 2200

		for l in ls:
			for line in l:
				line.n.z = 0
				m = magnitude1v(line.n)

	if not fill:
		gcode.write(";PERIMLAYER:0\n")

	for l in ls:	
		size = len(l)

		# Go to starting point
		n1 = l[0].n 
		n2 = l[size-1].n
		norm = add(n1,n2)
		m = magnitude1v(norm)

		va = sub(l[0].v1,mult(norm, 1))
		vc = va
		if (size > 1): next_ind = 1 
		else: next_ind = 0

		if (first):
			gcode.write("G0 X%.3f" % va.x + " Y%.3f" % va.y + " Z%.3f" % (va.z+0.3) + " F%.1f\n" % slow)
			first = False
		else:
			gcode.write("G0 X%.3f" % va.x + " Y%.3f" % va.y + " F%.1f\n" % fast)
		
		for line in l:
			n1 = line.n 
			n2 = l[next_ind].n 

			norm = add(n1,n2)
			m = magnitude1v(norm)
			next_ind += 1
			if (next_ind > size-1): next_ind = 0

			vb = sub(line.v2, mult(norm,i))
			extrude += magnitude2v(vc,vb) * 0.1
			vc = vb
			gcode.write("G1 X%.3f" % vb.x + " Y%.3f" % vb.y + " E%.4f" % extrude + " F%.1f\n" % slow)

# GCode printing for infill
def gcode_infill(gcode, ls, first):
	global extrude
	last_time = True
	for l in ls:
		# Switch off
		if (last_time):
			va = l.v1
			vb = l.v2
			last_time = False
		else:
			va = l.v2
			vb = l.v1
			last_time = True

		# First time?
		if first:
			gcode.write("G0 X%.3f" % va.x + " Y%.3f" % va.y + " Z%.3f" % (va.z+0.3) + " F3000.0\n")
			first = False
		else:
			gcode.write("G0 X%.3f" % va.x + " Y%.3f" % va.y + " F3000.0\n")

		# Write the line	
		gcode.write("G1 X%.3f" % vb.x + " Y%.3f" % vb.y + " E%.4f" % extrude + " F20000.0\n")


#########################
# Main
#########################

def main():

	#################################
	# Option parser inputs
	#################################

	parser = OptionParser()

	parser.add_option("--out",
						dest="outF",
						default="out.gcode",
						help="gcode output file path")
	parser.add_option("--layer",
						dest="p_numlayers",
						default=1,
						help="number of perimeter layers")
	parser.add_option("--l",
						dest="levels",
						default=3,
						help="# of levels of shading: 1 perimeter, up to 3 levels of shading, 1 final")
	parser.add_option("--th",
						dest="p_layerthickness",
						default=.35,
						help="layer thickness")
	parser.add_option("--infill",
						dest="p_infill",
						default=1.0,
						help = "percent infill")
	parser.add_option("--in",
						dest="img",
						help = "img file")
	parser.add_option("--r",
						dest="radius",
						default=101.0,
						help = "blur radius, odd #")
	parser.add_option("--t",
						dest="tolerance",
						default=0.0,
						help = "Darkest layer: 0 default; abs val max 50; - for darker, + for lighter")
	parser.add_option("--t2",
						dest="tolerance2",
						default=-100.0,
						help = "Middle layer: 0 default; abs val max 50; - for darker, + if lighter")
	parser.add_option("--w",
						dest="white",
						default=5.0,
						help = "White tolerance, lower = more sensitive. Photos ~35. White background ~5.")
	parser.add_option("--flip", 
						action="store_true", 
						dest="flip",
						default=False,
						help = "Flip: for final print")
	parser.add_option("--img", 
						action="store_true", 
						dest="imagetoggle",
						default=False,
						help = "No arg required, flag will show the images")


	#################################
	# Set up the parser options
	#################################

	(parse,args) = parser.parse_args()
	if not parse.img:
		parser.error("input file path required as argument (-h for help)")

	parse.radius = float(parse.radius)
	parse.tolerance = float(parse.tolerance)
	parse.tolerance2 = float(parse.tolerance2)
	if parse.tolerance2 == -100.0:
		parse.tolerance2 = parse.tolerance
	parse.p_layerthickness = float(parse.p_layerthickness)
	parse.p_infill = float(parse.p_infill)
	parse.p_numlayers = int(parse.p_numlayers)
	parse.white = float(parse.white)
	levels = int(parse.levels)

	if parse.p_numlayers < 1:
		parser.error("num layers must be >= 1 (-h for help)")
	if parse.p_infill > 1.0:
		parser.error("percent infill must be <= 1 (-h for help)")

	# Epsilon for floating point error
	epsilon = 0.01


	#################################
	# Set up writing the output to a file
	#################################

	# Write the file
	gcode = open(parse.outF, 'w')

	# Write the starting g-code
	gcode.write("M104 S200.0\n")
	gcode.write("M109 S200.0\n")
	gcode.write("G21       ;metric values\n")
	gcode.write("G90       ;absolute positioning\n")
	gcode.write("M82       ;set extruder to absolute mode\n")
	gcode.write("M107      ;start with the fan off\n")
	gcode.write("G28 X0 Y0 ;home X/Y\n")
	gcode.write("G28 Z0    ;home Z\n")
	gcode.write("G92 E0    ;zero the extruded length\n")
	gcode.write("G29       ;initiate auto bed leveling sequence\n")
	gcode.write("G92 X132.4 Y20 ;correct bed origin (G29 changes it)\n")
	gcode.write("G0 X50.949 Y51.120 F6000.000\n")
	gcode.write("G1 Z0.361 F6000.000\n")
	gcode.write("G1 E2.00000 F1800.000\n")

	gcode.write("M107\n")
	gcode.write("G1 F1500.0 E-6.50000\n")

	allperims = processPancake(parse.img, parse.radius, parse.tolerance, 
		parse.tolerance2, parse.p_layerthickness, parse.white, parse.imagetoggle, parse.flip)


	#################################
	# PERIMETER ONLY LAYER
	#################################

	perims0 = allperims[0]

	first = True
	gcode.write(";PERIM:0\n")
	gcode_perim(gcode, perims0, parse.p_numlayers, first, False)


	#################################
	# DARKEST LAYER	
	#################################

	if(levels >= 2):
		perims1 = allperims[1]
		grid1 = infill_grid(perims1, parse.p_infill, parse.p_numlayers * parse.p_layerthickness)
		il1 = infill(perims1, grid1, parse.p_numlayers * parse.p_layerthickness)

		first = False
		gcode.write(";PERIM:0\n")
		gcode_perim(gcode, perims1, parse.p_numlayers, first, False)

		gcode.write(";INFILL:0\n")
		gcode_infill(gcode, il1, first)


	#################################
	# MIDDLE LAYER
	#################################

	if(levels >= 1):
		perims2 = allperims[2]
		grid2 = infill_grid(perims2, parse.p_infill, parse.p_numlayers * parse.p_layerthickness)
		il2 = infill(perims2, grid2, parse.p_numlayers * float(parse.p_layerthickness))

		gcode.write(";PERIM:0\n")
		gcode_perim(gcode, perims2, parse.p_numlayers, first, False)

		gcode.write(";INFILL:0\n")
		gcode_infill(gcode, il2, first)


	#################################
	# LIGHTEST LAYER
	#################################

	if(levels >= 3):
		perims3 = allperims[3]
		grid3 = infill_grid(perims3, parse.p_infill, parse.p_numlayers * parse.p_layerthickness)
		il3 = infill(perims3, grid3, parse.p_numlayers * float(parse.p_layerthickness))

		gcode.write(";PERIM:0\n")
		gcode_perim(gcode, perims3, parse.p_numlayers, first, False)

		gcode.write(";INFILL:0\n")
		gcode_infill(gcode, il3, first)


	#################################
	# FINAL INFILL PERIMETER
	#################################

	perims4 = allperims[4]
	grid4 = infill_grid(perims4, parse.p_infill, parse.p_numlayers * parse.p_layerthickness)
	il4 = infill(perims4, grid4, parse.p_numlayers * float(parse.p_layerthickness))

	gcode.write(";INFILL:0\n")
	gcode_infill(gcode, il4, first)


	#################################
	# Final GCode
	#################################

	gcode.write("G1 F1500.0 E374.01664\n")
	gcode.write("M107\n")
	gcode.write("M104 S0     ;extruder heater off\n")
	gcode.write("M140 S0     ;heated bed heater off (if you have it)\n")
	gcode.write("M106 S0     ;fan off\n")
	gcode.write("G91         ;relative positioning\n")
	gcode.write("G1 E-1 F300 ;retract the filament a bit\n")
	#gcode.write("G1 Z+1 E-5 F9000 ;move Z up a bit and retract even more\n")
	gcode.write("G28 X0 Y0   ;home X/Y, so the head is out of the way\n")
	gcode.write("M84         ;steppers off\n")
	gcode.write("G90         ;absolute positioning\n")
	gcode.write("M104 S0.0\n")
	gcode.write(";End of Gcode\n")
	gcode.close()

main()
