#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escribir un programa que pida al usuario una palabra y muestre por pantalla
el número de veces que contiene cada vocal
'''

palabra = input("Ingrese una palabra: ").lower()

vocales = ["a", "e", "i", "o", "u"]

cantidad = [0] * 5

for letra in palabra :
    for i in range(len(vocales)):
        if letra == vocales[i]:
            cantidad[i] += 1
            
for vocal in vocales:
    print(vocal + ": " + str(cantidad[vocales.index(vocal)]))