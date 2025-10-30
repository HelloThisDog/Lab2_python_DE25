from numbers import Number 
import math 
from shapes_position import ShapesPosition #the parent class

class Circle(ShapesPosition):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        
        #validation area for the circle
        if not isinstance(radius, Number):
            raise TypeError(f"please put in a number not {radius}")
        
        if radius <= 0:
            raise ValueError("numbers may not be below 0")
        
        self._radius = radius 

    
    #these are to return the circles information
    @property 
    def radius(self):
        return self._radius
    
    @property
    def perimeter(self): #the perimeter math
        return self.radius * 2 * math.pi
    
    @property
    def area(self): #the area math
        return math.pi * self.radius ** 2