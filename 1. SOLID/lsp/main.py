from rectangle import Rectangle
from square import Square

def use_shape(shape):
    width = shape.width
    shape.height = 10
    expected_area = width * 10
    actual_area = shape.area
    print(f"Expected area: {expected_area}")
    print(f"Actual area: {actual_area}")

r = Rectangle(2, 3)
use_shape(r)

s = Square(5)
use_shape(s)