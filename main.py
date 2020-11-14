from fuzzy_logic.sets import FSet
from fuzzy_logic.inference import IsStatementAntecedent as IsStmnt, MamdaniRule, MamdaniMethod
from fuzzy_logic.variables import Variable
from fuzzy_logic.sets.functions import build_gaussian_function, build_s_function, build_z_function, build_ganma_function, build_l_function, build_pi_function, build_triangular_function
from fuzzy_logic.sets.defuzzification import centroid_defuzzification, bisection_defuzzification, min_maxium_defuzzification, med_maxium_defuzzification, max_maxium_defuzzification

from fuzzy_logic.utils import inputUntil, isFloatIn

service_bad_set = FSet('bad', build_z_function(1, 4))
service_good_set = FSet('good', build_gaussian_function(5, 2))
service_exelent_set = FSet('exelent', build_s_function(6, 9))

food_raw_set = FSet('raw', build_z_function(3, 7))
food_delicious_set = FSet('delicious', build_s_function(5, 9))

tip_poor_set = FSet('poor', build_l_function(4, 10))
tip_average_set = FSet('average', build_triangular_function(8, 15, 18))
tip_generous_set = FSet('rich', build_ganma_function(15, 23))

service_var = Variable('service', service_bad_set, service_good_set, service_exelent_set)
food_var = Variable('food', food_raw_set, food_delicious_set)
tip_var = Variable('tip', tip_poor_set, tip_average_set, tip_generous_set)

# service_var.graph(end_des=1)
# food_var.graph(end_des=1)
# tip_var.graph(end_des=2)

antecedent1 = IsStmnt(service_var, 'bad') | IsStmnt(food_var, 'raw')
rule1 = MamdaniRule(antecedent1, [tip_var], ['poor'])

antecedent2 = IsStmnt(service_var, 'good')
rule2 = MamdaniRule(antecedent2, [tip_var], ['average'])

antecedent3 = IsStmnt(service_var, 'exelent') | IsStmnt(food_var, 'delicious')
rule3 = MamdaniRule(antecedent3, [tip_var], ['rich'])

food_val = float(inputUntil('Input food calification:', lambda x: isFloatIn(x, m=0, M=10)))
service_val = float(inputUntil('Input service calification:', lambda x: isFloatIn(x, m=0, M=10)))

mamdani = MamdaniMethod([rule1, rule2, rule3])
ptip = mamdani.infer({
            'food': food_val,
            'service': service_val,
            })

print(f'Tip: {ptip}')
