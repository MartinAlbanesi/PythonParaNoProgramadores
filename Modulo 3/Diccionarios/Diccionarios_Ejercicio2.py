#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Preguntar al usuario:

- nombre
- edad
- direccion
- telefono 

guardar en un diccionario y mostrar por pantalla

<nombre> tiene <edad> años, vive en <direccion> y su numero de telefono es
<telefono>
'''

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su direccion: ")
telefono = input("Ingrese su telefono: ")

usuario = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}

print(usuario["nombre"] + " tiene " + usuario["edad"] + " años, vive en " + usuario["direccion"] + " y su numero de telefono es " + usuario["telefono"])
