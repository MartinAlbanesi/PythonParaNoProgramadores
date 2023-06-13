#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Crea un programa que solicite una fila y una columna e imprima en
pantalla el numero en esa posicion segun la siguiente matriz:

matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

El programa debe checkear que la fila y la columna tenga valores válidos
Si alguno de los valores es invalido, debe imprimir un mensaje de error
'''

matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

fila = int(input("Ingrese una fila: "))
columna = int(input("Ingrese una columna: "))

if(fila < 0 or fila > len(matriz) - 1 or columna < 0 or columna > len(matriz[0]) - 1):
    print("Error, fila o columna invalida")
else:
    print(matriz[fila][columna])
