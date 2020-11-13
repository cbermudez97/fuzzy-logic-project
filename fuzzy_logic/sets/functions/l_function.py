from .func_class import MembershipFunc


def build_l_function(a, m):
    def l(x):
        if x <= a:
            return 1
        if a <= x and x <= m:
            return (m-x)/(m-a)
        return 0
    return MembershipFunc([a, m], l)