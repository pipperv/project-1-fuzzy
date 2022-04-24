from hashlib import new
import numpy
import matplotlib.pyplot as plt

#Funciones para trabajar Conjuntos Difusos:

def memb_grade(a, X):
    # Da como resultado el grado de membresia del valor "a"
    # en el conjunto difuso "X"
    if a < X[0] or a > X[3]: return 0
    elif a >= X[0] and a < X[1]: return (a-X[0])/(X[1]-X[0])
    elif a >=X[1] and a <= X[2]: return 1
    elif a >X[2] and a <= X[3]: return (X[3]-a)/(X[3]-X[2])

def de_a(A,B):
    # Da como resultado el conjunto difuso de "A" a "B"
    if A[0]<B[0]: a = A[0]
    else: a = B[0]
    if A[1]<B[1]: b = A[1]
    else: b = B[1]
    if A[2]<B[2]: c = B[2]
    else: c = A[2]
    if A[3]<B[3]: d = B[3]
    else: d = A[3]
    return [a,b,c,d]

#Mapa de Reglas

def rule_map(rules):
    vert = [0,0,1,1,0,0]
    fig, axs = plt.subplots(len(rules),3, figsize=(12, 2*len(rules)))
    for i, rule in enumerate(rules):
        E1 = rule[0]
        E2 = rule[1]
        S1 = rule[2]
        
        axs[i][0].plot([-1,*E1,1], vert, color="olive")
        axs[i][0].grid(axis='y')
        axs[i][0].set_ylabel(f"Rule {i+1}", fontsize=24)
        
        axs[i][1].plot([-1,*E2,1],vert, color="blue")
        axs[i][1].grid(axis='y')
        
        
        axs[i][2].plot([-1,*S1,1],vert, color="orange")
        axs[i][2].grid(axis='y')
    #Titles
    fig.tight_layout()
    fig.subplots_adjust(top=0.95)
    fig.suptitle("Rule Map", fontsize=40)
    axs[0][0].set_title('E1', fontsize=24)
    axs[0][1].set_title('E2', fontsize=24)
    axs[0][2].set_title('S1', fontsize=24)
    plt.show()


#Maqina de Inferencia

def FIS(E1, E2, rules, method="COG", samples=41, ran=[-1.0,1.0]):
    d = numpy.abs(ran[1]-ran[0])
    sampling = numpy.arange(ran[0],ran[1],step=d/samples)
    out = numpy.zeros_like(sampling)
    t_rules = []
    h_per_rule = []
    for n, rule in enumerate(rules):
        h = min(memb_grade(E1,rule[0]),
          memb_grade(E2,rule[1]))
        #if h>0:
        t_rules.append(n+1)
        h_per_rule.append(h)
        for i, x in enumerate(sampling):
            f_x = min(h,memb_grade(x,rule[2]))
            out[i] = max(out[i],f_x)
            
    if method == "COG":
        if numpy.sum(out) == 0:
            S = 0
        else:
            S = numpy.sum(out*sampling)/numpy.sum(out)
        
    if method == "FOM":
        if numpy.sum(out) == 0:
            S = 0
        else:
            idx = numpy.argmax(out)
            S = sampling[idx]
    
    if method == "MOM":
        if numpy.sum(out) == 0:
            S = 0
        else:
            max_value = numpy.max(out)
            idxs = numpy.where(out == max_value)
            mxs = sampling[idxs]
            S = numpy.mean(mxs)
    
    return S, sampling, out, [t_rules,h_per_rule]


def remove_rules(rules, i_rules):
    for idx in i_rules:
        rules[idx-1] = None

    new_rules = []

    for idx, rule in enumerate(rules):
        if rule:
            new_rules.append(rule)

    return new_rules