"""
Ejercicio 022

Escribir un programa que permita ingresar tres números enteros e indicar cual
es el mayor.
"""
n1 = int(input("primer numero: "))
n2 = int(input("segundo numero: "))
n3 = int(input("tercer numero: "))

mayor = n1

if n2 > mayor:
    mayor = n2

if n3 > mayor:
    mayor=n3

print("el numero mayor es: " , mayor)

"""
FUNCIONA
"""