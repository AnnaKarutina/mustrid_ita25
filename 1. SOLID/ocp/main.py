from product import Product
from color import Color
from size import Size
from color_spec import  ColorSpecification
from size_spec import SizeSpecification
from and_spec import AndSpecification
from better_filter import BetterFilter

if __name__ == "__main__":
    products = [
        Product("Apple", Color.GREEN, Size.SMALL),
        Product("Tree", Color.GREEN, Size.LARGE),
        Product("House", Color.BLUE, Size.LARGE)
    ]

    bf = BetterFilter()

    print("Blue products:")
    blue = ColorSpecification(Color.BLUE)
    for p in bf.filter(products, blue):
        print(p.name)
    print()

    print("Large products:")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(p.name)
    print()

    print("Large blue products:")
    large_blue = AndSpecification(large, blue)
    for p in bf.filter(products, large_blue):
        print(p.name)