"""
Ejercicio 015

Definición del problema: Una inmobiliaria paga a sus vendedores un salario base,
más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas.
Realizar un programa que imprima el nombre del vendedor y el salario que le
corresponde en un determinado mes.

Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y
el valor total de las mismas.

¿Sobran datos? ¿Qué datos sobran?
Respuesta: si sobran datos,el porcentaje de comision y el salario base.
"""

nombre_vendedor = input("nombre de vendedor: ")
cantidad_ventas = int(input("ventas realizadas: "))
precio_ventas = float(input("precio de las ventas realizadas: "))
porcentaje = float(input("porcentaje de comision por ventas: "))
ventas_totales = (cantidad_ventas * precio_ventas)
print("nombre del vendedor : " , nombre_vendedor)
print("cantidad de ventas $" , precio_ventas)

"""
FUNCIONA
"""
