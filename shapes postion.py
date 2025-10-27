#this is going to be the parent class for the shapes
class ShapesPosition:
    #I'm basing this off of the OldCoinStash example from kokchun
    def __init__(self, shape):
        self.shape = shape
        # this is the starting position of the shapes
        self._x = 0
        self._y = 0
    
    def postion(self, x, y): #for now its going to avoid the negative positions
        if x <= 0 or y <= 0:
            raise ValueError(
                f"you can't place X at {x} position or Y at {y} position, they need to be above 0")
        
        self._x += x
        self._y += y

#trying to follow the inheritance example from kokchun
class Circle(ShapesPosition): #this doesn't feel right

    def __init__(self, shape):
        super().__init__(shape)
        self.radius = 1 #something is def not right