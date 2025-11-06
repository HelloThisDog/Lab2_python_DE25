from numbers import Number 
import math 
from shapes_position import ShapesPosition 
"""this is the Cricle class, it has inherited x and y off of ShapesPosition

The reason why it is a diffrent class and seperated from rektangle is quite simple, its diffrent types of math on both shapes
with the circle needing pi to do its math, while the rektangle doesn't"""
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
    
    @radius.setter
    def radius(self, value):
        self._radius = value
    
    
    @property
    def perimeter(self): #the perimeter math
        return self.radius * 2 * math.pi
    
    @property
    def area(self): #the area math
        return math.pi * self.radius ** 2
    
    """operator over load area"""
    def __str__(self):
        return f"Cricle, Radius = {self.radius}, center at {self.x}, {self.y}"
    
    def __repr__(self):
        return f"Cricle(x={self.x}, y={self.y}, radius={self.radius})"
    
    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise TypeError(f"Can't compare {type(other)} it has to be a circle")
        return self.radius == other.radius
    
    def __gt__(self, other):
        if not isinstance(other, Circle):
            raise TypeError(f"Can't cimpare {type(other)} it has to be a circle")
        return self.radius > other.radius
    
    def __lt__(self, other):
        if not isinstance(other, Circle):
            raise TypeError(f"can't compare {type(other)} it has to be a circle")
        return self.radius < other.radius
    
    def __ge__(self, other):
        if not isinstance(other, Circle):
            raise TypeError(f"can't compare {type(other)} it has to be a circle")
        return self.radius >= other.radius
    
    def __le__(self, other):
        if not isinstance(other, Circle):
            raise TypeError(f"can't compare {type(other)} it has to be a circle")
        return self.radius <= other.radius