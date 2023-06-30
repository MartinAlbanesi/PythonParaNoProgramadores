#!/usr/bin/env python
# -*- coding: utf-8 -*-

letras = ["a", "b", "c", "d"]

for letra in letras:
    if letra == "a":
        pass # pass -> no hace nada
    else:
        print(letra)
        
        
nombres = ["Pedro", "Luciana", "Josefina", "Martin"]

for nombre in nombres:
    if nombre.capitalize().startswith("J"): #.startswith("J") -> Empieza con la letra J | # capitalize() -> convierte la primera letra en mayuscula
        print(nombre, "empieza con J")
        break # break -> corta el ciclo
else: # else -> se ejecuta si el ciclo termina sin cortarse
    print("No hay nombres que empiecen con J")
    