from shape import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Width: {self.width}, Height: {self.height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width


    @property
    def height(self):
        return self._height


    @height.setter
    def height(self, height):
        self._height = height