import numpy
import sys
import math
import os

from Plane import Plane
from Line import Line
from Vert import Vert
from Vert import withinEpsilon

class OrderedPt(object):
	# p: vert
	# ptid: int
	# lid: int
	
	def __init__(self, p, ptid, lid, n=Vert(0, 0, 0)):
		self.p = p
		self.ptid = ptid
		self.lid = lid
		self.n = n

# Test grid intersection for infill
def grid_intersect(lines, gl):
	vert = []
	for p in lines:
		for l in p:
			s1_x = l.v2.x - l.v1.x
			s1_y = l.v2.y - l.v1.y
			s2_x = gl.v2.x - gl.v1.x
			s2_y = gl.v2.y - gl.v1.y
			d = (-s2_x * s1_y + s1_x * s2_y)
			if (d == 0):
				s = t = -1
			else:
				s = (-s1_y * (l.v1.x - gl.v1.x) + s1_x * (l.v1.y - gl.v1.y)) / d
				t = ( s2_x * (l.v1.y - gl.v1.y) - s2_y * (l.v1.x - gl.v1.x)) / d
			# intersection
			if (0 <= s <= 1 and 0 <= t <= 1):
				vert.append(Vert(l.v1.x + (t * s1_x), l.v1.y + (t * s1_y), l.v1.z))
	# print "Num intersect: ", len(vert)
	return vert 

# Create infill for region
def infill(lines, grid, n):
	newlines = []
	for gl in grid:
		# Vert is a list of all intersecting points: lines vs. gridlines
		vert = grid_intersect(lines, gl)
		
		i = 0
		if (withinEpsilon(gl.v1.x, gl.v2.x, 0.1)):
			vert = list(numpy.unique(vert))
			vert.sort(key = lambda v: v.y, reverse=False)

			while (i+1 < len(vert)):
				if abs(vert[i].y - vert[i+1].y) > n:
 					vert[i].y += n
 					vert[i+1].y -= n
 					newlines.append(Line(vert[i], vert[i+1]))

				i += 2

		else:
			vert = list(numpy.unique(vert))
			vert.sort(key = lambda v: v.x, reverse=False)
			while (i+1 < len(vert)):
				if abs(vert[i].x - vert[i+1].x) > n:
 					vert[i].x += n
 					vert[i+1].x -= n
 					newlines.append(Line(vert[i], vert[i+1]))
				i += 2

	return newlines

# Build an infill grid
def infill_grid(perims, k, n):
	minx = float('+inf')
	maxx = float('-inf')
	miny = float('+inf')
	maxy = float('-inf')
	z = perims[0][0].v1.z

	# Calculate bounding area
	for p in perims:
		for l in p:
			minx = min(minx, l.v1.x, l.v2.x)
			maxx = max(maxx, l.v1.x, l.v2.x)
			miny = min(miny, l.v1.y, l.v2.y)
			maxy = max(maxy, l.v1.y, l.v2.y)

	lowx = minx + (n*0.35) + 0.1
	lowy = miny + (n*0.35) + 0.1
	hix = maxx - (n*0.35) - 0.1
	hiy = maxy - (n*0.35) - 0.1
	maxx += 1
	maxy += 1
	minx -= 1
	miny -= 1
	if (k > 0.95): k = 0.95
	if (k > 0.95): k = 0.95
	stepx = n + (n * (1 - k))
	stepy = n + (n * (1 - k))
	if (stepy == 0 or stepx == 0):
		return []
	if (stepy < n): stepy = n
	if (stepx < n): stepx = n

	# Infill grid lines
	grid=[]
	for x in numpy.arange(lowx, hix, stepx):
		grid.append(Line(Vert(x, miny, z), Vert(x, maxy, z)))
	
	# Used for two-dimensional infill

	# for y in numpy.arange(lowy, hiy, stepy):
	# 	grid.append(Line(Vert(minx, y, z), Vert(maxx, y, z)))

	return grid
