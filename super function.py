class Area:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Area):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width


class Cube(Area):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Square(3, 4)
print("Area of square : ", square.area())

cube = Cube(3, 4, 5)
print(" Volume of Cube : ", cube.volume())
