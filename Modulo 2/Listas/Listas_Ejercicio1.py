#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Lista de nombres
Se tiene la siguiente lista de nombres:
nombres = ["Susana","Alejandro","Roberto"]
Insertar entre Alejandro y Roberto a Paula. Y luego agregar al final a Silvina.
Para finalizar, hay que recorrer la lista y mostrar a
todos los nombres por pantalla.
'''

nombres = ["Susana","Alejandro","Roberto"]

nombres.insert(2, "Paula")
nombres.append("Silvina")

for nombre in nombres:
    print(nombre)