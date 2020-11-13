from .func_class import MembershipFunc


def build_pi_function(a, b, c, d):
    def pi(x):
        if x <= a:
            return 0
        if a <= x and x <= b:
            return (x-a)/(b-a)
        if b <= x and x <= c:
            return 1
        if c <= x and x <=d:
            return (d-x)/(d-c)
        return 0
    return MembershipFunc([a, b, c, d], pi)
