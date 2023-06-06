#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Un empleado cobró 300 dólares por mes desde enero
a junio, 500 dólares de julio a octubre, y 700 dólares
por mes en noviembre y en diciembre.
Hace un programa que calcule el sueldo promedio. Y
que diga si este “empleado” está cobrando un sueldo
bajo, normal o mejor de lo normal.
● Sueldo bajo: por debajo de 300 dólares.
● Sueldo normal: entre 300 a 900.
● Sueldo mejor de lo normal: más de 900 dólares.
'''

cobro_total = (300*6) + (500*4) + (700*2)

promedio_cobro = cobro_total / 12


if promedio_cobro < 300:
    print("Sueldo bajo")
elif promedio_cobro >= 300 and promedio_cobro <= 900:
    print("Sueldo normal")
else:
    print("Sueldo mejor de lo normal")