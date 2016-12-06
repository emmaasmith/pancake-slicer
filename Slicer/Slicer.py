import numpy
import sys
import math
import os
import cv2

from Intersections import buildPerimeter
from Intersections import perimeter
from Intersections import infill
from Intersections import infill_grid
#from Intersections import full_fill_grid
from Intersections import giveFillLayer
from Intersections import emptyFillLayer 
from Facet import Facet
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

def processPancake(imgurl, rad, tol):
	img = pancake(imgurl, rad, tol)

	perims = []
	for p in img:
		lines = []

		plen = len(p)
		if plen > 2:
			i=0
			while i < (plen-1):
				v1 = Vert(float(p[i][0][0]), float(p[i][0][1]), 1.0)
				v2 = Vert(float(p[i+1][0][0]), float(p[i+1][0][1]), 1.0)
				lines.append(Line(v1, v2, Vert(0.0, 0.0, 1.0)))
				i+=1
			v1 = Vert(float(p[i][0][0]), float(p[i][0][1]), 1.0)
			v2 = Vert(float(p[0][0][0]), float(p[0][0][1]), 1.0)
			lines.append(Line(v1, v2, Vert(0.0, 0.0, 1.0)))

			perims.append(lines)

	return perims

# Read in the STL file
# Generate a triangle mesh from STL file
def processSTL(inF, offset):
	facets = []
	o = Vert(float(offset),float(offset),0.0);
	with open(inF,'r') as f:
		line = f.readline()
		while 'endsolid' not in line:
			if 'normal' in line:
				l = line.split()
				normal = Vert(float(l[2]), float(l[3]), float(l[4]))
				line = f.readline()
				line = f.readline()
				l = line.split()
				v1 = Vert(float(l[1]), float(l[2]), float(l[3]))
				v1 = add(v1,o)
				line = f.readline()
				l = line.split()
				v2 = Vert(float(l[1]), float(l[2]), float(l[3]))
				v2 = add(v2,o)
				line = f.readline()
				l = line.split()
				v3 = Vert(float(l[1]), float(l[2]), float(l[3]))
				v3 = add(v3,o)
				facet = Facet(v1, v2, v3, normal)
				facets.append(facet)
			line = f.readline()
	return facets

# Find height of mesh
def findHeight(mesh):
	maxz = 0
	for f in mesh:
		maxz = max([f.v1.z, f.v2.z, f.v3.z, maxz])
	return maxz


##### gcode helpers

def find_norm(v1,v2,v3):
	v12 = sub(v1,v2)
	v13 = sub(v1,v3)
	n12 = Vert(v12.y,-1*v12.x)
	d = dot(n12,v13)
	if d < 0:
		n12 = mult(n12,-1)
	n12.z = 0
	m = magnitude1v(n12)
	n12 = div(n12,m)
	return n12

def gcode_fill(gcode,perim,epsilon,first):
	lines = []
	found = False
	norm = Line(0.0, 0.0, 0.1)
	
	for l in perim:
		lines.append(l)

	# find range
	minx = lines[0].v1.x
	maxx = lines[0].v1.x
	miny = lines[0].v1.y
	maxy = lines[0].v1.y
	for l in lines:
		minx = min(minx, l.v1.x, l.v2.x)
		maxx = max(maxx, l.v1.x, l.v2.x)
		miny = min(miny, l.v1.y, l.v2.y)
		maxy = max(maxy, l.v1.y, l.v2.y)
	d = min((maxx - minx), (maxy - miny))
	s = len(perim)
	d = d / (s*2)
	i = ((s-1) * .6)
	if s == 1: 
		d = int(d)
	elif s == 2:
		d = int(d*i)
	elif 8 > s > 2:
		d = 0
	print "D is ", d
	gcode_perim(gcode, perim, int(d), first, True)

def gcode_perim(gcode,ls,n,first,fill):
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

	for i in range(n):
		if not fill:
			gcode.write(";PERIMLAYER:%d\n" % i)
		for l in ls:	
			size = len(l)

			# go to starting point
			n1 = l[0].n 
			n2 = l[size-1].n
			norm = add(n1,n2)
			m = magnitude1v(norm)

			va = sub(l[0].v1,mult(norm,i)) # approx nozzle thickness
			vc = va
			if (size > 1): next_ind = 1 
			else: next_ind = 0
			if (first):
				gcode.write("G0 X%.3f" % va.x + " Y%.3f" % va.y + " Z%.3f" % (va.z+0.3) + " E0" + " F%.1f\n" % slow)
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

				vb = sub(line.v2,mult(norm,i))
				extrude += magnitude2v(vc,vb) * 0.05
				vc = vb
				gcode.write("G1 X%.3f" % vb.x + " Y%.3f" % vb.y + " E%.4f" % extrude + " F%.1f\n" % slow)

def gcode_infill(gcode, ls, first, fill):
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

		# # Is this for infill
		# if fill:
		# 	extrude += magnitude2v(va,vb) * 0.2
		# else:
		# 	extrude += magnitude2v(va,vb) * 0.05

		# First time?
		if first:
			gcode.write("G0 X%.3f" % va.x + " Y%.3f" % va.y + " Z%.3f" % (va.z+0.3) + " E0" + " F3000.0\n")
			first = False
		else:
			gcode.write("G0 X%.3f" % va.x + " Y%.3f" % va.y + " E0" + " F3000.0\n")

		# Write the line	
		gcode.write("G1 X%.3f" % vb.x + " Y%.3f" % vb.y + " E%.4f" % extrude + " F20000.0\n")


def gcode_support(gcode,supports,x):
	global extrude

	for s in supports:
		# support bottom to s.z -> doesn't deal with supports onto mesh TODO
		if x < s.z:
			gcode.write("G0 X%.3f" % s.x + " Y%.3f" % s.y + " F3000.0\n")
			extrude += .01
			gcode.write("G1 X%.3f" % (s.x+0.1) + " Y%.3f" % (s.y+0.1) + " E%.4f" % extrude + " F2200.0\n") 
			# TODO



######### MAIN

def main():
	##### Set up parameters
	parser = OptionParser()
		# parsing
	parser.add_option("--out",
						dest="outF",
						default="out.gcode",
						help="gcode output file path")
	parser.add_option("--layer",
						dest="p_numlayers",
						default=2,
						help="number of perimeter layers")
	parser.add_option("--thick",
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
	parser.add_option("--radius",
						dest="radius",
						default=101,
						help = "blur radius, odd #")
	parser.add_option("--tolerance",
						dest="tolerance",
						default=250,
						help = "tolerance 1-300")
	(parse,args) = parser.parse_args()
	# if not parse.inF:
		# parser.error("input file path required as argument (-h for help)")
	if int(parse.p_numlayers) < 1:
		parser.error("num layers must be >= 1 (-h for help)")
	if float(parse.p_infill) > 1:
		parser.error("percent infill must be <= 1 (-h for help)")

	# epsilon for floating point error
	epsilon = 0.01

	##### Set up writing the output to a file
	# write the file
	gcode = open(parse.outF, 'w')

	# write the starting g-code
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
	gcode.write("G1 X50.949 Y51.120 F6000.000\n")
	gcode.write("G1 Z0.361 F6000.000\n")
	gcode.write("G1 E2.00000 F1800.000\n")

	##### Process the STL and build a mesh, supports, infill grid
	# mesh = processSTL(parse.inF,45)
	perims = processPancake(parse.img, parse.radius, parse.tolerance)

	# for p in perims:
	# 	print "Perim"
	# 	for l in p:
	# 		print l.v1.x, l.v1.y, l.v1.z
	# 		print l.v2.x, l.v2.y, l.v2.z
	# 	print " "

	# supports = support(mesh, epsilon)

	# ht = float(findHeight(mesh))
	grid = infill_grid(perims, float(parse.p_infill), int(parse.p_numlayers))

	# # Determine the layers and build perimeters
	# x = float(0.0)
	# fills = []
	# infill_lines = []
	# layer = 0

	# while (x <= ht):
	# Build a plane
	# plane = Plane(x, Vert(0, 0, 1))

	# Build perimeters by connecting the points into lines
	# print ls 

	# fl = giveFillLayer()
	# fills.append(fl)
	# emptyFillLayer()
	# allperims = [item for l in perims for item in l]

	# Perims is an array (item = each perimeter) of arrays (item = each line)
	# print "Num perims: ", len(perims)
	# x=0
	# for lns in perims:
	# 	x += len(lns)
	# print "Num lines: ", x
	il = infill(perims, grid, int(parse.p_numlayers) * float(parse.p_layerthickness))


	# infill_lines.append(il)

	# if (ht > x >= ht - float(parse.p_layerthickness)):
	# 	x = ht
	# else:
	# 	x += .2 #float(parse.p_layerthickness)
	# layer += 1

	# #print gcode to file line by line
	# layer = 0
	# x = float(parse.p_layerthickness)
	# while (x < (ht+.4)): #(ht+(2*float(parse.p_layerthickness)))):
	# 	gcode.write(";LAYER:" + str(layer) + "\n")
	# 	if (layer == 0):
	gcode.write("M107\n")
	gcode.write("G1 F1500.0 E-6.50000\n")
	# 	if (layer == 1):
	# 		gcode.write("M106 S255.0\n");

	first = True
	# 	if fills[layer]:




	# gcode.write(";FILLLAYER:0\n")
	# for p in perims:
	# 	gcode_fill(gcode, p, epsilon, first)




	# for p in perims:
	# 	print "Perim"
	# 	for l in p:
	# 		print l.v1.x, l.v1.y, l.v1.z
	# 		print l.v2.x, l.v2.y, l.v2.z
	# 		print " "




	# print il

	# 		first = False
	gcode.write(";PERIM:0\n")
	gcode_perim(gcode, perims, int(parse.p_numlayers), first, False)

	gcode.write(";INFILL:0\n")
	gcode_infill(gcode, il, first, False)

	# 	# gcode.write(";SUPPORT:" + str(layer) + "\n")
	# 	# gcode_support(gcode, supports, x)

	# 	x += .2 #float(parse.p_layerthickness)
	# 	layer += 1

	# write end gcode
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
