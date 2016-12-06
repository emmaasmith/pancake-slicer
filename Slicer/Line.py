import math

from Vert import Vert
from Vert import equalv

class Line(object):
	# v1: vert
	# v2: vert
	# optional n: vert (normal)

	def __init__(self, v1, v2, n=Vert(0, 0, 0)):
		self.v1 = v1
		self.v2 = v2
		self.n = n

	def newv1(self, p):
		self.v1 = p

	def newv2(self, p):
		self.v2 = p

	def addX(self, dx):
		self.v1.x = self.v1.x + dx
		self.v2.x = self.v1.x + dx

	def addY(self, dy):
		self.v1.x = self.v1.y + dy
		self.v2.x = self.v1.y + dy

	def addZ(self, dz):
		self.v1.x = self.v1.z + dz
		self.v2.x = self.v1.z + dz

def makeLine(v1, v2):
    l = Line(v1, v2)
    return l

def magnitude1l(l):
	return sqrt((l.v2.x - l.v1.x)^2 + (l.v2.y - l.v1.y)^2 + (l.v2.z - l.v1.z)^2)

def angle(l1, l2):
    return arcos(dot(l1, l2) / (magnitude1l(l1) * magnitude1l(l2)))

def equall(l1, l2):
	if ((equalv(l1.v1, l2.v1) and equalv(l1.v2, l2.v2))
		or (equalv(l1.v1, l2.v2) and equalv(l1.v2, l2.v1))):
		return True
	else:
		return False