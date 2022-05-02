from plant import *
from cld_utils import *
import matplotlib.pyplot as plt
from o_a import plot_realistic_trajectory

X = range(50)


rules = get_rules()
dict_sets = get_dict_sets()
# Modificar la regla 3 (reducir el sobrepaso)
#rules[2][2] = dict_sets["pi"]
# Modificar la regla 10 (mejorar el tiempo de establecimiento)
#rules[9][2] = dict_sets["ng"]
#rules[8][2] = dict_sets["ng"]
#rules[7][2] = dict_sets["ng"]  

# Mejorar la oscilaciones
rules[8][2] = dict_sets["ni"]
rules[9][2] = dict_sets["ni"]
rules[11][2] = dict_sets["ni"]
rules[0][2] = dict_sets["pm"]

removed_rules = [2, 3, 4, 7, 16]
rules = remove_rules(rules, removed_rules)
# Convergencia de el metodo alturas

#rules[11][2] = dict_sets["ng"]
#rules[13][2] = dict_sets["pg"]


P_COG_600, H, TR_COG_600 = compute_realistic_plant('COG',600,rules=rules)
P_COG_720, H, TR_COG_720 = compute_realistic_plant('COG',720,rules=rules)
P_COG_850, H,TR_COG_850 = compute_realistic_plant('COG',850,rules=rules)

P_FOM_600, H, TR_FOM_600 = compute_realistic_plant('Heights',600,rules=rules)
P_FOM_720, H, TR_FOM_720 = compute_realistic_plant('Heights',720,rules=rules)
P_FOM_850, H, TR_FOM_850 = compute_realistic_plant('Heights',850,rules=rules)

P_MOM_600, H, TR_MOM_600 = compute_realistic_plant('MOM',600,rules=rules)
P_MOM_720, H, TR_MOM_720 = compute_realistic_plant('MOM',720,rules=rules)
P_MOM_850, H, TR_MOM_850 = compute_realistic_plant('MOM',850,rules=rules)

#Plot de las curvas de P(t) vs t

fig, axs = plt.subplots(3, 3, figsize=(12, 9))

plt.subplots_adjust(left=0.1, 
                    bottom=0.1,  
                    right=0.9,  
                    top=0.9,  
                    wspace=0.4,  
                    hspace=0.4)

fig.subplots_adjust(top=0.9)
fig.suptitle(f"Evolución de la Presión realizando las modificaciones en las reglas", fontsize=14)

axs[0][0].plot(X,P_COG_600)
axs[0][0].title.set_text("Centro de Gravedad y P0 = 600")

axs[0][1].plot(X,P_COG_720)
axs[0][1].title.set_text("Centro de Gravedad y P0 = 720")

axs[0][2].plot(X,P_COG_850)
axs[0][2].title.set_text("Centro de Gravedad y P0 = 850")

axs[1][0].plot(X,P_FOM_600)
axs[1][0].title.set_text("Alturas y P0 = 600")

axs[1][1].plot(X,P_FOM_720)
axs[1][1].title.set_text("Alturas y P0 = 720")

axs[1][2].plot(X,P_FOM_850)
axs[1][2].title.set_text("Alturas y P0 = 850")

axs[2][0].plot(X,P_MOM_600)
axs[2][0].title.set_text("Promedio de los Maximos y P0 = 600")

axs[2][1].plot(X,P_MOM_720)
axs[2][1].title.set_text("Promedio de los Maximos y P0 = 720")

axs[2][2].plot(X,P_MOM_850)
axs[2][2].title.set_text("Promedio de los Maximos y P0 = 850")

#Config for all plots:
for i in range(3):
    for j in range(3):
        axs[i][j].set_xlabel("t")
        axs[i][j].set_ylabel("P(t)")
        axs[i][j].grid()

plt.show()


X = range(50)

init_p = [600,720,850]
methodes = ['COG','Heights','MOM']


p_data = []
tr_data = []

for m in methodes:
    tmp_p = []
    tmp_tr = []
    for p in init_p:
        x, y = compute_plant(m,p,rules=rules)
        tmp_p.append(x)
        tmp_tr.append(y)
    p_data.append(tmp_p)
    tr_data.append(tmp_tr)

fig, axs = plt.subplots(3, 3, figsize=(12, 12))

plt.subplots_adjust(left=0.1, 
                    bottom=0.1,  
                    right=0.9,  
                    top=0.9,  
                    wspace=0.4,  
                    hspace=0.4)

fig.subplots_adjust(top=0.9)
fig.suptitle("Reglas Disparadas en distintos casos de Presión inicial y metodo de Des-difusión", fontsize=14)

for i, A in enumerate(tr_data):
    for j, B in enumerate(A):
        for n, tr in enumerate(B):
            p = init_p[j]
            m = methodes[i]
            rgba_colors = numpy.zeros((len(tr[0]),4))
            rgba_colors[:,0] = 1.0
            rgba_colors[:,3] = tr[1]
            axs[i][j].grid()
            axs[i][j].scatter(numpy.ones_like(tr[0])*n,tr[0],color=rgba_colors)
            axs[i][j].set_xlabel("t")
            axs[i][j].set_ylabel("Rule Triggered")
            axs[i][j].title.set_text(f"Reglas disparadas ({m} , {p})")
                
plt.show()

methods = ['COG', 'Heights', 'MOM']
initial_conditions = [600, 720, 850]

for method in methods:
    plot_realistic_trajectory(method, initial_conditions, rules=rules)