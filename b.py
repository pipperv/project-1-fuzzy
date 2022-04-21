from plant import *
import matplotlib.pyplot as plt

X = range(50)

P_COG_600, TR_COG_600 = compute_plant('COG',600)
P_COG_720, TR_COG_720 = compute_plant('COG',720)
P_COG_850, TR_COG_850 = compute_plant('COG',850)

P_FOM_600, TR_FOM_600 = compute_plant('FOM',600)
P_FOM_720, TR_FOM_720 = compute_plant('FOM',720)
P_FOM_850, TR_FOM_850 = compute_plant('FOM',850)

P_MOM_600, TR_MOM_600 = compute_plant('MOM',600)
P_MOM_720, TR_MOM_720 = compute_plant('MOM',720)
P_MOM_850, TR_MOM_850 = compute_plant('MOM',850)

#Plot de las curvas de P(t) vs t

fig, axs = plt.subplots(3, 3, figsize=(12, 9))

plt.subplots_adjust(left=0.1, 
                    bottom=0.1,  
                    right=0.9,  
                    top=0.9,  
                    wspace=0.4,  
                    hspace=0.4)

fig.subplots_adjust(top=0.9)
fig.suptitle("Evolución de la Presión en distintos casos de Presión inicial y metodo de Des-difusión", fontsize=14)

axs[0][0].plot(X,P_COG_600)
axs[0][0].title.set_text("Centro de Gravedad y P0 = 600")

axs[0][1].plot(X,P_COG_720)
axs[0][1].title.set_text("Centro de Gravedad y P0 = 720")

axs[0][2].plot(X,P_COG_850)
axs[0][2].title.set_text("Centro de Gravedad y P0 = 850")

axs[1][0].plot(X,P_FOM_600)
axs[1][0].title.set_text("Primero de los Maximos y P0 = 600")

axs[1][1].plot(X,P_FOM_720)
axs[1][1].title.set_text("Primero de los Maximos y P0 = 720")

axs[1][2].plot(X,P_FOM_850)
axs[1][2].title.set_text("Primero de los Maximos y P0 = 850")

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