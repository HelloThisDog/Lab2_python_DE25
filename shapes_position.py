from numbers import Number #x and y need their numbers

#this is going to be the parent class for the shapes
class ShapesPosition:
    #I'm basing this off of the OldCoinStash example from kokchun
    #this is the starting position of the shapes
    def __init__(self, x, y):
        if not isinstance(x, Number):
            raise TypeError(f"please put in a number not {x}")
        #this is the validation area for x and y
        if not isinstance(y, Number):
            raise TypeError(f"please put in a number not {y}")
        #made x and y read only, becuase you don't need to see the starting position
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    #these return x and y, more specifically the changed version of them
    @property
    def y(self):
        return self._y

