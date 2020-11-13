import matplotlib.pyplot as plt

from numpy import arange
from .functions import MembershipFunc


UMAX = max # Union method using max
USUM = lambda x, y: min(x + y, 1) # Union method using limited sum
UPRO = lambda x, y: (x + y) - x * y # Union method using product

IMIN = min # Intersection method using min
ISUB = lambda x, y: max(x + y - 1, 0) # Intersection method using limited substraction
IPRO = lambda x, y: x * y # Intersection method using product

class FSet:
    def __init__(self, name:str, membership:MembershipFunc, union_method=UMAX, intersec_method=IMIN):
        self.name = name
        self.membership = membership
        self.umethod = union_method
        self.imethod = intersec_method

    def __add__(self, other):
        memb = MembershipFunc( self.membership.ipoints + other.membership.ipoints, lambda x: self.umethod(self.membership(x), other.membership(x)))
        return FSet(f'union_({self.name})_({other.name})', memb, union_method=self.umethod, intersec_method=self.imethod)
    
    def __mul__(self, other):        
        memb = MembershipFunc( self.membership.ipoints + other.membership.ipoints, lambda x: self.imethod(self.membership(x), other.membership(x)))
        return FSet(f'inter_({self.name})_({other.name})', memb, union_method=self.umethod, intersec_method=self.imethod)

    def graph(self, end_des=10, step=0.05):
        x_data = list(arange(0, self.membership.ipoints[-1] + end_des, step)) + self.membership.ipoints
        x_data.sort()
        y_data = [ self.membership(x) for x in x_data ]
        plt.title(self.name)
        plt.xlabel('Domain values')
        plt.ylabel('Membership grade')
        plt.plot(x_data, y_data)
        plt.show()
