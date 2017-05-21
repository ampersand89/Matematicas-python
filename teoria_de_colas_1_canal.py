#!/usr/bin/python
# Teoria de colas
# Formulas de un solo canal
from __future__ import division

lam = input("lambda: ")
mu = input ("mu: ")



# Numero de unidades en el sistema
def funcion_ls(lam, mu):
    ls = lam/(mu-lam)
    return ls

# tiempo en el cual una unidad esta en el sistema

def funcion_ws(lam, mu):
    ws = 1/(mu-lam)
    return ws

# numero promedio de unidades esperando en la fila
def funcion_lq(lam, mu):
    lq = (lam**2)/(mu*(mu-lam))   
    return lq 

# tiempo en que una unidad espera en la fila
def funcion_wq(lam, mu):
    wq = lam/(mu*(mu-lam))
    return wq

# factor de uso del sistema
def funcion_P(lam, mu):
    P = lam/mu
    return P

#Probabilidad de que ninguna unidad se encuentre en el sistema y 
#probabilidad de que el sistema tenga exactamente "n" unidades

def funcion_P_sub_n(P, n):
    P_sub_n = (1-P)*(P**n)
    return P_sub_n     

print 'N de unidades en el sistema: ', funcion_ls(lam, mu), 'unidades'
print 'Tiempo de unidad en el sistema: ', funcion_ws(lam, mu), 'horas' 
print 'Promedio de unidades esperando en fila: ', funcion_lq(lam, mu), 'unidades'
print 'Tiempo de espera en fila de una unidad:' , funcion_wq(lam, mu), 'horas'
P = funcion_P(lam, mu)
print 'factor de uso del sistema', P, 
print ' Probabilidad de que ninguna unidad se encuentra en el sistema: ', funcion_P_sub_n(P, 0)*100, '%'
#llamdo para dos unidades)
print ' probabilidad para dos unidades: ', funcion_P_sub_n(P, 2)*100, '%'
