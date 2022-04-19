import numpy
import matplotlib.pyplot as plt

from plant import *
from cld_utils import *

N = 50
method = 'MOM'


x_values = numpy.linspace(-1,1,N)
y_values = numpy.linspace(-1,1,N)

X , Y = numpy.meshgrid(x_values, y_values)

rules = get_rules()

Z = []

for x in x_values:
    row = []
    for y in y_values:
        z = FIS(x, y, rules, method)[0]
        row.append(z)
    Z.append(row)

Z = numpy.array(Z)

fig = plt.figure()
ax = plt.axes(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis',vmin=-1,vmax=1)

ax.set_xlabel("EP")
ax.set_ylabel("TP")
ax.view_init(30,120)

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()