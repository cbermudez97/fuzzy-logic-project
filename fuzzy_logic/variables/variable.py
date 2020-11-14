from ..sets import FSet


class Variable:
    def __init__(self, name, *args):
        assert all([ isinstance(fset, FSet) for fset in args ]), 'All sets should be valid ones.'
        self.name = name
        self.descriptors = dict()
        for fset in args:
            self.descriptors[fset.name] = fset

    def fuzzify(self, x, dname):
        return self.descriptors[dname].membership(x)
