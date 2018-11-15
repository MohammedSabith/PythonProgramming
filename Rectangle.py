'''Design a class named Rectangle to represent a rectangle. class contains: 

Two data fields named width and heig
ht . 

A  constructor  that  creates  a  rectangle  with  the  specified  width  and 
height . 

The default values are 1 and 2 for the width and height, respectively.

A method named getArea() that returns the area of this rectangle. 

A method named getPerimeter() that
returns the perimeter. 
Write  a  test  program  that  creates  two  Rectangle  objects
—
one  with  width  4 
and height 40 and the other with width 3.5 and height 35.7. Display the width, 
height, area, and perimeter of each rectangle in this order'''

class Rectangle:

	def __init__(self,width=1.0,height=2.0):
		self.width = width
		self.height = height

	def getArea(self):
		area = self.width * self.height
		return area

	def getPerimeter(self):
		perimeter = (2 * self.width) + (2 * self.height)
		return perimeter


r1 = Rectangle(4,40)
r2 = Rectangle(3.5,35.7)
print("Rectangle 1 : \nwidth : ",r1.width," height : ",r1.height," area : ",r1.getArea()," perimeter : ",r1.getPerimeter())
print("Rectangle 2 : \nwidth : ",r2.width," height : ",r2.height," area : ",round(r2.getArea(),2)," perimeter : ",r2.getPerimeter())