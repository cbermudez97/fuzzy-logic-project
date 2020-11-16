from fuzzy_logic.sets import FSet
from fuzzy_logic.inference import IsStatementAntecedent as IsStmnt, MamdaniRule, MamdaniMethod, LarsenRule, LarsenMethod
from fuzzy_logic.variables import Variable
from fuzzy_logic.sets.functions import build_gaussian_function, build_s_function, build_z_function, build_ganma_function, build_l_function, build_pi_function, build_triangular_function
from fuzzy_logic.sets.defuzzification import centroid_defuzzification, bisection_defuzzification, min_maxium_defuzzification, med_maxium_defuzzification, max_maxium_defuzzification

from fuzzy_logic.utils import inputUntil, isFloatIn

# Temperature variable measured in Farenheits
temperature_cold_set = FSet('cold', build_l_function(32, 43))
temperature_cool_set = FSet('cool', build_triangular_function(38, 55, 67))
temperature_hot_set = FSet('hot', build_ganma_function(64, 77))
temperature_var = Variable('temperature', temperature_cold_set, temperature_cool_set, temperature_hot_set)

# Pressure variable measured in hPa
pressure_low_set = FSet('low', build_l_function(980, 1015))
pressure_high_set = FSet('high', build_ganma_function(995, 1040))
pressure_var = Variable('pressure', pressure_low_set, pressure_high_set)

# Humidity variable, this is the percent of water in the air from the total it can hold in that moment
humidity_low_set = FSet('low', build_l_function(40, 60))
humidity_average_set = FSet('average', build_triangular_function(55, 70, 85))
humidity_high_set = FSet('high', build_ganma_function(80, 95))
humidity_var = Variable('humidity', humidity_low_set, humidity_average_set, humidity_high_set)

# Sea Level variable measured in meters(m), this refers to the actual difference of the average sea level with the actual sea level in that moment
sea_level_normal_set = FSet('normal', build_l_function(0, 1.5))
sea_level_medium_set = FSet('medium', build_triangular_function(1, 1.9, 2.5))
sea_level_high_set = FSet('high', build_ganma_function(2.3, 3))
sea_level_var = Variable('sea_level', sea_level_normal_set, sea_level_medium_set, sea_level_high_set)

# Flood Control Dam operation variable, this value does not have a real signification it only gives a quantifier to the operation to use
operation_open_set = FSet('open', build_l_function(0, 1))
operation_close_set = FSet('close', build_ganma_function(1, 2))
operation_var = Variable('operation', operation_open_set, operation_close_set)

# temperature_var.graph()
# pressure_var.graph()
# humidity_var.graph()
# sea_level_var.graph()
# operation_var.graph()

antecedent1 = IsStmnt(sea_level_var, 'normal')
mrule1 = MamdaniRule(antecedent1, [operation_var], ['open'])
lrule1 = LarsenRule(antecedent1, [operation_var], ['open'])

antecedent2 = IsStmnt(sea_level_var, 'high')
mrule2 = MamdaniRule(antecedent2, [operation_var], ['close'])
lrule2 = LarsenRule(antecedent2, [operation_var], ['close'])

antecedent3 = IsStmnt(humidity_var, 'high') & IsStmnt(temperature_var, 'hot') & IsStmnt(pressure_var, 'low') 
mrule3 = MamdaniRule(antecedent3, [operation_var], ['close'])
lrule3 = LarsenRule(antecedent3, [operation_var], ['close'])

antecedent4 = (IsStmnt(humidity_var, 'average') | IsStmnt(humidity_var, 'low')) & IsStmnt(temperature_var, 'hot') & IsStmnt(pressure_var, 'low') & IsStmnt(sea_level_var, 'normal')
mrule4 = MamdaniRule(antecedent4, [operation_var], ['open'])
lrule4 = LarsenRule(antecedent4, [operation_var], ['open'])

antecedent5 = (IsStmnt(temperature_var, 'hot') | IsStmnt(pressure_var, 'high') | IsStmnt(humidity_var, 'average')) & IsStmnt(sea_level_var, 'medium')
mrule5 = MamdaniRule(antecedent5, [operation_var], ['open'])
lrule5 = LarsenRule(antecedent5, [operation_var], ['open'])

temperature_val = float(inputUntil('Input temperature value (F):', lambda x: isFloatIn(x, m=0, M=100)))
pressure_val = float(inputUntil('Input pressure value (hPa):', lambda x: isFloatIn(x, m=800, M=1100)))
humidity_val = float(inputUntil('Input humidity percent (%100):', lambda x: isFloatIn(x, m=0, M=100)))
sea_level_val = float(inputUntil('Input sea level difference (m):', lambda x: isFloatIn(x, m=0, M=5)))

mamdani = MamdaniMethod([mrule1, mrule2, mrule3, mrule4, mrule5])
larsen = LarsenMethod([lrule1, lrule2, lrule3, lrule4, lrule5])

m_op = mamdani.infer({
            'temperature': temperature_val,
            'pressure': pressure_val,
            'humidity': humidity_val,
            'sea_level': sea_level_val,
            })['operation']

l_op = larsen.infer({
            'temperature': temperature_val,
            'pressure': pressure_val,
            'humidity': humidity_val,
            'sea_level': sea_level_val,
            })['operation']

print(f'The dam will { "open" if m_op < 1 else "close"}.(using Mamdani)')
print(f'The dam will { "open" if l_op < 1 else "close"}.(using Larsen)')
