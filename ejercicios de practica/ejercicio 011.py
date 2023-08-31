"""
Ejercicio 011

Escribir un programa que permita resolver el siguiente problema:

Tres personas aportan diferente capital a una sociedad y desean saber el valor
total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).

Solicitar la carga por teclado del nombre de cada socio y su capital aportado,
a partir de esto calcular e informar lo requerido previamente.
"""

nombre_socio1 = input("nombre socio1= ")
aporte_socio1 = float(input("aporte socio1= "))
nombre_socio2 = input("nombre socio2= ")
aporte_socio2 = float(input("aporte socio2= "))
nombre_socio3 = input("nombre socio3= ")
aporte_socio3 = float(input("aporte socio3= "))

invercion_total = (aporte_socio1 + aporte_socio2 + aporte_socio3)

porcentaje_inversion_persona1 = round((aporte_socio1 / invercion_total) * 100, 2)
porcentaje_inversion_persona2 = round((aporte_socio2 / invercion_total) * 100, 2)
porcentaje_inversion_persona3 = round((aporte_socio3 / invercion_total) * 100, 2)

print(nombre_socio1 , "," , "aporto" , porcentaje_inversion_persona1 , "%")
print(nombre_socio2 , "," , "aporto" , porcentaje_inversion_persona2 , "%")
print(nombre_socio3 , "," , "aporto" , porcentaje_inversion_persona3 , "%")

print("capital total:" , "$" , invercion_total)

"""
FUNCIONA
"""