from .func_class import MembershipFunc


def build_s_function(a, c):
    def s(x):
        if x <= a:
            return 0
        if a <= x and x <= (a+c)/2:
            return 2*((x-a)/(c-a))**2
        if (a+c)/2 <= x and x < c:
            return 1 - 2*((c-x)/(c-a))**2
        return 1
    return MembershipFunc([a, (a+c)/2, c], s)
