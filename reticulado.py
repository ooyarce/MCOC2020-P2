import numpy as np
from scipy.linalg import solve

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    def __init__(self):
        super(Reticulado, self).__init__()
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        self.Ndimensiones = 2
        self.tiene_solucion = False

    def agregar_nodo(self, x, y, z=0):
        if self.Nnodos+1 > Reticulado.__NNodosInit__:
            self.xyz.resize((self.Nnodos+1,3))
        self.xyz[self.Nnodos,:] = [x,y,z]
        self.Nnodos +=1
        if z != 0.:
            self.Ndimensiones = 3
        
    def agregar_barra(self, barra):
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
        return self.xyz[0:self.Nnodos,:].copy()

    def obtener_barras(self):
        return self.barras

    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        """Agrega una restriccion, dado el nodo, grado de libertad y valor 
        del desplazamiento de dicho grado de libertad
        """
        if nodo not in self.restricciones:
            self.restricciones[nodo]= [[gdl, valor]]
        else:
            self.restricciones[nodo].append([gdl,valor])

    def agregar_fuerza(self, nodo, gdl, valor):
        """Agrega una restriccion, dado el nodo, grado de libertad y valor 
        del la fuerza en la direccion de dicho GDL
        """
        if nodo not in self.cargas:
            self.cargas[nodo] = [[gdl,valor]]
        else:
            self.cargas[nodo].append([gdl,valor])
        
    def ensamblar_sistema(self):
        """Ensambla el sistema de ecuaciones"""
        
        Ngdl = self.Nnodos * self.Ndimensiones
        self.K = np.zeros((Ngdl,Ngdl), dtype=np.double)
        self.f = np.zeros((Ngdl), dtype=np.double)
        self.u = np.zeros((Ngdl), dtype=np.double)
		
		#Implementar
        for b in self.barras:
            ni = b.ni
            nj = b.nj
            d = [2*ni, (2*ni)+1, 2*nj, (2*nj)+1]
            
            for i in range (len(d)):
                p = d[i]
                for j in range(len(d)):
                    q = d[j]
                    ke = b.obtener_rigidez(self)
                    self.K[p,q] += ke[i,j]
                    
                    fe = b.obtener_vector_de_cargas(self)
                self.f[p] += fe[i]
		
        return self.K, self.f 

    def resolver_sistema(self):
        
        K = self.K
        f = self.f
        Ngdl = self.Nnodos * self.Ndimensiones
        u = np.arange(Ngdl)
        gdl_libres = np.arange(Ngdl)
        gdl_restringidos_lista = []
        f_list = []

        for nodo in self.restricciones:
            nodo_dir_i = 2*nodo
            nodo_dir_j = 2*nodo + 1  
            if len(self.restricciones[nodo]) == 1:
                gdl_restringidos_lista.append(nodo_dir_j)
                u[nodo_dir_j] = 0
            else:
                gdl_restringidos_lista.append(nodo_dir_i)
                gdl_restringidos_lista.append(nodo_dir_j)
                u[nodo_dir_i] = 0
                u[nodo_dir_j] = 0
        
        for nodo in self.cargas:
            for carga in self.cargas[nodo]:
                gdl = carga[0]
                valor = carga[1]
                gdl_global = 2*nodo + gdl
                self.f[gdl_global] += valor
                
        gdl_libres = np.setdiff1d(gdl_libres,gdl_restringidos_lista)
        
        for carga in gdl_libres:
            f_list.append(f[carga])
                
        ff = f_list
        Kff = K[np.ix_(gdl_libres,gdl_libres)]
        uf = solve(Kff,ff)
        self.u[gdl_libres] = uf
        self.tiene_solucion = True
        return self.u
        
    def obtener_desplazamiento_nodal(self, n):
        """Entrega desplazamientos en el nodo n como un vector numpy de (2x1) o (3x1)
        """
        dofs = [2*n, 2*n+1]
        return self.u[dofs]

    def recuperar_fuerzas(self):
        fuerzas = np.zeros((len(self.barras)), dtype=np.double)
        for i,b in enumerate(self.barras):
            fuerzas[i] = b.obtener_fuerza(self)

        return fuerzas

    def __str__(self):
        s = "nodos:\n"
        for n in range(self.Nnodos):
            s += f"  {n} : ( {self.xyz[n,0]}, {self.xyz[n,1]}, {self.xyz[n,2]}) \n "
        s += "\n\n"

        s += "barras:\n"
        for i, b in enumerate(self.barras):
            n = b.obtener_conectividad()
            s += f" {i} : [ {n[0]} {n[1]} ] \n"
        s += "\n\n"
        
        s += "restricciones:\n"
        for nodo in self.restricciones:
            s += f"{nodo} : {self.restricciones[nodo]}\n"
        s += "\n\n"
        
        s += "cargas:\n"
        for nodo in self.cargas:
            s += f"{nodo} : {self.cargas[nodo]}\n"
        s += "\n\n"

        if self.tiene_solucion:
            s += "desplazamientos:\n"
            if self.Ndimensiones == 2:
                uvw = self.u.reshape((-1,2))
                for n in range(self.Nnodos):
                    s += f"  {n} : ( {uvw[n,0]}, {uvw[n,1]}) \n "
        s += "\n\n"

        if self.tiene_solucion:
            f = self.recuperar_fuerzas()
            s += "fuerzas:\n"
            for b in range(len(self.barras)):
                s += f"  {b} : {f[b]}\n"
        s += "\n"

        return s
