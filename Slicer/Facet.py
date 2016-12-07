import math

from Plane import Plane
from Line import Line
from Vert import Vert


class Facet(object):
	# v1: vert
	# v2: vert
	# v3: vert
	# n: vert

	def __init__(self, v1, v2, v3, n):
		self.v1 = v1
		self.v2 = v2
		self.v3 = v3
		self.n = n

def makeFacet(v1, v2, v3, n):
    f = Facet(v1, v2, v3, n)
    return f

def equal(f1, f2):
	if (equalv(f1.v1, f2.v1) and equalv(f1.v2, f2.v2) and 
		equalv(f1.v3, f2.v3) and equalv(f1.n, f2.n)):
		return True
	else:
		return False
