from o_a import plot_realistic_trajectory
import matplotlib.pyplot as plt
from cld_utils import remove_rules
from plant import get_rules, compute_realistic_plant



removed_rules = [2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 15, 16]
rules = get_rules()
rules = remove_rules(rules, removed_rules)

methods = ['COG', 'Heights', 'MOM']
initial_conditions = [600, 720, 850]

for method in methods:
    plot_realistic_trajectory(method, initial_conditions, rules=rules)


probar = False
if probar:
    for i in range(1, 18):
        
        X = range(50)

        string_rules = ' '.join([str(item) for item in removed_rules])

        P_COG_600,H , TR_COG_600 = compute_realistic_plant('COG',600,rules=rules)
        P_COG_720,H , TR_COG_720 = compute_realistic_plant('COG',720,rules=rules)
        P_COG_850,H , TR_COG_850 = compute_realistic_plant('COG',850,rules=rules)

        P_FOM_600,H , TR_FOM_600 = compute_realistic_plant('Heights',600,rules=rules)
        P_FOM_720,H , TR_FOM_720 = compute_realistic_plant('Heights',720,rules=rules)
        P_FOM_850,H , TR_FOM_850 = compute_realistic_plant('Heights',850,rules=rules)

        P_MOM_600,H , TR_MOM_600 = compute_realistic_plant('MOM',600,rules=rules)
        P_MOM_720,H , TR_MOM_720 = compute_realistic_plant('MOM',720,rules=rules)
        P_MOM_850,H , TR_MOM_850 = compute_realistic_plant('MOM',850,rules=rules)

        #Plot de las curvas de P(t) vs t

        fig, axs = plt.subplots(3, 3, figsize=(12, 9))

        plt.subplots_adjust(left=0.1, 
                            bottom=0.1,  
                            right=0.9,  
                            top=0.9,  
                            wspace=0.4,  
                            hspace=0.4)

        fig.subplots_adjust(top=0.9)
        fig.suptitle(f"Evolución de la Presión sin reglas {removed_rules}", fontsize=14)

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
else:
    X = range(50)


    string_rules = ' '.join([str(item) for item in removed_rules])

    P_COG_600,H , TR_COG_600 = compute_realistic_plant('COG',600,rules=rules)
    P_COG_720,H , TR_COG_720 = compute_realistic_plant('COG',720,rules=rules)
    P_COG_850,H , TR_COG_850 = compute_realistic_plant('COG',850,rules=rules)

    P_FOM_600,H , TR_FOM_600 = compute_realistic_plant('Heights',600,rules=rules)
    P_FOM_720,H , TR_FOM_720 = compute_realistic_plant('Heights',720,rules=rules)
    P_FOM_850,H , TR_FOM_850 = compute_realistic_plant('Heights',850,rules=rules)

    P_MOM_600,H , TR_MOM_600 = compute_realistic_plant('MOM',600,rules=rules)
    P_MOM_720,H , TR_MOM_720 = compute_realistic_plant('MOM',720,rules=rules)
    P_MOM_850,H , TR_MOM_850 = compute_realistic_plant('MOM',850,rules=rules)

    #Plot de las curvas de P(t) vs t

    fig, axs = plt.subplots(3, 3, figsize=(12, 9))

    plt.subplots_adjust(left=0.1, 
                        bottom=0.1,  
                        right=0.9,  
                        top=0.9,  
                        wspace=0.4,  
                        hspace=0.4)

    fig.subplots_adjust(top=0.9)
    fig.suptitle(f"Evolución de la Presión sin reglas {removed_rules}", fontsize=14)

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


    #La 7 esta casi
    # 1, 7, 16 es casi la combinacion
    # 4, 7, 16 es casi la combinacion
    # 5, 7, 16 tambien esta buena
    # 2, 4, 7, 16 es "buena"
    # 3, 4, 7, 16
    # 2, 3, 4, 7, 16 no llega exactamente a 0, pero mejora la respuesta dinamica
    # 2, 3, 4, 16 tiene el mismo efecto