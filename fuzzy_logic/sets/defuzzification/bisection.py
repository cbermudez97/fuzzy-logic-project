from ..fuzzy_set import FSet


def bisection_defuzzification(fset:FSet):
    data = fset.get_domain_sample()
    sums = []
    for x in data:
        try:
            sums.append(fset.membership(x) + sums[-1])
        except IndexError:
            sums.append(fset.membership(x))
    
    for it in range(len(data)):
        if sums[it] >= sums[-1]/2:
            return data[it]
