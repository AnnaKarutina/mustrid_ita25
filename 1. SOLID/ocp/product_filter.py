class ProductFilter:
    def filter_by_color(self, products, color):
        return list(filter(lambda product: product.color == color, products))

    def filter_by_size(self, products, size):
        return list(filter(lambda product: product.size == size, products))

    def filter_by_size_and_color(self, products, size, color):
        return list(filter(lambda product: (product.size == size and product.color == color), products))