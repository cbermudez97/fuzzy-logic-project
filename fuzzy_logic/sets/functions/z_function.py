from .func_class import MembershipFunc


def build_z_function(a, c):
    def z(x):
        if x <= a:
            return 1
        if a < x and x <= (a+c)/2:
            return 1 - 2*((x-a)/(c-a))**2
        if (a+c)/2 < x and x < c:
            return 2*((c-x)/(c-a))**2
        return 0
    return MembershipFunc([a, (a+c)/2, c], z)
