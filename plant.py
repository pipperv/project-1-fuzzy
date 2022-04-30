from cld_utils import *
import matplotlib.pyplot as plt
import numpy

#Conjuntos Difusos

ng = [-1.0,-1.0,-0.8,-0.5]
nm = [-0.8,-0.5,-0.4,-0.2]
np = [-0.4,-0.3,-0.2,-0.1]
ni = [-0.2,-0.1, 0.0, 0.0]
ce = [-0.2, 0.0, 0.0, 0.2]
pi = [ 0.0, 0.0, 0.1, 0.2]
pp = [ 0.1, 0.2, 0.3, 0.4]
pm = [ 0.2, 0.4, 0.5, 0.8]
pg = [ 0.5, 0.8, 1.0, 1.0]

fuzzy_interface = [ng,nm,np,ni,ce,pi,pp,pm,pg]
fuzzy_names = ["ng","nm","np","ni","ce","pi","pp","pm","pg"]

def get_sets():
    return fuzzy_interface.copy(), fuzzy_names.copy()

#Reglas Difusas

rules_ = [[          ng, de_a(ng,pp), pg],
		 [ de_a(ng,nm), de_a(ng,np), pm],
		 [          np, de_a(np,pi), pm],
		 [          ni, de_a(ng,nm), pm],
		 [          ni, de_a(pm,pg), np],
		 [ de_a(ni,pi),          ce, ce],
		 [          pi, de_a(ng,nm), pp],
		 [          pi, de_a(pm,pg), nm],
		 [          pp, de_a(np,pg), nm],
		 [ de_a(pm,pg), de_a(pp,pg), nm],
		 [          pg, de_a(np,pg), ng],
		 [          ni,          pp, ce],
		 [          ni,          np, pp],
		 [          pi,          np, ce],
		 [          pi,          pp, np],
		 [ de_a(ng,np), de_a(pm,pg), pg],
		 [ de_a(pp,pg), de_a(ng,nm), ng]]

def get_rules():
    return rules_.copy()
#
def compute_plant(method,P0,PO=700,K=0.7,points=50, get_EP_TP =False, rules=None):
	# Entrega una lista del valor de P en cada instancia de tiempo
	# desde t=0 hasta t=points-1

	#Condiciones Iniciales
	P = P0
	EP, TP, dH = 0, 0, 0

	points-=1

	P_list = [P0]
	t_rules_list = []

	if get_EP_TP:
			TP_l = []
			EP_l = []
			S_l = []
	if not rules:
		rules = get_rules()


	for t in range(points):
		TP = EP
		EP = P - PO
		TP -= EP

		

		norm_EP = numpy.sign(EP)*min(1,abs(EP/12))
		norm_TP = numpy.sign(TP)*min(1,abs(TP/12))
	
		S, sampling, out, t_rules = FIS(norm_EP,norm_TP,rules, method)

		dH = S*12
		dP = K * dH 
		P += dP
		P_list.append(P)
		t_rules_list.append(t_rules)

		if get_EP_TP:
			EP_l.append(norm_EP)
			TP_l.append(norm_TP)
			S_l.append(S)

	if get_EP_TP:
		return P_list, t_rules_list, EP_l, TP_l, S_l
	return P_list, t_rules_list


def compute_realistic_plant(method,P0,H0=700,PO=700,K=0.7,points=50, get_EP_TP =False, rules=None, c=0.5):
	# Entrega una lista del valor de P en cada instancia de tiempo
	# desde t=0 hasta t=points-1

	#Condiciones Iniciales
	P, H = P0, H0
	EP, TP, dH, dP = 0, 0, 0, 0

	points-=1

	P_list, H_list = [P0], [H0]
	t_rules_list = []

	if get_EP_TP:
			TP_l = []
			EP_l = []
			S_l = []
	if not rules:
		rules = get_rules()


	for t in range(points):
		TP = EP
		EP = P - PO
		TP -= EP

		

		norm_EP = numpy.sign(EP)*min(1,abs(EP/12))
		norm_TP = numpy.sign(TP)*min(1,abs(TP/12))
	
		S, sampling, out, t_rules = FIS(norm_EP,norm_TP,rules, method)

		dH = S*12
		dP = K * dH + c * dP
		P += dP
		H += dH
		H_list.append(P)
		P_list.append(P)
		t_rules_list.append(t_rules)

		if get_EP_TP:
			EP_l.append(norm_EP)
			TP_l.append(norm_TP)
			S_l.append(S)

	if get_EP_TP:
		return P_list, H_list, t_rules_list, EP_l, TP_l, S_l
	return P_list, H_list, t_rules_list


#plt.figure()
#plt.plot(range(points+1),P_list)
#plt.show()