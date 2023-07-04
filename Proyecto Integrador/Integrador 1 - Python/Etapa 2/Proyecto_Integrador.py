#!/usr/bin/env python
# -*- coding: utf-8 -*-

alumnos = {}
opcion = 0

while opcion != 3:
    print("____________________________________________________")
    
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Ver la lista de alumnos.")
    print("2 - Añadir un alumno a la lista.")
    print("3 - Ver la cantidad de cursos de un alumno.")
    print("3 - Salir.")
    
    opcion = int(input())
    
    if opcion == 1:
        print("Lista de alumnos:")
        for alumno in alumnos:
            cursos =  alumnos[alumno]
            print("Alumno: ", alumno, " - ", str(cursos), " cursos")
            
    elif opcion == 2:
        alumno = input("Ingrese el nombre del alumno: ")
        cursos = int(input("Ingrese la cantidad de cursos: "))
        alumnos[alumno] = cursos
        print("¡El alumno fue añadido al diccionario!")
        
    elif opcion == 3:
        alumnoBuscado = input("Ingresar el nombre del alumno:")
        for alumno in alumnos:
            if alumnoBuscado in alumno:
                print(alumno, " - ", str(alumnos[alumno]), " cursos")
        
    elif opcion == 4:
        print("¡Gracias por utilizar el programa!")
        
    else:
        print("La opción ingresada no es correcta, vuelva a intentarlo.")
    