# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:22:02 2020

@author: Speedy Gonzàlez
"""

import numpy as np 

class Reticulado(object):
    
    def __init__(self):
        
        super(Reticulado, self).__init__()
        
        self.xyz = np.zeros((0,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
    
    def agregar_nodo(self, x, y, z=0):
        if self.Nnodos+1 > Reticulado.__NnodosInit__:
            self.xyz.resize((self.Nnodos + 1, 3))
        self.xyz[self.Nnodos,:] = [x,y,z]
        self.Nnodos += 1 
        
    
    def agregar_barra(self,barra):
        self.barras.append(barra)
        
    def obtener_coordenada_nodal(self, n):
        if n >= self.Nnodos:
            return
        return self.xyz[n, :]
    
    def calcular_peso_total(self):
        
        peso = 0.
        for b in self.barras:
            peso += b.calcular_peso_total(self)
        return peso
    
    def obtener_nodos(self):
        return self.xyz[0: self.Nnodos,:].copy()
    
    def obtener_barras(self):
        return self.barras
    

    
    
    
    
    
    
    