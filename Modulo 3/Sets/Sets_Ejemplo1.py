#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Listas
# 1) TUPLAS - TUPLES
# 2) Sets
# 3) Diccionarios

numeros = [1, 1, 2, 3, 4]

a = set(numeros) # Transformar una lista a un Set
b = {1, 5} # Crear un Set

print(a | b) # Union
print( a & b) # Interseccion
print(a - b) # Diferencia
print(a ^ b) # Diferencia simetrica
    
# OPERADOR TERNARIO
# <valor si es True> if <condicion> else <valor si es False>

print("Si esta" if 7 in a else "No esta")


# Ejemplo de operador ternario

edad = 22

if edad >= 18:
    mensaje = "Es mayor de edad"
else:
    mensaje = "Es menor de edad"
    
print(mensaje)

mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"

print(mensaje)