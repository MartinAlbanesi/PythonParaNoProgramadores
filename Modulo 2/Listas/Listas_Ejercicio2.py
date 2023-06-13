#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escribir un programa que almancene las materias de un curso en una lista:

- Matematicas
- Fisica
- Quimica
- Historia

Se debe preguntar al usuario que notas ha sacado en cada materia y después se 
debe mostrar por pantalla el siguiente mensaje:

"En <materia> sacaste <nota>".
'''

materias = ["Matematicas", "Fisica", "Quimica", "Historia"]
notas = []
cont = 0

while len(materias) > cont:
     notas.append(input("Introduce la nota de " + materias[cont] + ": "))
     cont += 1

cont = 0

while len(materias) > cont:
    print(materias[cont] + ": " + notas[cont])
    cont += 1
