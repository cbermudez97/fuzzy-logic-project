from .func_class import MembershipFunc


def build_ganma_function(a, m):
    def ganma(x):
        if x <= a:
            return 0
        if a <= x and x <= m:
            return (x-a)/(m-a)
        return 1
    return MembershipFunc([a, m], ganma)
