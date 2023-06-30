#!/usr/bin/env python
# -*- coding: utf-8 -*-

alumnos = []
opcion = 0

while opcion != 3:
    print("____________________________________________________")
    
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Ver la lista de alumnos.")
    print("2 - Añadir un alumno a la lista.")
    print("3 - Salir.")
    
    opcion = int(input())
    
    if opcion == 1:
        print("Lista de alumnos:")
        for alumno in alumnos:
            print(alumno[0] + " - " + str(alumno[1]) + " cursos")
    elif opcion == 2:
        alumno = input("Ingrese el nombre del alumno: ")
        cursos = int(input("Ingrese la cantidad de cursos: "))
        alumnos.append([alumno, cursos])
        print("¡El alumno fue añadido a la lista!")
    elif opcion == 3:
        print("¡Gracias por utilizar el programa!")
    else:
        print("La opción ingresada no es correcta, vuelva a intentarlo.")
    