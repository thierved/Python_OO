class Point:
    ''' Creates a point in RXR '''

    def __init__(self, x=0, y=0):
        self.move(x, y)
      
    def move(self, x=1, y=1):
        'Translate the point to (x, y)'
        self.x = x
        self.y = y

    def reset(self):
        'Resets the point the default origin'
        self.move(0, 0)

    def point_position(self):
        'Displays the coordonate of the point'
        print(self.x, self.y)

a = Point()
a.point_position()
a.move(5, 2)
a.point_position()
a.reset()
a.point_position()
