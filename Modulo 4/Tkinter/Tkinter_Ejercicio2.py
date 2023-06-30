#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crear una funcion que fuerce el ingreso de solo numeros.

Debo recibir un numero decimal por argumento, y verificar que este sea
un numero posible de convertir a INT. Caso contrario, volver a pedir el ingreso dentro de la 
funcion.

Debe retonar el valor convertido a INT
"""

def pedirNumero() :
    numero = input("Ingrese un numero: ")
    while not numero.isdecimal() or numero != "" or numero != float(numero):
        numero = input("Ingrese un numero: ")
    return int(numero)

print(pedirNumero())