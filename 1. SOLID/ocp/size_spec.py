from specification import Specification

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, product):
        return self.size == product.size
