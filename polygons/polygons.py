import math
from math import tan, pi

# implementing a parent class of polygons


class Polygon:
    def __init__(self, Num_sides):
        self.Num_sides = Num_sides

    def polygon_type(self):
        '''
        :return: a string indicating the type of the polygon
        '''
        if self.Num_sides is 3:
            return "Triangle"
        elif self.Num_sides is 4:
            return "Rectangle"
        elif self.Num_sides is 0:
            return "Circle"
        else:
            return "Polygon"

    def number_of_sides(self):
        '''
        :return: the number of the sides of the polygon
        '''
        return self.Num_sides

    def area(self, side_length):
        '''
        calculate the area of a regular polygon
        :param side_lenght:
        :return: the area of a regular polygon , the formula is: (num-sides*side-length)/(4 * tan(pi/num-sides))
        '''
        self.side_length = side_length
        return (self.Num_sides * self.side_length) / (4 * tan(pi / self.Num_sides))

    def perimeter(self, side_length):
        '''
        calculate the perimeter of a regular polygon
        :parame_lenght:
        :return: number of sides multiplied by the side length of te polygon
        '''
        return self.Num_sides * self.side_length

# implementing the children classes from the class polygon , these classes are : Triangle , Rectangle & Circle


class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        '''
        The main initialization function of this class depends on initialization of polygon class by number of sides
        equal to 3
        :param side1:
        :param side2:
        :param side3:
        '''
        Polygon.__init__(self, 3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        '''
        This function calculates the area of the triangle by the general formula which is:
        1/(s*(s-a)(s-b)(s-c)) , where s = (a+b+c)/2
        :return: the calculated area
        '''
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * ((s - self.side1) * (s - self.side2) * (s - self.side3)))
        return area

    def perimeter(self):
        '''
        calculates the perimeter of the triangle - the general formula of calculating the perimeter -
        :return: the summation of the sides
        '''
        return self.side1 + self.side2 + self.side3


class Rectangle(Polygon):
    def __init__(self, width, length):
        '''
        The main initialization function of this class depends on initialization of polygon class by number of sides
        equal to 4
        :param width:
        :param length:
        '''
        Polygon.__init__(self, 4)
        self.width = width
        self.length = length

    def area(self):
        '''
        calculates the area of the rectangle
        :return: lenght * width
        '''
        return self.length * self.width

    def perimeter(self):
        '''
        calculates the perimeter of the rectangle
        :return: 2 times lenght times width
        '''
        return 2 * (self.length + self.width)


class Circle(Polygon):
    def __init__(self, radius):
        '''
        The main initialization function of this class depends on initialization of polygon class by number of sides
        equal to 0
        :param radius:
        '''
        Polygon.__init__(self, 0)
        self.radius = radius

    def area(self):
        return pi*self.radius**2

    def perimeter(self):
        return 2*pi*self.radius

# Creating some objects


polygon1 = Polygon(6)
print("The area of polygon1 is ", polygon1.area(3))
print("the perimeter of polygon1 is ", polygon1.perimeter(3))
polygon2 = Circle(9)
print("The type of polygon2 is ", polygon2.polygon_type()) # this function is called from the parent class -Polygon-
print("the area is ", polygon2.area()) # this is called from the child class -Circle-
polygon3 = Rectangle(4, 7)
print("The type of polygon3 is ", polygon3.polygon_type())
print("the perimeter of polygon is ", polygon3.perimeter(), " and the area is ", polygon3.area())
