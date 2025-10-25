class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y
    
    def __init__(self, rho, theta):
        self.rho = rho
        self.theta = theta
#--------------------
## cant be done because init can be overloaded with same values
from enum import Enum
from math import *
class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Point:
    def __init__(self, a, b, system):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        if system == CoordinateSystem.POLAR:
            self.x = a *cos(b)
            self.y = a *sin(b)
#-------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'x: {self.x} y: {self.y}'
    
    @staticmethod
    def new_cartesian_point(x,y):
        return Point(x,y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho*cos(theta), rho*sin(theta))

p = Point(2,2)
p1 = Point.new_cartesian_point(2,2)
print(p1)
p2 = Point.new_polar_point(2,2)
print(p2)

#-------------------
class PointFactory:
    @staticmethod
    def new_cartesian_point(x,y):
        return Point(x,y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho*cos(theta), rho*sin(theta))

p1 = PointFactory.new_cartesian_point(2,2)
print(p1)
p2 = PointFactory.new_polar_point(2,2)
print(p2)
#----------- discoverablity
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'x: {self.x} y: {self.y}'
    class PointFactory:
        def new_cartesian_point(x,y):
            return Point(x,y)

        def new_polar_point( rho, theta):
            return Point(rho*cos(theta), rho*sin(theta))

p1 = Point.PointFactory.new_cartesian_point(2,2)
print(p1)
