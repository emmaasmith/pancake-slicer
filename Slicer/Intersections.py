import numpy
import sys
import math
import os

from Facet import Facet
from Plane import Plane
from Line import Line
from Vert import Vert
from Vert import withinEpsilon

fillLayer = []

def giveFillLayer():
	fl = fillLayer
	return fl

def emptyFillLayer():
	global fillLayer
	fillLayer = []

class OrderedPt(object):
	# p: vert
	# ptid: int
	# lid: int
	
	def __init__(self, p, ptid, lid, n=Vert(0, 0, 0)):
		self.p = p
		self.ptid = ptid
		self.lid = lid
		self.n = n

# Line/plane intersection (for z plane, normal=(0, 0, 1)): return vert
	# return z=-1 if the line doesn't intersect or is on the plane
def intersectLineZ(l, pl, epsilon):
	# -1: Entirely on the plane
	if withinEpsilon(l.v1.z, l.v2.z, epsilon) and withinEpsilon(l.v1.z, pl.p, epsilon):
		return Vert(0, 0, -1)

	# -5: Entirely outside the plane
	if ((l.v1.z > (pl.p - epsilon) and l.v2.z > (pl.p - epsilon)) or (l.v1.z < (pl.p + epsilon) and l.v2.z < (pl.p + epsilon))):
		return Vert(0, 0, -5) 

	scaling = (pl.p - l.v1.z) / (l.v2.z - l.v1.z)

	return Vert((l.v1.x + (scaling * (l.v2.x-l.v1.x))),
		(l.v1.y + (scaling * (l.v2.y-l.v1.y))),
		pl.p)

# Point/line/normal identify side: return bool
# Line/line intersection: return vert

# Facet intersect: for a facet tri and plane, intersection test, return lines of intersection l[]
def intersectFacetZ(f, pl, epsilon):
	l1 = Line(f.v1, f.v2, f.n)
	l2 = Line(f.v1, f.v3, f.n)
	l3 = Line(f.v2, f.v3, f.n)
	ip1 = intersectLineZ(l1, pl, epsilon)
	ip2 = intersectLineZ(l2, pl, epsilon)
	ip3 = intersectLineZ(l3, pl, epsilon)

	# 0 v are on the plane, no intersect
	if (ip1.z == -5 and ip2.z == -5 and ip3.z == -5):
		return []
	# 3 v are on the plane
	if (ip1.z == -1 and ip2.z == -1 and ip3.z == -1):
	 	return [l1, l2, l3]

	# 1 edge overlaps (only need to test 1 edge == -1)
	if (ip1.z == -1):
		return [l1]
	if (ip2.z == -1):
		return [l2]
	if (ip3.z == -1):
		return [l3]

	# 1 vert only intersects
	# 1 vert and 1 edge intersect
		# if one vertex is on the z-plane, and the opposite edge is/not outside
	if (f.v1.z==pl.p):
		if (ip3.z == -5):
			return []
		else:
			return [Line(f.v1, ip3, f.n)]
	if (f.v2.z==pl.p):
		if (ip2.z == -5):
			return []
		else:
			return [Line(f.v2, ip2, f.n)]
	if (f.v3.z==pl.p):
		if (ip1.z == -5):
			return []
		else:
			return [Line(f.v3, ip1, f.n)]

	# 2 points of intersection (only need to test which edge is outside)
	if (ip3.z == -5):
		return [Line(ip1, ip2, f.n)]
	if (ip1.z == -5):
		return [Line(ip2, ip3, f.n)]
	if (ip2.z == -5):
		return [Line(ip1, ip3, f.n)]

	return []

# Perimeter order construction: input input array of facets and plane, build a perimeter p
def buildQuadTree(pts, epsilon, isx, d):
	# Base case: contains 
		# 0 endpoints, 
		# 1 endpoint (not a polygon), 
		# 2 endpoints not part of the same line (good!)
	if (len(pts)==0):
		return d
	if (len(pts)==1):
		d[pts[0].ptid] = -1
		return d
	if (len(pts)==2):
		# Add the relationship to the idctionary
		d[pts[0].ptid] = pts[1].ptid
		d[pts[1].ptid] = pts[0].ptid
		return d

	# Find the median index value
	med = (int)(len(pts)/2)

	# Sort the points by x or y and determine midpoints
	if isx==True:
		# Order all pts with their lowest x-coord first, increasing x order
		pts.sort(key=lambda l: l.p.x, reverse=False)
		# Find the nearest x coord line greater than epsilon away.
		left = []
		right = []
		mp = float(pts[med].p.x)
		lp = float(pts[med-1].p.x)
		gp = float(pts[med+1].p.x)

	else:
		# Order all pts with their lowest y-coord first, increasing y order
		pts.sort(key=lambda l: l.p.y, reverse=False)
		# Find the nearest x coord line greater than epsilon away.
		left = []
		right = []
		mp = float(pts[med].p.y)
		lp = float(pts[med-1].p.y)
		gp = float(pts[med+1].p.y)

	if (med%2==1):
		left = pts[0:med+1]
		right = pts[med+1:len(pts)]
	else:
		left = pts[0:med]
		right = pts[med:len(pts)]

	# Recursive return: build the tree
	return buildQuadTree(left, epsilon, not isx, (buildQuadTree(right, epsilon, not isx, d)))


def buildPerimeter(facets, plane, epsilon):
	global fillLayer
	lines = []
	for f in facets:
		ls = intersectFacetZ(f,plane,epsilon)
		if len(ls) == 3:
			fillLayer.append(f)
		else:
			lines.extend(ls)

	return perimeter(lines,epsilon)

def perimeter(lines,epsilon):
	# Build an unordered list of all points with their lineids
	pts = []
	lineid = 0
	ptid = 0
	linedict = {}
	for l in lines:
		linedict[lineid] = [ptid, ptid+1]
		pts.append(OrderedPt(l.v1, ptid, lineid, l.n))
		pts.append(OrderedPt(l.v2, ptid+1, lineid, l.n))
		lineid += 1
		ptid += 2

	# Build the quad tree
	synonyms = buildQuadTree(pts, epsilon, True, {})
	
	# Filter out lines that don't build the perimeter
	extralines = dict((k, v) for k, v in synonyms.iteritems() if v == -1)
	synonyms = dict((k, v) for k, v in synonyms.iteritems() if v != -1)

	# Final output and loops
	perimeters = []

	while synonyms:
		# Find the next perimeter to draw

		# Read the quad tree dictionary into a perimeter
		pts.sort(key=lambda l: l.ptid, reverse=False)
		perimeter = []

		# Start with line #0
		if not any(linedict):
			break
 
		nextline = linedict.iterkeys().next()
		firstpt = linedict[nextline][0]

		pt1 = linedict[nextline][0]
		pt2 = linedict[nextline][1]
		perimeter.append(Line(pts[pt1].p, pts[pt2].p, pts[pt1].n))

		# Loop through one perimeter until it circles
		while linedict:

			# take pt 2 and find its synonym. 
			if pt2 in extralines:
				del linedict[nextline]
				break

			pt1 = synonyms[pt2]

			# remove pt1 from synonyms, pt2 from pts
			del linedict[nextline]
			del synonyms[pt2]

			# find the lineid of pt 2's synonym
			nextline = pts[pt1].lid
			# find the other pt that shares that lineid
			if nextline in linedict:
				twopts = linedict[nextline]
				if twopts[0] == pt1:
					pt2 = twopts[1]
				else:
					pt2 = twopts[0]

				# add the pts for that lineid to perimeter
				perimeter.append(Line(pts[pt1].p, pts[pt2].p, pts[pt1].n))

				# remove pt1 from pts
				del synonyms[pt1]
			else:
				break


		perimeters.append(perimeter)


	### Data structure key:
	# synonyms: one ptid (by smaller index) to its synonym ptid (larger index)
	# linedict: lineid to two ptids
	# pts: list of points, ptid, lid (ordered by ptid index)

	return perimeters

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

def infill(lines, grid, n):
	# print "n is ", n
	newlines = []
	for gl in grid:
		# Vert is a list of all intersecting points: lines vs. gridlines
		vert = grid_intersect(lines, gl)
		
		i = 0
		if (withinEpsilon(gl.v1.x, gl.v2.x, 0.1)):
			vert = list(numpy.unique(vert))
			vert.sort(key = lambda v: v.y, reverse=False)
			# print "1 "
			# for v in vert:
			# 	print v.x, v.y, v.z
			# print " "
			while (i+1 < len(vert)):
				if abs(vert[i].y - vert[i+1].y) > n:
 					vert[i].y += n
 					vert[i+1].y -= n
 					newlines.append(Line(vert[i], vert[i+1]))
 					# print vert[i].x, vert[i].y, vert[i].z
 				# else:
					# print "abs ", abs(vert[i].y - vert[i+1].y)

				i += 2

		else:
			vert = list(numpy.unique(vert))
			vert.sort(key = lambda v: v.x, reverse=False)
			while (i+1 < len(vert)):
				if abs(vert[i].x - vert[i+1].x) > n:
 					vert[i].x += n
 					vert[i+1].x -= n
 					newlines.append(Line(vert[i], vert[i+1]))
 					# print "2", i
				i += 2

	# for nl in newlines:
	# 	print nl.v1.x, nl.v1.y, nl.v1.z
	# 	print nl.v2.x, nl.v2.y, nl.v2.z
	# 	print " "
	return newlines

# give lines l and percent infill k
def infill_grid(perims, k, n):
	minx = float('+inf')
	maxx = float('-inf')
	miny = float('+inf')
	maxy = float('-inf')
	z = perims[0][0].v1.z

	# find bounding area
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

	# dif = all steps
	# dif / n  = # of layers
	# dif / 100 = 1% filled
	# dif * x = x% (x is a decimal) filled
	# dif * x / n = # of layers

	stepx = n + (n * (1 - k))
	stepy = n + (n * (1 - k))
	if (stepy == 0 or stepx == 0):
		return []
	if (stepy < n): stepy = n
	if (stepx < n): stepx = n


	# infill grid lines
	grid=[]
	for x in numpy.arange(lowx, hix, stepx):
		grid.append(Line(Vert(x, miny, z), Vert(x, maxy, z)))
	for y in numpy.arange(lowy, hiy, stepy):
		grid.append(Line(Vert(minx, y, z), Vert(maxx, y, z)))

	return grid

def full_fill_grid(facets,n):
	minx = float('+inf')
	maxx = float('-inf')
	miny = float('+inf')
	maxy = float('-inf')
	z = facets[0].v1.z # all z should be the same

	# find bounding area
	for f in facets:
		if (f.v1.x < minx): minx = float(f.v1.x)
		if (f.v1.y < miny): miny = float(f.v1.y)
		if (f.v1.x > maxx): maxx = float(f.v1.x)
		if (f.v1.y > maxy): maxy = float(f.v1.y)
		if (f.v2.x < minx): minx = float(f.v2.x)
		if (f.v2.y < miny): miny = float(f.v2.y)
		if (f.v2.x > maxx): maxx = float(f.v2.x)
		if (f.v2.y > maxy): maxy = float(f.v2.y)
		if (f.v3.x < minx): minx = float(f.v3.x)
		if (f.v3.y < miny): miny = float(f.v3.y)
		if (f.v3.x > maxx): maxx = float(f.v3.x)
		if (f.v3.y > maxy): maxy = float(f.v3.y)

	lowx = minx + (n*0.2)
	hix = maxx - (n*0.2)

	# grid lines
	grid=[]
	for x in numpy.arange(lowx,hix,.8):
		grid.append(Line(Vert(x,miny,z),Vert(x,maxy,z)))
	return grid


