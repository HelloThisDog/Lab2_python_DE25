from numbers import Number 

"""This is the parent class that all the shapes are using as their base

I've based this off the inheritence examples from kokchuns repos.

this is effectively the starting positions of the shapes, x and y are read only modules, you don't really need to see the starting positions"""

class ShapesPosition:

    def __init__(self, x, y):
        if not isinstance(x, Number):
            raise TypeError(f"please put in a number not {x}")
        #this is the validation area for x and y
        if not isinstance(y, Number):
            raise TypeError(f"please put in a number not {y}")
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    #these return x and y, more specifically the changed version of them
    @property
    def y(self):
        return self._y

