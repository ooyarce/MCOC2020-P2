# MCOC2020-P2
Diseño Estructural Optimo aplicando Programación orientada a objetos

Integrantes:

- Paulina Guerra
- Omar Oyarce (jefe)
- Exequiel Vial

** Resultado Entrega 2 ** 

![alt_text](https://github.com/ooyarce/MCOC2020-P2/blob/master/result.png?raw=true)

**README ESCRITO POR EXEQUIEL VIAL, LO SUBIÓ OMAR PORQUE EXEQUIEL TUVO PROBLEMAS AL SUBIRLO**
**Escoja 5 barras interesantes del reticulado (identificadas por sus nodos) y manualmente realice el rediseño, buscando minimizar el peso de la barra y cumplir con FU < 1.0 comparando con los resultados de su programa.**
Las barras que como grupo elegimos para rediseñar son las:
-	0-1
-	1-8
-	3-6
-	5-6
-	1-5
Todas con dimensiones iniciales de 8 cm. de radio y 5 mm. de espesor, como la idea del rediseño es optimizar el uso de material se busca bajar el valor de ambas medidas, cumpliendo las siguientes condiciones:  
 
 1.- Raiz (L/radiogiro) < 300
 2.-	En caso de las barras en compresión el Pu se calcula como min(Area/Sigmay; picuadradoEL/L2)

Y el Fu como ØPu/Pn debe ser menor a 1 pero lo más cercano posible
- En las barras en tracción se calcula sólo como Tu = Area/sigmay y  el Fu como ØTn/Tu debe ser menor a 1 pero lo más cercano posible

**Comente respecto de la nueva distribución de FU del reticulado y el peso del mismo. ¿Que cambios globales se pueden hacer para mejorar aún más el costo (peso del acero) del mismo?**
Se logra apreciar, como era esperado, que la disminución de las dimensiones de las barras produjo un aumento de cargas en las otras barras ya que deben soportar una mayor carga, pero al mismo tiempo disminuye el peso total del puente lo que disminuye la carga muerta total. Para mejorar más el costo lo que se puede es optimizar todas las barras que no se estudiaron en este experimento.

![alt_text](https://github.com/ooyarce/MCOC2020-P2/blob/master/1.png?raw=true)
![alt_text](https://github.com/ooyarce/MCOC2020-P2/blob/master/2.png?raw=true)
![alt_text](https://github.com/ooyarce/MCOC2020-P2/blob/master/3.png?raw=true)
![alt_text](https://github.com/ooyarce/MCOC2020-P2/blob/master/4.png?raw=true)
![alt_text](https://github.com/ooyarce/MCOC2020-P2/blob/master/5.png?raw=true)
