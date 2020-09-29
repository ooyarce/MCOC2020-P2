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
        self.xyz.resize((self.Nnodos+1,3))
        self.xyz[self.Nnodos,:] = [x,y,z]
        self.Nnodos +=1
        return
        
    def agregar_barra(self,barra):
        self.barras.append(barra)
        
    def obtener_coordenada_nodal(self, n):
        if n >= self.Nnodos:
            return
        return self.xyz[n, :]
    
    def calcular_peso_total(self):
        peso = 0.
        for b in self.barras:
            peso += b.calcular_peso(self)
        return peso
    
    def obtener_nodos(self):
        return self.xyz[0: self.Nnodos,:].copy()
    
    def obtener_barras(self):
        return self.barras
    
    def __str__(self):
        s = "nodos\n"  
        for n in range(self.Nnodos):
            s += f" {n} : ( {self.xyz[n,0]}, {self.xyz[n,1]}, {self.xyz[n,2]} )\n "
        s += "\n"
        s += "barras: \n"
        for b in range(len(self.barras)):
            s+=f"{b} : [{self.barras[b].ni} {self.barras[b].nj}] \n"
        return s
        
