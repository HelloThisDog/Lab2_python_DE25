from shapes_position import ShapesPosition
from numbers import Number
"""this is the rektangle class,
    the main goal with it? make the basis of a rektangle
    
    I followed what I already made from the circle class,
    but changed it so that it'd fit with a rektangle"""

class Rektangle(ShapesPosition):
    def __init__(self, x, y, height, length):
        super().__init__(x, y)

        if not isinstance(height, Number):
            raise TypeError(f"please put in a number not {height}")
        
        if not isinstance(length, Number):
            raise TypeError(f"please put in a number not {length}")
        
        if height <= 0:
            raise ValueError("numbers may not be below 0")
        
        if length <= 0:
            raise ValueError("numbers may not be below 0")
        
        self._height = height
        self._length = length
    

    @property
    def height(self):
        return self._height
    
    @property
    def length(self):
        return self._length
    
    @property
    def perimeter(self):
        return self._height * 2 + self._length * 2
    
    @property
    def area(self):
        return self._height * self._length
