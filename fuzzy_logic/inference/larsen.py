from .rules import Rule
from .antecedent import Antecedent
from ..sets import FSet
from ..sets.functions.func_class import MembershipFunc
from ..sets.defuzzification import centroid_defuzzification, bisection_defuzzification, min_maxium_defuzzification, med_maxium_defuzzification, max_maxium_defuzzification
from ..variables import Variable
from .mamdani import MamdaniMethod


class LarsenRule(Rule):
    def __init__(self, antecedent:Antecedent, con_var:list, con_desc:list):
        super(LarsenRule, self).__init__(antecedent)
        self.con_vars = con_var
        self.con_descs = con_desc

    def eval(self, values:dict):
        result = self.antecedent.eval(values)
        scaled = dict()
        for con_var, con_desc in zip(self.con_vars, self.con_descs):
            to_scale:FSet = con_var.descriptors[con_desc]
            func = MembershipFunc(to_scale.membership.ipoints, lambda x: result * to_scale.membership(x))
            fset = FSet(f'scaled_{to_scale.name}', func, union_method=to_scale.umethod, intersec_method=to_scale.imethod)
            scaled[con_var.name] = fset
        return scaled

class LarsenMethod(MamdaniMethod):
    pass
        