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

fig, axs = plt.subplots(3, 3, figsize=(12, 12))

axs[0][0].title.set_text("Reglas disparadas (COG , P0=600)")
for i, tr in enumerate(TR_COG_600):
    for r, h in zip(tr[0],tr[1]):
        axs[0][0].plot(i,r,marker='o',color=(0,0,1,h))
        axs[0][0].grid()

axs[0][1].title.set_text("Reglas disparadas (COG , P0=720)")
for i, tr in enumerate(TR_COG_720):
    for r, h in zip(tr[0],tr[1]):
        axs[0][1].plot(i,r,marker='o',color=(0,0,1,h))
        axs[0][1].grid()

axs[0][2].title.set_text("Reglas disparadas (COG , P0=850)")
for i, tr in enumerate(TR_COG_850):
    for r, h in zip(tr[0],tr[1]):
        axs[0][2].plot(i,r,marker='o',color=(0,0,1,h))
        axs[0][2].grid()

axs[1][0].title.set_text("Reglas disparadas (FOM , P0=600)")
for i, tr in enumerate(TR_FOM_600):
    for r, h in zip(tr[0],tr[1]):
        axs[1][0].plot(i,r,marker='o',color=(0,0,1,h))
        axs[1][0].grid()

axs[1][1].title.set_text("Reglas disparadas (FOM , P0=720)")
for i, tr in enumerate(TR_FOM_720):
    for r, h in zip(tr[0],tr[1]):
        axs[1][1].plot(i,r,marker='o',color=(0,0,1,h))
        axs[1][1].grid()

axs[1][2].title.set_text("Reglas disparadas (FOM , P0=850)")
for i, tr in enumerate(TR_FOM_850):
    for r, h in zip(tr[0],tr[1]):
        axs[1][2].plot(i,r,marker='o',color=(0,0,1,h))
        axs[1][2].grid()

axs[2][0].title.set_text("Reglas disparadas (MOM , P0=600)")
for i, tr in enumerate(TR_MOM_600):
    for r, h in zip(tr[0],tr[1]):
        axs[2][0].plot(i,r,marker='o',color=(0,0,1,h))
        axs[2][0].grid()

axs[2][1].title.set_text("Reglas disparadas (MOM , P0=720)")
for i, tr in enumerate(TR_MOM_720):
    for r, h in zip(tr[0],tr[1]):
        axs[2][1].plot(i,r,marker='o',color=(0,0,1,h))
        axs[2][1].grid()

axs[2][2].title.set_text("Reglas disparadas (MOM , P0=850)")
for i, tr in enumerate(TR_MOM_850):
    for r, h in zip(tr[0],tr[1]):
        axs[2][2].plot(i,r,marker='o',color=(0,0,1,h))
        axs[2][2].grid()

plt.show()