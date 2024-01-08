
class Coordinates:

    def __init__(self,x,y):
        if not isinstance(x, int) or not isinstance(y,int):
            raise ValueError("Coordinates must be integers")

        self.x = x
        self.y = y
