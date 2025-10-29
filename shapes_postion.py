#this is going to be the parent class for the shapes
class ShapesPosition:
    #I'm basing this off of the OldCoinStash example from kokchun
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def postion(self, x, y): #for now its going to avoid the negative positions
        if x <= 0 or y <= 0:
            raise TypeError(
                f"you can't place X at {x} position or Y at {y} position, they need to be above 0") #change message
        #this is the starting position of the shapes
        self._x += int(x)
        self._y += int(y)

#trying to follow the inheritance example from kokchun
class Circle(ShapesPosition): #this doesn't feel right

    def __init__(self, shape):
        super().__init__(shape)
        self.radius = float(1) #something is def not right