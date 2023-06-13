
"""
Sumar tres variables

En un script de Python, crear 3 variables nombradas a, b y c con valores 
numéricos cualesquiera. Una cuarta variable llamada resultado que sea
la suma de las primeras 3 y por último imprimir en pantalla cada una
de ellas.

Antes de mostrar el valor de cada variable, indicar su nombre en una
línea anterior.
"""

a = 3
b = 5
c = 1
resultado = a + b + c

print("Variable a")
print(a)
print("Variable b")
print(b)
print("Variable c")
print(c)
print("Variable resultado")
print(resultado)

#Concatenación de string y int
print("Variable a = "  + str(a))

#Cambio de tipo de variable

print(type(a))
a = str(a)
print(type(a))