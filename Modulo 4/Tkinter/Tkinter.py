#!/usr/bin/env python
# -*- coding: utf-8 -*-

#LIBRERIA TKINTER ----> TK INTER

import tkinter as tk
import time

#print(time.asctime()) #imprime la fecha y hora actual

def funcion_boton():
    print("Se hizo click en el boton")


def funcion_boton2():
    nombre = caja.get()
    etiqueta_nombre.config(text= "Hola, soy " + nombre)

ventana = tk.Tk() #crea la ventana
ventana.config(width=400, height=300) #configura el tamaño de la ventana
ventana.config(bg="pink") #-configura el color de fondo de la ventana
ventana.title("Aplicacion de escritorio") #configura el titulo de la ventana

boton = tk.Button(ventana, text="Click", bg="violet", command=funcion_boton) #crea un boton y le cambia el color de fondo
boton.place(x=20, y=120, width=200, height=25) #posiciona el boton en la ventana

caja = tk.Entry(ventana) #crea una caja de texto
caja.place(x=20, y=50, width=200, height=25) #posiciona la caja de texto en la ventana

etiqueta = tk.Label(ventana, text="Ingresa tu nombre:", bg="yellow") #crea una etiqueta y le cambia el color de fondo
etiqueta.place(x=20, y=20) #posiciona la etiqueta en la ventana

etiqueta_nombre= tk.Label
etiqueta_nombre.place(x=40, y=200)

ventana.mainloop() #mantiene la ventana abierta