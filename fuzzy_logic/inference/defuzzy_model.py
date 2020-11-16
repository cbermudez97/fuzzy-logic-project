from .rules import Rule
from .antecedent import Antecedent
from ..sets import FSet
from ..sets.functions.func_class import MembershipFunc
from ..sets.defuzzification import centroid_defuzzification, bisection_defuzzification, min_maxium_defuzzification, med_maxium_defuzzification, max_maxium_defuzzification
from ..variables import Variable


class Defuzzy_Rule(Rule):
    def __init__(self, antecedent:Antecedent, con_var:list, con_desc:list):
        super(Defuzzy_Rule, self).__init__(antecedent)
        self.con_vars = con_var
        self.con_descs = con_desc

    def merge(self, value, fset1:FSet):
        raise NotImplementedError()

    def eval(self, values:dict):
        result = self.antecedent.eval(values)
        transformed = dict()
        for con_var, con_desc in zip(self.con_vars, self.con_descs):
            to_trans:FSet = con_var.descriptors[con_desc]
            fset = self.merge(result, to_trans)
            transformed[con_var.name] = fset
        return transformed

class Defuzzy_Model:
    def __init__(self, rules:list):
        self.rules = rules

    def infer(self, input_values:dict, def_method=centroid_defuzzification):
        final = self.rules[0].eval(input_values)
        for rule in self.rules[1:]:
            update = rule.eval(input_values)
            for var_name in update:
                final[var_name] = final[var_name] + update[var_name]
        
        for var_name in final:
            final[var_name] = def_method(final[var_name])

        return final
        