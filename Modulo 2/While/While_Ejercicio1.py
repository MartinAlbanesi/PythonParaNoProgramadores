#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Con un bucle while incrementar una variable entera de uno en uno
desde 0 a 10 sin incluir.

Mostrar por patalla el resultado por cada vuelta del bucle
'''

variable = 0

while variable < 9: # while <condicion> -> ejecuta el bloque de código mientras la condición sea verdadera
    variable += 1 # NO EXISTEN LOS OPERADORES ++ y -- EN PYTHON
    print(variable)