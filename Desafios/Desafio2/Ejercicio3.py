#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escriba un programa que permita crear una lista
de nombres.
Para ello, el programa tiene que pedir un número
y luego solicitar esa cantidad de nombres para
crear la lista. Por último, el programa tiene que
mostrar la lista creada.
'''

nombres = []
cant = int(input("Ingrese la cantidad de nombres a ingresar: "))

for i in range(cant):
    nombres.append(input("Ingrese el nombre " + str((i+1)) + ": "))
    
for nombre in nombres:
    print(nombre)
    
