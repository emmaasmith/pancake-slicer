import math

from Line import Line
from Vert import Vert


class Plane(object):
	# p: float (dist from origin)
	# n: vert

	def __init__(self, p, n):
		self.p = p
		self.n = n

	def newp(self, p):
		self.p = p

	def newn(self, n):
		self.n = n

def makePlane(p, n):
    pl = Plane(p, n)
    return pl

def equalpl(pl1, pl2):
	if pl1.p==pl2.p and equall(pl1.n, pl2.n):
		return True
	else:
		return False

