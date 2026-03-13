from product import Product
from color import Color
from size import Size
from color_spec import  ColorSpecification
from size_spec import SizeSpecification
from better_filter import BetterFilter

if __name__ == "__main__":
    products = [
        Product("Apple", Color.GREEN, Size.SMALL),
        Product("Tree", Color.GREEN, Size.LARGE),
        Product("House", Color.BLUE, Size.LARGE)
    ]

    bf = BetterFilter()

    print("Green products:")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(p.name)
    print()

    print("Large products:")
    # small = SizeSpecification(Size.SMALL)
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(p.name)
    print()

    # print("Large blue products:")
    # for p in pf.filter_by_size_and_color(products, Size.LARGE, Color.BLUE):
    #     print(p.name)