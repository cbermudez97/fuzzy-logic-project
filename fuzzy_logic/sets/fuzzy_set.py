import matplotlib.pyplot as plt


UMAX = max # Union method using max
USUM = lambda x, y: min(x + y, 1) # Union method using limited sum
UPRO = lambda x, y: (x + y) - x * y # Union method using product

IMIN = min # Intersection method using min
ISUB = lambda x, y: max(x + y - 1, 0) # Intersection method using limited substraction
IPRO = lambda x, y: x * y # Intersection method using product

class FSet:
    def __init__(self, name:str,membership:dict, union_method=UMAX, intersec_method=IMIN):
        self.name = name
        self.membership = membership
        self.umethod = union_method
        self.imethod = intersec_method

    def __add__(self, other):
        union_memb = dict()
        for x in self.membership.keys():
            if not x in other.membership.keys():
                raise ValueError('Domains sets must be identical.')
            union_memb[x] = self.umethod(self.membership[x], other.membership[x])
        return FSet(f'union_({self.name})_({other.name})', union_memb, union_method=self.umethod, intersec_method=self.imethod)
    
    def __mul__(self, other):
        int_memb = dict()
        for x in self.membership.keys():
            if not x in other.membership.keys():
                raise ValueError('Domains sets must be identical.')
            int_memb[x] = self.imethod(self.membership[x], other.membership[x])
        return FSet(f'inter_({self.name})_({other.name})', int_memb, union_method=self.umethod, intersec_method=self.imethod)

    def graph_data(self):
        data = list(self.membership.items())
        data.sort()
        x_data = []
        y_data = []
        for x, y in data:
            x_data.append(x)
            y_data.append(y)
        return x_data, y_data

    def graph(self):
        x_data, y_data = self.graph_data()
        plt.title(self.name)
        plt.xlabel('Domain values')
        plt.ylabel('Membership values')
        plt.plot(x_data, y_data)
        plt.show()
