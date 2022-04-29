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
removed_rules = [3,4,5,6,7,8,9,12,13,14,15,16,17]
rules = get_rules()
rules = remove_rules(rules, removed_rules)

methods = ['COG', 'Heights', 'MOM']
initial_conditions = [600, 720, 850]

for method in methods:
    plot_trajectory(method, initial_conditions, rules=rules)

# reglas que sirve extraer:
# [8, 16, 17]
# la 8 es muy buena
# la 16 no está tan mal