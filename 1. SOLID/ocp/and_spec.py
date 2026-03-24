from specification import Specification

class AndSpecification(Specification):

    # def __init__(self, spec1, spec2):
    #     self.spec1 = spec1
    #     self.spec2 = spec2
    #
    # def is_satisfied(self, product):
    #     return self.spec1.is_satisfied(product) and self.spec2.is_satisfied(product)

    def __init__(self, *specs):
        self.specs = specs

    # def is_satisfied(self, product):
    #     for spec in self.specs:
    #         if not spec.is_satisfied(product):
    #             return False
    #     return True

    def is_satisfied(self, product):
        return all(map(lambda spec: spec.is_satisfied(product), self.specs))
