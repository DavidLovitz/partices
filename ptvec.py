import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        xdiff = self.x - other.x
        ydiff = self.y - other.y
        dist = math.sqrt((xdiff**2)+(ydiff**2))
        return dist

    def move(self, vector):
        self.x += vector.horizontal
        self.y += vector.vertical

    def makeVectorTo(self, them):
        vect = Vector(them.x-self.x, them.y-self.y)
        return vect

class Vector:
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    def length(self):
        length = math.sqrt(self.horizontal**2 + self.vertical**2)
        return length

    def add(self, them):
        horiz = self.horizontal + them.horizontal
        vert = self.vertical + them.vertical
        return Vector(horiz, vert)

    def subtract(self, them):
        horiz = self.horizontal - them.horizontal
        vert = self.vertical - them.vertical
        return Vector(horiz,vert)

    def multiply(self, number):
        horiz = self.horizontal * number
        vert = self.vertical * number
        return Vector(horiz,vert)

    def divide(self, number):
        if number > 0:
            horiz = self.horizontal / number
            vert = self.vertical / number
            return Vector(horiz,vert)

    def normalize(self):
        if (self.length() == 0.0):
            #print "divide zero"
            return Vector(0.0,0.0)
        horiz = self.horizontal/self.length()
        vert = self.vertical/self.length()
        return Vector(horiz, vert)
