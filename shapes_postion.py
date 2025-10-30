from numbers import Number

#this is going to be the parent class for the shapes
class ShapesPosition:
    #I'm basing this off of the OldCoinStash example from kokchun
    def __init__(self, x, y):
        if not isinstance(x, Number):
            raise TypeError(f"please put in a number not {x}")

        if not isinstance(y, Number):
            raise TypeError(f"please put in a number not {y}")
        
        self._x = x
        self._y = y


    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

        #this is the starting position of the shapes

#trying to follow the inheritance example from kokchun
class Circle(ShapesPosition):

    def __init__(self, x, y):
        super().__init__(x, y)