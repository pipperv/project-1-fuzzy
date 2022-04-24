from matplotlib.pyplot import get, plot, plot_date
from d_bonito import plot_trajectory
from cld_utils import remove_rules
from plant import get_rules

method = 'COG'
initial_conditions = [600, 720, 850]

"""
for i in range(17):
    print(f'Rule No {i +1}')
    plot_trajectory(method, initial_conditions, remove_rule=i)

"""
rules = get_rules()
rules = remove_rules(rules, [8])
plot_trajectory(method, initial_conditions, rules=rules)

# reglas que sirve extraer:
# [1, 8, 16, 17]
# la 8 es muy buena
# la 16 no está tan mal