from .defuzzy_model import Defuzzy_Model, Defuzzy_Rule
from .antecedent import Antecedent
from ..sets import FSet
from ..sets.functions.func_class import MembershipFunc
from ..sets.defuzzification import centroid_defuzzification, bisection_defuzzification, min_maxium_defuzzification, med_maxium_defuzzification, max_maxium_defuzzification
from ..variables import Variable
from .mamdani import MamdaniMethod


class LarsenRule(Defuzzy_Rule):
    def merge(self, value, to_scale:FSet):
        func = MembershipFunc(to_scale.membership.ipoints, lambda x: value * to_scale.membership(x))
        return FSet(f'scaled_{to_scale.name}', func, union_method=to_scale.umethod, intersec_method=to_scale.imethod)

class LarsenMethod(Defuzzy_Model):
    pass
        