import sys
import math

class Vert(object):
	# x: float
	# y: float
	# z: float
	
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	def addX(self, dx):
		self.x = self.x + dx

	def addY(self, dy):
		self.y = self.y + dy

	def addZ(self, dz):
		self.z = self.z + dz


def withinEpsilon(x, y, epsilon):
	if abs(float(x) - float(y)) < epsilon:
		return True
	else:
		return False
		
def makeVert(x, y, z):
	v = Vert(x, y, z)
	return v

def add(v1, v2):
	x = v1.x + v2.x
	y = v1.y + v2.y
	z = v1.z + v2.z
	v = Vert(x,y,z)
	return v

def sub(v1, v2):
	x = v1.x - v2.x
	y = v1.y - v2.y
	z = v1.z - v2.z
	v = Vert(x,y,z)
	return v

def mult(v1, i):
	x = v1.x * i
	y = v1.y * i
	z = v1.z * i
	v = Vert(x,y,z)
	return v

def div(v1, i):
	x = v1.x / i
	y = v1.y / i
	z = v1.z / i
	v = Vert(x,y,z)
	return v

def dot(v1, v2):
	return (v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z)

def magnitude1v(v):
	return math.sqrt(pow(v.x,2) + pow(v.y,2) + pow(v.z,2))

def magnitude2v(v1, v2):
	return math.sqrt(pow(v2.x - v1.x,2) + pow(v2.y - v1.y,2) + pow(v2.z - v1.z,2))

def equalv(v1, v2):
	if v1.x == v2.x and v1.y == v2.y and v1.z == v2.z:
		return True
	else:
		return False

