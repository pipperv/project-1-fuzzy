import numpy
from plant import *

# Plots the trajectory followed by the plant in the plane EPxTP
def plot_realistic_trajectory(method: str, initial_conditions: list, N=50, rules=None) -> None:
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
        P, H, TR, EP, TP, controller_values  = compute_realistic_plant(method, initial_condition, 700,  get_EP_TP=True, rules=rules)
        ax = fig.add_subplot(1, 3, idx + 1)
        ax.pcolor(X,Y,Z)
        ax.plot(EP, TP, 'k')
        ax.set_xlabel("EP")
        ax.set_ylabel("TP")
        ax.set_title(f'Trayectoria seguida por la planta con \n desdifusión {method} y \n condición inicial {initial_condition}')
    
    plt.show()

    fig = plt.figure()
    
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(H)
    ax.set_xlabel("T")
    ax.set_ylabel("H")
    ax.set_title(f'Evolución de H con desdifusión {method} y \n condición inicial {initial_condition}')

    plt.show()






methods = ['COG', 'Heights', 'MOM']
initial_conditions = [600, 720, 850]


for method in methods:
    plot_realistic_trajectory(method, initial_conditions)