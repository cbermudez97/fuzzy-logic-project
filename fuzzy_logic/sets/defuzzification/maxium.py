from ..fuzzy_set import FSet


def min_maxium_defuzzification(fset:FSet):
    data = fset.get_domain_sample()
    result = 0
    result_val = -1 
    for x in data:
        if result_val < fset.membership(x):
            result = x
            result_val = fset.membership(x)
    return result

def max_maxium_defuzzification(fset:FSet):
    data = fset.get_domain_sample()
    result = 0
    result_val = -1 
    for x in data:
        if result_val <= fset.membership(x):
            result = x
            result_val = fset.membership(x)
    return result

def med_maxium_defuzzification(fset:FSet):
    min_max = min_maxium_defuzzification(fset)
    max_max = max_maxium_defuzzification(fset)
    return (min_max + max_max)/2