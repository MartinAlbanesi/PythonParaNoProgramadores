#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escribir un programa que guarde en una variable el diccionario
{"Euro": "EUR", "Dolar": "USD", "Pesos": "ARS"}

pregunte al usuario por una divisa y muestre su abreviatura por pantalla.
Si la divisa no existe en el diccionario, dar aviso por pantalla.
'''

monedas = {"Euro": "EUR", "Dolar": "USD", "Pesos": "ARS"}

divisa = input("Ingrese una divisa: ").title()

if divisa in monedas:
    print(monedas[divisa])
else:
    print("ERROR, divisa no encontrada")