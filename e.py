from matplotlib.pyplot import plot, plot_date
from d_bonito import plot_trajectory


method = 'COG'
initial_conditions = [600, 720, 850]

for i in range(17):
    print(f'Rule No {i +1}')
    plot_trajectory(method, initial_conditions, remove_rule=i)

# reglas que sirve remover:
# 5