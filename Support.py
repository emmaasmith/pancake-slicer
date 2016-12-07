import numpy
import sys
import math
import os

from Facet import Facet
from Plane import Plane
from Line import Line
from Vert import Vert
from Vert import withinEpsilon

def support(facets, epsilon):
	vs = []
	verts = []
	for f in facets:
		if f.v1.z > 0.0:
			arr = [f.v1.x, f.v1.y, f.v1.z]
			if arr not in vs:
				vs.append(arr)
		if f.v2.z > 0.0:
			arr = [f.v2.x, f.v2.y, f.v2.z]
			if arr not in vs:
				vs.append(arr)
		if f.v3.z > 0.0:
			arr = [f.v3.x, f.v3.y, f.v3.z]
			if arr not in vs:
				vs.append(arr)

	for v in vs:
		verts.append(Vert(v[0], v[1], v[2]))

	supports = []

	# sort by ascending z
	facets.sort(key = lambda f: f.v1.z, reverse=False)
	verts.sort(key = lambda x: x.z, reverse=False)

	# for every vertex of a facet
	for v in verts:
		check = support_help(v, facets, supports, epsilon)
		if check:
			supports.append(check)

	return supports

def support_help(v, facets, supports, epsilon):
	e = epsilon * 80

	if outside(v, facets, e, epsilon): 
		if not bound(v, supports, e):
			return v

# True: the vert v doesn't intersect a downward-facing vert
# False: it does
def outside(v, facets, e, epsilon):
	d = .5
	down = 0

	for f in facets:
		d1 = v.z - f.v1.z
		d2 = v.z - f.v2.z
		d3 = v.z - f.v3.z
		# only check facets below v
		if (abs(d1) > epsilon and abs(d2) > epsilon and abs(d3) > epsilon) and (d1 > epsilon or d2 > epsilon or d3 > epsilon):
			# v area intersects with facet
			if (infacet(v, f)):
				# or close enough to facet that no support is needed

				# intersected facet is face down (infill will act as support)
				if (abs(f.n.z) < epsilon) and (d1 < d or d2 < d or d3 < d):
					return False
				elif (f.n.z < 0.0):
					down += 1
				else:
					down -= 1
	if down == 0:
		return True
	else:
		return False


# check if vert v is in bounding rectangle of any existing support (if so, don't build one)
def bound(v, supports, e):
	for s in supports:
		minx = s.x - e
		maxx = s.x + e
		miny = s.y - e
		maxy = s.y + e
		if (minx <= v.x <= maxx and miny <= v.y <= maxy):
			return True
	return False

def sign(p1, p2, p3):
    sign = (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

    if sign <= 0.0:
    	return True
    else:
    	return False


def infacet (v, f):
    b1 = sign(v, f.v1, f.v2)
    b2 = sign(v, f.v2, f.v3)
    b3 = sign(v, f.v3, f.v1)
    if ((b1 == b2) and (b2 == b3)):
    	return True
    else:
    	return False


