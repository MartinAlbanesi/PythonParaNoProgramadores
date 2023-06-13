#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Se tiene una lista de nombres y se desea recorrer con un bucle for

Ordenar de mayor a menor (Z-A) e imprimir por pantalla cada elemento

nombres = ["Agustina", "Marisa", "Juan", "Osvaldo"]
'''

nombres = ["Agustina", "Marisa", "Juan", "Osvaldo"]

nombres.sort(reverse=True)

for nombre in nombres :
    print(nombre)