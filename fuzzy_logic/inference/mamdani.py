from .rules import Rule
from .defuzzy_model import Defuzzy_Model, Defuzzy_Rule
from .antecedent import Antecedent
from ..sets import FSet
from ..sets.functions.func_class import MembershipFunc
from ..sets.defuzzification import centroid_defuzzification, bisection_defuzzification, min_maxium_defuzzification, med_maxium_defuzzification, max_maxium_defuzzification
from ..variables import Variable


class MamdaniRule(Defuzzy_Rule):
    def merge(self, value, to_cut:FSet):
        func = MembershipFunc(to_cut.membership.ipoints, lambda x: min(value, to_cut.membership(x)))
        return FSet(f'cuted_{to_cut.name}', func, union_method=to_cut.umethod, intersec_method=to_cut.imethod)

class MamdaniMethod(Defuzzy_Model):
    pass
        