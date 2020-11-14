from ..fuzzy_set import FSet


def centroid_defuzzification(fset:FSet):
    data = fset.get_domain_sample()
    num = 0
    den = 0
    for x in data:
        num += x * fset.membership(x)
        den += fset.membership(x)
    return num/den
