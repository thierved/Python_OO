class Point:
    ''' Creates a point in RXR '''

    def __init__(self, x=0, y=0):
        self.move(x, y)
      
    def move(self, x=1, y=1):
        'Translate the point to (x, y)'
        self._x = x
        self._y = y

    def reset(self):
        'Resets the point the default origin'
        self.move(0, 0)

    def point_position(self):
        'Displays the coordonate of the point'
        print(self._x, self._y)