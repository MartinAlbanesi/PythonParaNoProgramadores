#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Hola a todos") #cadena de caracteres
print(1) #numero entero

print(3*2) #operaciones matematicas

print("2" + "2") #concatena dos cadenas de caracteres


#Variables
suma = 3+2
palabra = "hola"

print(suma)
print(palabra)

print(type(suma)) #muestra el tipo de la variable
print(type(palabra))

"""
TIPOS DE VARIABLES
- int 
- float
- str
- booleans
"""

#Abrir consola interactiva de Python (Windows -> Ejecutar -> Python)

a = 3

#En Python, el operador || es OR y el operador && es AND
print(a > 1 or a == 0) 
print(a > 1 and a == 5)

# El operador ! (distinto/negación) es NOT
print(not a == 10)

print(2**3) #potencia
print(8 ** (1/3)) #raiz cubica

print(not True) #negacion

edad = input("cuantos años tenes: ")
print(type(edad))
