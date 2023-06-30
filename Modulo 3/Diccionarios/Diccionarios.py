#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Listas
# 1) TUPLAS - TUPLES
# 2) Sets
# 3) Diccionarios

# Pares clave-valor (key-value pair)

persona = {"nombre" : "Juan", "telefono" : "1153425032"} # Crear un diccionario

print(persona["nombre"], persona["telefono"])

otra_persona = dict(nombre = "Pedro", telefono = "1123512650") # dict() crea un diccionario

print(otra_persona["nombre"], otra_persona["telefono"])

otra_persona["nombre"] = "Jose" # Modificar una clave-valor

print(otra_persona["nombre"])

otra_persona["direccion"]= "Av. Siempreviva 742" # Agregar una clave-valor

print(otra_persona["direccion"])

print(otra_persona)

del otra_persona["direccion"] # Eliminar una clave-valor

print(otra_persona)

for clave in otra_persona:
    print(clave, otra_persona[clave])