# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:17:27 2020

@author: pauli
"""
import numpy as np
g = 9.81 #kg*m/s^2

class Barra(object):
    def __init__(self, ni, nj, R, t, E, ρ, σy):
        super(Barra, self).__init__()
        self.ni = ni	
        self.nj = nj
        self.R = R
        self.t = t
        self.E = E
        self.ρ = ρ
        self.σy = σy
        
    def obtener_conectividad (self):
        return [self.ni,self.nj]
    
    def calcular_area(self):
        A = np.pi*(self.R**2) - np.pi*((self.R-self.t)**2)
        # 2Pi*r*H
        return A
		
    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra. """
 	    # xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        # xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        xi= reticulado.obtener_coordenada_nodal(self.ni) #falta algo
        xj= reticulado.obtener_coordenada_nodal(self.nj) #falta algo
        dij= (xi-xj)
        return np.sqrt (np.dot (dij,dij))

    def calcular_peso(self, reticulado):
        """Devuelve el largo de la barra. """
        L= self.calcular_largo()
        A= self.calcular_area()
        return self.ρ* A * L * g
        
from reticulado import Reticulado
from barra import Barra
from graficar2d import ver_reticulado_2d

# Unidades
cm = 1e-2
mm = 1e-3
kg = 1.0
GPa = 1e+9
MPa = 1e+6
KN = 1e3
m = 1.0

#Inicializar modelo
ret = Reticulado()


#Nodos
ret.agregar_nodo(0,0)
ret.agregar_nodo(1,0)
ret.agregar_nodo(1,1)

print(ret)

# #Barras
b1 = Barra(0, 1, 20*cm, 4*mm, 200*GPa, 7600*kg/m**3, 420*MPa)
b2 = Barra(1, 2, 20*cm, 4*mm, 200*GPa, 7600*kg/m**3, 420*MPa)
b3 = Barra(0, 2, 20*cm, 4*mm, 200*GPa, 7600*kg/m**3, 420*MPa)

ret.agregar_barra(b1)
ret.agregar_barra(b2)
ret.agregar_barra(b3)

peso_total = ret.calcular_peso_total()

print(f"peso_total = {peso_total}")

ver_reticulado_2d(ret)
        






