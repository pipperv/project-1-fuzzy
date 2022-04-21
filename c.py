from plant import *
import matplotlib.pyplot as plt
import numpy

X = range(50)

init_p = [600,720,850]
methodes = ['COG','FOM','MOM']

p_data = []
tr_data = []

for p in init_p:
    tmp_p = []
    tmp_tr = []
    for m in methodes:
        x, y = compute_plant(m,p)
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