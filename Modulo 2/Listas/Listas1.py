#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Declaración de listas
nombre_lista = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

lista2 = ["Pedro", "Luciana", "Josefina", "Joaquin"]

lista3 = ["CABA", 3, True, 2.5]

print(lista2)
lista2.append("Juan") # append(<elemento>) -> agrega un elemento al final de la lista
print(lista2)
lista2.insert(1, "Juan") # insert(<nro indice>, "Juan") -> agrega un elemento en el indice indicado
print(lista2)
del lista2[-1] # del <lista>[<indice>] -> elimina el elemento en el indice indicado
print(lista2)

lista2.remove("Pedro") # remove(<elemento>) -> elimina el elemento indicado
print(lista2)

print(len(nombre_lista)) # len(<lista>) -> devuelve la cantidad de elementos de la lista

print(nombre_lista[len(nombre_lista) -  1]) # nombre_lista[<indice>] -> devuelve el elemento en el indice indicado
