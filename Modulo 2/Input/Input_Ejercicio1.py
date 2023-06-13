#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Pedir nombre

Crear un programa que solicite el nombre de un alumno a través de la
consola, y luego chequee que no esté vacío.

En caso de estarlo tiene que imprimir un mensaje de error; caso 
contrario deberá imprimir un mensajes indicando que se ingresó correctamente.
'''


cadena = input("Introduce el nombre: ") # input(<mensaje>) -> muestra el mensaje y devuelve lo ingresado por teclado

if cadena != "":
    print("Nombre ingresado correctamente")
else:
    print("Error: no se ingresó ningún nombre")
