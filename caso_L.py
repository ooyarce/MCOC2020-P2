# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:35:07 2020

@author: pauli
"""

# Caso L cargas vivas

from reticulado import Reticulado
from barra import Barra

def caso_L():
	
	# Unidades base
    m = 1.
    kg = 1.
    s = 1. 
	
	#Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    KN = 1000*N
    kgf = 9.80665*N
    Pa = N / m**2
    KPa = 1000*Pa
    MPa = 1000*KPa
    GPa = 1000*MPa
	
	#Parametros
    L = 5.0  *m
    B = 2.0 *m
    H = 3.5 *m
    q  = 400*kgf/m**2
    F = q*L*B/4
   
	#Inicializar modelo
    ret = Reticulado()
	
	#Nodos
    ret.agregar_nodo(0     , 0   ,  0  ) #0
    ret.agregar_nodo(L     , 0   ,  0  ) #1
    ret.agregar_nodo(2*L   , 0   ,  0  ) #2
    ret.agregar_nodo(3*L   , 0   ,  0  ) #3
    ret.agregar_nodo(L/2   , B/2 ,  H  ) #4
    ret.agregar_nodo(3*L/2 , B/2 ,  H  ) #5
    ret.agregar_nodo(5*L/2 , B/2 ,  H  ) #6
    ret.agregar_nodo(0     , B   , 0   ) #7
    ret.agregar_nodo(L     , B   , 0   ) #8
    ret.agregar_nodo(2*L   , B   , 0   ) #9
    ret.agregar_nodo(3*L   , B   , 0   ) #10
	
	
	
	
	
	#Barras
    R = 8 *cm
    t = 5 *mm
    props = [R, t, 200*GPa, 0*kg/m**3, 420*MPa]
    ret.agregar_barra(Barra(0,  1, *props))   # 0
    ret.agregar_barra(Barra(1,  2, *props))   # 1
    ret.agregar_barra(Barra(2,  3, *props))   # 2
    ret.agregar_barra(Barra(3, 10, *props))   # 3
    ret.agregar_barra(Barra(10, 9, *props))   # 4
    ret.agregar_barra(Barra(9,  8, *props))   # 5
    ret.agregar_barra(Barra(8,  7, *props))   # 6
    ret.agregar_barra(Barra(7,  0, *props))   # 7
    ret.agregar_barra(Barra(8,  1, *props))   # 8
    ret.agregar_barra(Barra(9,  2, *props))   # 9
    ret.agregar_barra(Barra(7,  4, *props))   # 10
    ret.agregar_barra(Barra(0,  4, *props))   # 11
    ret.agregar_barra(Barra(1,  4, *props))   # 12
    ret.agregar_barra(Barra(8,  4, *props))   # 13
    ret.agregar_barra(Barra(1,  5, *props))   # 14
    ret.agregar_barra(Barra(2,  5, *props))   # 15
    ret.agregar_barra(Barra(9,  5, *props))   # 16
    ret.agregar_barra(Barra(8,  5, *props))   # 17
    ret.agregar_barra(Barra(2,  6, *props))   # 18
    ret.agregar_barra(Barra(3,  6, *props))   # 19
    ret.agregar_barra(Barra(10, 6, *props))   # 20
    ret.agregar_barra(Barra(9,  6, *props))   # 21
    ret.agregar_barra(Barra(0,  8, *props))   # 2
    ret.agregar_barra(Barra(1,  7, *props))   # 23
    ret.agregar_barra(Barra(1,  9, *props))   # 24
    ret.agregar_barra(Barra(2,  8, *props))   # 25
    ret.agregar_barra(Barra(2, 10, *props))   # 26
    ret.agregar_barra(Barra(3,  9, *props))   # 27
    ret.agregar_barra(Barra(4,  5, *props))   # 26
    ret.agregar_barra(Barra(5,  6, *props))   # 27
    
    
    
    
    
# Restricciones: Parte izquierda del reticulado es fija, y parte derecha es deslizante
	# Nodos 3 y 10 no desplazamiento en y,z....x libre
    ret.agregar_restriccion(10, 1, 0)
    ret.agregar_restriccion(10, 2, 0)
    ret.agregar_restriccion(3,  1, 0)
    ret.agregar_restriccion(3,  2, 0)
    


	#Nodo 7 y 0 son fijos
    ret.agregar_restriccion(7, 0, 0)
    ret.agregar_restriccion(7, 1, 0)
    ret.agregar_restriccion(7, 2, 0)
    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
    
    ret.agregar_fuerza(0, 2,     -F)
    ret.agregar_fuerza(1, 2, -(2*F))
    ret.agregar_fuerza(2, 2, -(2*F))
    ret.agregar_fuerza(3, 2,     -F)
    ret.agregar_fuerza(7, 2,     -F)
    ret.agregar_fuerza(8, 2, -(2*F))
    ret.agregar_fuerza(9, 2, -(2*F))
    ret.agregar_fuerza(10, 2,    -F)
    
    return ret