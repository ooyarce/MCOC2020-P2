# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:17:27 2020

@author: pauli
"""
import numpy as np
g = 9.81 #kg*m/s^2

# ---------------------------------------------------------------------------------------------------
# ENTREGA 1: 
# ---------------------------------------------------------------------------------------------------
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
        return A
		
    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra.
        ret: instancia de objeto tipo reticulado
        """
 	    # xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        # xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        xi= reticulado.obtener_coordenada_nodal(self.ni) #falta algo
        xj= reticulado.obtener_coordenada_nodal(self.nj) #falta algo
        distancia_ij= (((xi[0]-xj[0])**2 + (xi[1]-xj[1])**2 + (xi[2]-xj[2])**2)**(1/2))
        return  distancia_ij
    
    
    # Otra opción, por el profe:
        # dij = xi-xj
        # return np.sqrt(np.dot(dij,dij))

    def calcular_peso(self, reticulado):
        """Devuelve el peso de la barra. 
        ret: instancia de objeto tipo reticulado """
        L= self.calcular_largo(reticulado)
        A= self.calcular_area()
        peso = (self.ρ * A * L * g)
        return  peso
        
# ---------------------------------------------------------------------------------------------------
# ENTREGA 2: 
# ---------------------------------------------------------------------------------------------------
    def obtener_rigidez(self, ret):
        """Devuelve la rigidez ke del elemento. Arreglo numpy de (4x4)
        ret: instancia de objeto tipo reticulado
        """
        L= self.calcular_largo(ret)
        A= self.calcular_area()
        k= self.E * A/L
        
        
    # Posicion del nodo
    # ni(xi,yi)
        xi=ret.xyz[self.ni,0]
        yi=ret.xyz[self.ni,1]
    # nj(xj,yj)   
        xj=ret.xyz[self.nj,0]
        yj=ret.xyz[self.nj,1]
        
        
    # Proyección de L0 con respecto al ángulo teta:
    # Como L0*cos(teta)= xj-xi: 
        cos_teta= (xj-xi)/L
    # Como L0*sin(teta)= yj-yi: 
        sin_teta= (yj-yi)/L
        
        
     # Vector evaluado en el ángulo de la barra
        Tteta= np.array ([[-cos_teta],[-sin_teta],[cos_teta],[sin_teta]])
    # Matriz de rigidez:
        ke= (Tteta @ Tteta.T) * k
                
        return ke


    def obtener_vector_de_cargas(self, ret):
        """Devuelve el vector de cargas nodales fe del elemento. Vector numpy de (4x1)
        ret: instancia de objeto tipo reticulado
        """
        
        W=self.calcular_peso(ret)
        # Vector de fuerzas externas:
        vec= np.array([[0],[-1],[0],[-1]]) 
        
        # Para evaluar en trabajo externo:
        fe= vec*(W/2.0) 
          
        return fe

       

    def obtener_fuerza(self, ret):
        """Devuelve la fuerza se que debe resistir la barra. Un escalar tipo double. 
        ret: instancia de objeto tipo reticulado
        """
        L= self.calcular_largo(ret)
        A= self.calcular_area()
        k= self.E * A/L
        
        ni=self.ni
        nj=self.nj
        
        # U=  [Uf, Uc]^T
        # Para cada elemento se tiene: gdl globales
        u2ni= ret.u[ni*2]
        u2ni1= ret.u[((2*ni)+1)]
        u2nj= ret.u[2*nj]
        u2nj1= ret.u[((2*nj)+1)]
        
        # Subconjunto del Utotal
        ue= np.array([u2ni, u2ni1, u2nj, u2nj1])
           
        
        # Posicion del nodo
    # ni(xi,yi)
        xi=ret.xyz[ni,0]
        yi=ret.xyz[ni,1]
    # nj(xj,yj)   
        xj=ret.xyz[nj,0]
        yj=ret.xyz[nj,1]
        
    # Proyección de L0 con respecto al ángulo teta:
    # Como L0*cos(teta)= xj-xi: 
        cos_teta= (xj-xi)/L
    # Como L0*sin(teta)= yj-yi: 
        sin_teta= (yj-yi)/L

        
        # Vector evaluado en el ángulo de la barra
        Tteta= np.array ([[-cos_teta],[-sin_teta],[cos_teta],[sin_teta]])
        # Fuerza de los elementos
        se = k * (Tteta.T @ ue)

        return se


      

