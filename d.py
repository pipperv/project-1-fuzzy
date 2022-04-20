import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from plant import *
from cld_utils import *

N = 50
x_values = numpy.linspace(-1,1,N)
y_values = numpy.linspace(-1,1,N)

X , Y = numpy.meshgrid(x_values, y_values)

rules = get_rules()




Z = []

for x in x_values:
    row = []
    for y in y_values:
        z = FIS(x, y, rules, 'COG')[0]
        row.append(z)
    Z.append(row)

Z = numpy.array(Z)

fig = plt.figure(figsize=plt.figaspect(0.5))

P_COG_600, TR_COG_600, EP_list_COG_600, TP_list_COG_600, values_COG_600  = compute_plant('COG',600, get_EP_TP=True)
ax = fig.add_subplot(1, 3, 1, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis',vmin=-1,vmax=1, alpha= 0.5)
ax.plot(EP_list_COG_600, TP_list_COG_600, values_COG_600, 'k')
ax.set_xlabel("EP")
ax.set_ylabel("TP")
ax.view_init(30,120)


P_COG_720, TR_COG_720, EP_list_COG_720, TP_list_COG_720, values_COG_720  = compute_plant('COG',720, get_EP_TP=True)
ax = fig.add_subplot(1, 3, 2, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis',vmin=-1,vmax=1, alpha= 0.5)
ax.plot(EP_list_COG_720, TP_list_COG_720, values_COG_720, 'k')
ax.set_xlabel("EP")
ax.set_ylabel("TP")
ax.view_init(30,120)


P_COG_850, TR_COG_850, EP_list_COG_850, TP_list_COG_850, values_COG_850  = compute_plant('COG',850, get_EP_TP=True)
ax = fig.add_subplot(1, 3, 3, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis',vmin=-1,vmax=1, alpha= 0.5)
ax.plot(EP_list_COG_850, TP_list_COG_850, values_COG_850, 'k')
ax.set_xlabel("EP")
ax.set_ylabel("TP")
ax.view_init(30,120)

plt.show()


Z = []

for x in x_values:
    row = []
    for y in y_values:
        z = FIS(x, y, rules, 'FOM')[0]
        row.append(z)
    Z.append(row)

Z = numpy.array(Z)

fig = plt.figure(figsize=plt.figaspect(0.5))

P_FOM_600, TR_FOM_600, EP_list_FOM_600, TP_list_FOM_600, values_FOM_600  = compute_plant('FOM',600, get_EP_TP=True)
ax = fig.add_subplot(1, 3, 1, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis',vmin=-1,vmax=1, alpha= 0.5)
ax.plot(EP_list_FOM_600, TP_list_FOM_600, values_FOM_600, 'k')
ax.set_xlabel("EP")
ax.set_ylabel("TP")
ax.view_init(30,120)

P_FOM_720, TR_FOM_720, EP_list_FOM_720, TP_list_FOM_720, values_FOM_720  = compute_plant('FOM',720, get_EP_TP=True)
ax = fig.add_subplot(1, 3, 2, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis',vmin=-1,vmax=1, alpha= 0.5)
ax.plot(EP_list_FOM_720, TP_list_FOM_720, values_FOM_720, 'k')
ax.set_xlabel("EP")
ax.set_ylabel("TP")
ax.view_init(30,120)

P_FOM_850, TR_FOM_850, EP_list_FOM_850, TP_list_FOM_850, values_FOM_850  = compute_plant('FOM',850, get_EP_TP=True)
ax = fig.add_subplot(1, 3, 3, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis',vmin=-1,vmax=1, alpha= 0.5)
ax.plot(EP_list_FOM_850, TP_list_FOM_850, values_FOM_850, 'k')
ax.set_xlabel("EP")
ax.set_ylabel("TP")
ax.view_init(30,120)

plt.show()



Z = []

for x in x_values:
    row = []
    for y in y_values:
        z = FIS(x, y, rules, 'MOM')[0]
        row.append(z)
    Z.append(row)

Z = numpy.array(Z)


fig = plt.figure(figsize=plt.figaspect(0.5))

P_MOM_600, TR_MOM_600, EP_list_MOM_600, TP_list_MOM_600, values_MOM_600  = compute_plant('MOM',600, get_EP_TP=True)
ax = fig.add_subplot(1, 3, 1, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis',vmin=-1,vmax=1, alpha= 0.5)
ax.plot(EP_list_MOM_600, TP_list_MOM_600, values_MOM_600, 'k')
ax.set_xlabel("EP")
ax.set_ylabel("TP")
ax.view_init(30,120)

P_MOM_720, TR_MOM_720, EP_list_MOM_720, TP_list_MOM_720, values_MOM_720  = compute_plant('MOM',720, get_EP_TP=True)
ax = fig.add_subplot(1, 3, 2, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis',vmin=-1,vmax=1, alpha= 0.5)
ax.plot(EP_list_MOM_720, TP_list_MOM_720, values_MOM_720, 'k')
ax.set_xlabel("EP")
ax.set_ylabel("TP")
ax.view_init(30,120)

P_MOM_850, TR_MOM_850, EP_list_MOM_850, TP_list_MOM_850, values_MOM_850  = compute_plant('MOM',850, get_EP_TP=True)
ax = fig.add_subplot(1, 3, 3, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis',vmin=-1,vmax=1, alpha= 0.5)
ax.plot(EP_list_MOM_850, TP_list_MOM_850, values_MOM_850, 'k')
ax.set_xlabel("EP")
ax.set_ylabel("TP")
ax.view_init(30,120)

plt.show()



