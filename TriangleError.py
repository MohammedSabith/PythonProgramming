import math
import sys

class RunTimeError(Exception):
	pass

class TriangleError(RunTimeError):
	def __init__(self,side1,side2,side3):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

	def getSide1(self):
		return self.side1

	def getSide2(self):
		return self.side2

	def getSide3(self):
		return self.side3

	def printError(self):
		print("The three sides cannot make a triangle")
		sys.exit()


class GeometricObject:
	def __init__(self,color,filled):
		self.color = color
		self.filled = filled

	def getArea(self):
		pass

	def getPerimeter(self):
		pass


class Triangle(GeometricObject):

	def __init__(self,color,filled,side1=1.0,side2=1.0,side3=1.0):
		GeometricObject.__init__(self,color,filled)

		try:
			if(((side1 + side2) < side3) or ((side1 + side3) < side2) or ((side3 + side2) < side1)):
				raise TriangleError(side1,side2,side3)
		except TriangleError:
			TriangleError.printError(self)


		self.side1 = side1
		self.side2 = side2
		self.side3 = side3


		

	def getSide1(self):
		return self.side1

	def getSide2(self):
		return self.side2

	def getSide3(self):
		return self.side3

	def getPerimeter(self):
		return self.side1 + self.side2 + self.side3

	def getArea(self):
		# height = math.sqrt((self.side1**2) - ((self.side3/2)**2))
		# area = 0.5 * self.side3 * height

		p = self.getPerimeter() / 2
		area = math.sqrt(p * (p-self.side1) * (p-self.side2) * (p-self.side3))
		return round(area,2)

	def __str__(self):

		st = "side1 : "+str(self.side1)+"\nside2 : "+str(self.side2)
		st += "\nside3 : "+str(self.side3)+"\nArea : "+str(self.getArea())
		st += "\nPerimeter : "+str(self.getPerimeter())+"\nColor : "+self.color
		st += "\nfilled : "+str(self.filled)+"\n"

		return st


t1 = Triangle("red",1)
print(t1)

t2 = Triangle("blue",0,6,6,6)
print(t2)