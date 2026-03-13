class BetterFilter:
    def filter(self, products, spec):
        return list(filter(lambda product: spec.is_satisfied(product), products))
