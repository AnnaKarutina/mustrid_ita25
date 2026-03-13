from product import Product
from color import Color
from size import Size
from product_filter import ProductFilter

if __name__ == "__main__":
    products = [
        Product("Apple", Color.GREEN, Size.SMALL),
        Product("Tree", Color.GREEN, Size.LARGE),
        Product("House", Color.BLUE, Size.LARGE)
    ]

    pf = ProductFilter()

    print("Green products:")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(p.name)
    print()

    print("Small products:")
    for p in pf.filter_by_size(products, Size.SMALL):
        print(p.name)
    print()

    print("Large blue products:")
    for p in pf.filter_by_size_and_color(products, Size.LARGE, Color.BLUE):
        print(p.name)