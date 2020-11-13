from .func_class import MembershipFunc
from .s_function import build_s_function
from .z_function import build_z_function


def build_gaussian_function(b, d):
    def gaussian(x):
        s = build_s_function(b-d, b)
        z = build_z_function(b, b+d)
        if x <= b:
            return s(x)
        return z(x)
    return MembershipFunc([b-d, b, b+d], gaussian)
