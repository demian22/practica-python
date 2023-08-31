"""
Ejercicio 021

Escribir un programa que permita ingresar dos números enteros e indicar si el
primero es mayor, menor o igual al segundo.
"""

print("calculo de si un numero es mayor o menor que otro")
numero1 = int(input("ingrese un numero entero: "))
numero2 = int(input("ingrese otro numero entero: "))

if numero1 == numero2:
    print("los dos numeros son iguales")

else:
    if numero1 > numero2:
        print(numero1 , "es mayor que" , numero2)

    else:
        print(numero1 , "es menor que" , numero2)

"""
FUNCIONA
"""