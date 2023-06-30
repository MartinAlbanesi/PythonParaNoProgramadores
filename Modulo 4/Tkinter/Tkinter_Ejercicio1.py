#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crear una app de escritotio con dos cajas de texto y un boton,
de modo que al presionarla se imprima en pantalla la suma de los dos numeros
ingresados en las primeras. La disposicion de los controles y el tamaño son a 
eleccion.
"""

import tkinter as tk

def sumar():
    
    resultado = int(caja1.get()) + int(caja2.get())
    etiquetaResultado.config(text=str(resultado))


ventana = tk.Tk()
ventana.config(width=400, height=300, bg = "grey")
ventana.title("Calculadora de suma")

texto = tk.Label
texto.place(x=50, y=50, text="+")

caja1 = tk.Entry(ventana)
caja1.place(x=20, y=50, width=50, height=25)

caja2 = tk.Entry(ventana)
caja2.place(x=80, y=50, width=50, height=25)

boton = tk.Button(ventana, text="Sumar", bg="violet", command=sumar)
boton.place(x=20, y=100, width=100, height=25)

etiquetaResultado = tk.Label(ventana, text="Resultado", bg="yellow")
etiquetaResultado.place(x=20, y=150)

ventana.mainloop()