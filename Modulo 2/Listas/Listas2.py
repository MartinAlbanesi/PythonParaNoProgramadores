#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Reemplazar un valor de la lista
letras = ["a", "b", "c", "d"]
letras[0] = "A"

## Crear una lista de 10 ceros
ceros = [0] * 10
print(ceros)

## Combinar Listas
combinada = ceros + letras 
print(combinada)

## Los strings tambien son iterables, iteran por sus caracteres
##caracteres = list("Hola")
caracteres = "Hola"

print(len(caracteres))

contador = 0
cont = 0

while contador < len(caracteres):
    print(caracteres[contador])
    contador += 1
    
#----------------------------------------------#
    
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)
print(numeros[0:5]) # [0:5] -> devuelve los elementos desde el indice 0 hasta el 5 sin incluirlo
print(numeros[::-1]) # [::-1] -> invierte la lista

del numeros[0:5] # del <lista>[<indice inicio>:<indice fin>] -> elimina los elementos desde el indice inicio hasta el indice fin sin incluirlo

numeros.clear() # clear() -> elimina todos los elementos de la lista


## Guardar los elementos en variables

numeros2 = [1, 2, 3, 4, 4, 4, 4, 9]
primero, segundo, *otros = numeros2 # *<nombre> -> guarda los elementos restantes en una lista
print(primero, segundo)
print(otros)

primero, *otros, ultimo = numeros2
print(primero)
print(otros)
print(ultimo)


## Ordenar listas

numeros3= [3, 51, 2, 8, 6]
numeros3.sort() # sort() -> ordena los elementos de la lista de menor a mayor
print(numeros3)
numeros3.sort(reverse=True) # sort(reverse=True) -> ordena los elementos de la lista de mayor a menor
print(numeros3)

letras2 = ["b", "z", "a", "c"]
letras2.sort()
print(letras2)

palabras = ["casa", "mesa", "arbol"]
palabras.sort()
print(palabras)

print(sorted(palabras, reverse=True)) # sorted(<lista>) -> ordena los elementos de la lista de menor a mayor sin modificar la lista original
