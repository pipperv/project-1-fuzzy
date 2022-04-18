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

#Reglas Difusas

rules = [[          ng, de_a(ng,pp), pg],
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

#
def compute_plant(method,P0,PO=700,K=0.7,points=50):
	# Entrega una lista del valor de P en cada instancia de tiempo
	# desde t=0 hasta t=points-1

	#Condiciones Iniciales
	P = P0
	EP, TP, dH = 0, 0, 0

	points-=1

	P_list = [P0]

	for t in range(points):
		TP = EP
		EP = P - PO
		TP -= EP

		norm_EP = numpy.sign(EP)*min(1,abs(EP/12))
		norm_TP = numpy.sign(TP)*min(1,abs(TP/12))

		S, sampling, out, t_rules = FIS(norm_EP,norm_TP,rules,method)

		dH = S*12
		dP = K * dH
		P += dP
		P_list.append(P)

	return P_list

#plt.figure()
#plt.plot(range(points+1),P_list)
#plt.show()