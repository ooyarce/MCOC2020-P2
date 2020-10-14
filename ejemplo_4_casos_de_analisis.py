# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:09:40 2020

@author: pauli
"""
# Casos de análisis:
    
# Implementando carga muerta y carga viva
from caso_D import caso_D
from caso_L import caso_L
from graficar3d import ver_reticulado_3d

ret_D = caso_D()
ret_L = caso_L()

peso = ret_D.calcular_peso_total()

print(f"peso = {peso}")


ver_reticulado_3d(ret_D, 
	axis_Equal=True, 
	opciones_barras={
	"ver_numeros_de_barras": False
	}, 
    llamar_show=True,
    zoom=200.,
    deshabilitar_ejes=True)


#Reticulado para Peso propio
ret_D.ensamblar_sistema()
ret_D.resolver_sistema()
f_D = ret_D.recuperar_fuerzas()

#Reticulado para Carga Viva
ret_L.ensamblar_sistema()
ret_L.resolver_sistema()
f_L = ret_L.recuperar_fuerzas()


# Para rediseñar según combinacion
# for i in barras_a_diseñar:
    # barras[i].rediseñar(1.4*f_D[i])   (combinacion 1)
     # barras[i].rediseñar(1.*f_D[i]+1.6 f_L[i])   (combinacion 2)



#Combinaciones de carga
f_1 = 1.4*f_D           #Combinacion 1
f_2 = 1.2*f_D + 1.6*f_L #Combinacion 2


# Factores de utilización:
FU_caso1 = ret_D.recuperar_factores_de_utilizacion(f_1)
FU_caso2 = ret_D.recuperar_factores_de_utilizacion(f_2)




import matplotlib.pyplot as plt
# Tensiones caso 1
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=200.,
    deshabilitar_ejes=True)

plt.title("Tensiones en caso 1: 1.4 D ")
plt.show()


# Tensiones en caso 2
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "dato": f_2,
        "ver_dato_en_barras": True,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=200.,
    deshabilitar_ejes=True)

plt.title("Tensiones en caso 1: 1.2 D + 1.6 L")
plt.show()










# Factor de utilizacion caso 1
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True, 
        "dato": FU_caso1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=200.,
    deshabilitar_ejes=True)

plt.title("FU caso 1: 1.4 D ")
plt.show()


# Factor de utilizacion caso 2
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=200.,
    deshabilitar_ejes=True)

plt.title("FU caso 2: 1.2 D + 1.6 L")
plt.show()







# REDISEÑAR:
# Fu= #definir # Escribir Factor de utilización por cada barra
# ret_D.rediseñar (Fu)
    
    
    
# ret_D.rediseñar()    
# ret_L.rediseñar()  
    
    # iMPLEMENTAR
    
    
    
# barras_a_rediseñar =[]  # Elegir las barras
# barras_casoD= ret_D.obtener_barras()
# barras_casoL=ret_L.obtener_barras()







#Peso propio
ret_D.ensamblar_sistema()
ret_D.resolver_sistema()
f_D = ret_D.recuperar_fuerzas()

#Carga Viva
ret_L.ensamblar_sistema()
ret_L.resolver_sistema()
f_L = ret_L.recuperar_fuerzas()

#Combinaciones de carga
f_1 = 1.4*f_D           #Combinacion 1
f_2 = 1.2*f_D + 1.6*f_L #Combinacion 2

# Calcular factores 
FU_caso1_red = ret_D.recuperar_factores_de_utilizacion(f_1)
FU_caso2_red = ret_D.recuperar_factores_de_utilizacion(f_2)



