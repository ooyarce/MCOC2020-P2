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
        return np.array([self.ni,self.nj])
    
    def calcular_area(self):
        A = np.pi*(self.R**2) - np.pi*((self.R-self.t)**2)
        return A
		
    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra. """
 	    # xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        # xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        xi= reticulado.obtener_coordenada_nodal(self.ni) #falta algo
        xj= reticulado.obtener_coordenada_nodal(self.nj) #falta algo
        distancia_ij= (((xi[0]-xj[0])**2 + (xi[1]-xj[1])**2 + (xi[2]-xj[2])**2)**(1/2))
        return  distancia_ij

    def calcular_peso(self, reticulado):
        """Devuelve el peso de la barra. """
        L= self.calcular_largo(reticulado)
        A= self.calcular_area()
        peso = (self.ρ* A * L * g)
        return  peso
        







