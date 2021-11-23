import numpy as np

arregloColores = np.array(
    [
        [["amarillo","verde","verde"],
        ["blanco","naranja","rojo"],
        ["rojo","blanco","verde"]]
    ,
        [["amarillo","verde","verde"],
        ["blanco","naranja","rojo"],
        ["rojo","blanco","verde"]]
    ,
        [["amarillo","verde","verde"],
        ["blanco","naranja","rojo"],
        ["rojo","blanco","verde"]]
    ]
    )

contadorDimension = 0
contadorFila = 0 
contadorPosicion = 0
cantidadPosicion = 0
cantidadAmarillo = 0
cantidadRojo = 0
cantidadNaranja = 0 
cantidadVerde = 0
cantidadBlanco = 0


for dimension in range(3):
    for fila in range(3):
        for posicion in range(3):
            if(arregloColores[dimension][fila][posicion].upper() == "AMARILLO"):
                cantidadAmarillo = cantidadAmarillo + 1
                   
            elif(arregloColores[dimension][fila][posicion].upper() == "ROJO"):
                cantidadRojo = cantidadRojo + 1
                   
            elif(arregloColores[dimension][fila][posicion].upper() == "NARANJA"):
                cantidadNaranja = cantidadNaranja + 1
           
            elif(arregloColores[dimension][fila][posicion].upper() == "VERDE"):
                cantidadVerde = cantidadVerde + 1
            
            elif(arregloColores[dimension][fila][posicion].upper() == "BLANCO"):
                cantidadBlanco = cantidadBlanco + 1
          

def imprimir():
    print(f"Numero de elementos 'amarillo'  : {cantidadAmarillo} ")
    print(f"Numero de elementos 'rojo'      : {cantidadRojo} ")
    print(f"Numero de elementos 'naranja'   : {cantidadNaranja} ")
    print(f"Numero de elementos 'verde'     : {cantidadVerde} ")
    print(f"Numero de elementos 'blanco'    : {cantidadBlanco} ")
  