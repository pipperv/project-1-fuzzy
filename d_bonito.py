import numpy
from plant import *

# Plots the trajectory followed by the plant in the plane EPxTP
def plot_trajectory(method: str, initial_conditions: list, N=50, rules=None) -> None:
    x_values = numpy.linspace(-1,1,N)
    y_values = numpy.linspace(-1,1,N)

    X , Y = numpy.meshgrid(x_values, y_values)

    if not rules:
        rules = get_rules()

    Z = []

    for x in x_values:
        row = []
        for y in y_values:
            z = FIS(x, y, rules, method)[0]
            row.append(z)
        Z.append(row)

    Z = numpy.array(Z)

    fig = plt.figure(figsize=plt.figaspect(0.5))
    for idx, initial_condition in enumerate(initial_conditions):
        P, TR, EP, TP, controller_values  = compute_plant(method, initial_condition, get_EP_TP=True, rules=rules)
        ax = fig.add_subplot(1, 3, idx + 1)
        ax.pcolor(X,Y,Z)
        ax.plot(EP, TP, 'k')
        ax.set_xlabel("EP")
        ax.set_ylabel("TP")
        ax.set_title(f'Trayectoria seguida por la planta con \n desdifusión {method} y \n condición inicial {initial_condition}')
    
    plt.show()

if __name__ == '__main__':
    methods = ['COG', 'FOM', 'MOM']
    initial_conditions = [600, 720, 850]

    for method in methods:
        plot_trajectory(method, initial_conditions)