'''
Design a class named Triangle that extends the GeometricObject class. The Triangle
class contains:
* Three float data fields named side1 , side2 , and side3 to denote the three
sides of the triangle.
* A constructor that creates a triangle with the specified side1 , side2 , and
side3 with default values 1.0 .
* The accessor methods for all three data fields.
* A method named getArea() that returns the area of this triangle.
* A method named getPerimeter() that returns the perimeter of this triangle.
* A method named _ _str_ _() that returns a string description for the triangle.
Write a test program that prompts the user to enter the three sides of the triangle, a
color, and 1 or 0 to indicate whether the triangle is filled. The program should create
a Triangle object with these sides and set the color and filled properties using the
input. The program should display the triangle’s area, perimeter, color, and True or
False to indicate whether the triangle is filled or not.
'''

import math

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


sx = []
sx = input("Enter sides : ").split(" ")
c = input("Enter color : ")
f = int(input("Enter filled 0/1 :"))

print(type(sx[0]))

t1 = Triangle(c,f,int(sx[0]),int(sx[1]),int(sx[2]))

print(t1)


