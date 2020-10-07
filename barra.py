# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:17:27 2020

@author: pauli
"""
import numpy as np
g = 9.81 #kg*m/s^2

# --------------------------------------------------------------------------------------------------
# ENTREGA 1
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
        A = self.calcular_area()
        L = self.calcular_largo(ret)
        xi = ret.obtener_coordenada_nodal(self.ni)
        xj = ret.obtener_coordenada_nodal(self.nj)
        cosθx = (xj[0] - xi[0])/L
        cosθy = (xj[1] - xi[1])/L
        cosθz = (xj[2] - xi[2])/L
        
        Tθ = np.array([ -cosθx, -cosθy, -cosθz, cosθx, cosθy, cosθz]).reshape((6,1))

        return self.E * A / L * (Tθ @ Tθ.T )

    def obtener_vector_de_cargas(self, ret):
        W= self.calcular_peso(ret)
        return np.array ([0, 0,-W,0,0,-W])
 


    def obtener_fuerza(self, ret):
        ue = np.zeros(6)
        ue[0:3] = ret.obtener_desplazamiento_nodal(self.ni)
        ue[3:] = ret.obtener_desplazamiento_nodal(self.nj)
		
        A = self.calcular_area()
        L = self.calcular_largo(ret)

        xi = ret.obtener_coordenada_nodal(self.ni)
        xj= ret.obtener_coordenada_nodal(self.nj)

        cosθx = (xj[0] - xi[0])/L
        cosθy = (xj[1] - xi[1])/L
        cosθz = (xj[2] - xi[2])/L
        
        Tθ = np.array([ -cosθx, -cosθy, -cosθz, cosθx, cosθy, cosθz]).reshape((6,1))

        return self.E * A / L * (Tθ.T @ ue)
        	





# --------------------------------------------------------------------------------------------------
# ENTREGA 3:
# ---------------------------------------------------------------------------------------------------




    def chequear_diseño(self, Fu, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
		revisar si esta barra cumple las disposiciones de diseño.
		"""
        # Para el caso de tracción o compresión
        # Resistencia nominal:
        A= self.calcular_area()
        Fn= A* self.σy
        
        # Se multiplica Fn por el factor de minoración    
        if ϕ*Fn < abs(Fu):
            return False
        else:
            return True

    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
		calcular y devolver el factor de utilización
		"""
        A= self.calcular_area()
        Fn= A* self.σy
        # FU = 0. 
        return abs(Fu) / abs(ϕ*Fn)

    def rediseñar(self, Fu, ret, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
		re-calcular el radio y el espesor de la barra de modo que
		se cumplan las disposiciones de diseño lo más cerca posible
		a FU = 1.0.
		"""
        self.R = 0.6*self.R   #cambiar y poner logica de diseño: 0.6 
        self.t = 0.6*self.t   #cambiar y poner logica de diseño
        return None

      

