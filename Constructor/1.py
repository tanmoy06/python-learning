class Point:
    # __init__ is a constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(10, 20)
point1.draw()
# point1.x = 10
# point1.y = 34
print(point1.x)
