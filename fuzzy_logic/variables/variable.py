import matplotlib.pyplot as plt

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

    def graph(self, end_des=5, step=0.05):
        plots = []
        for it, desc in enumerate(self.descriptors.values()):
            x_data = desc.get_domain_sample(end_des=end_des, step=step)
            y_data = [ desc.membership(x) for x in x_data ]
            plots.append(plt.plot(x_data, y_data, f'C{it+1}', label=desc.name))
        plt.legend()
        plt.title(self.name)
        plt.show()
