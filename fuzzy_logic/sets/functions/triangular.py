from .func_class import MembershipFunc


def build_triangular_function(a, m, b):
    def triangular(x):
        if x <= a:
            return 0
        if a <= x and x <= m:
            return (x-a)/(m-a)
        if m <= x and x <=b:
            return (b-x)/(b-m)
        return 0
    return MembershipFunc([a, m, b], triangular)
