"""
Ejercicio 017

¡Ayuda! Se me rompió el programa que convierte una cantidad de dinero en la
cantidad mínima de billetes y monedas necesarios. Tengo todas las instrucciones
necesarias, pero están todas mezcladas. ¿Podrías ayudarme a ordenarlas de
manera correcta para que funcione el programa como debería? A lo mejor se me
perdieron algunas instrucciones, ¿podrías agregarlas?

resto = cantidad_total
billetes_cien = resto // 100
resto = resto % 100
billetes_cinco = resto // 5
billetes_mil = resto // 1000
billetes_cincuenta = resto // 50
billetes_doscientos = resto // 200
billetes_diez = resto // 10
billetes_docientos = resto // 200
resto = resto % 10
cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))
billetes_uno = resto // 1
print("Para la cantidad de  ",cantidadtotal,"senecesitan:")print(billetesmil,"billetesde 1000")
print(billetes_doscientos, "billetes de  200")print(billetescien,"billetesde 100")
print(billetes_cincuenta, "billetes de  50")print(billetesdiez,"billetesde 10")
print(billetes_cinco, "billetes de  5")print(billetesuno,"billetesde 1")

"""

cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))
billetes_cien = cantidad_total // 100
resto = 100
billetes_cinco = cantidad_total // 5
billetes_mil = cantidad_total // 1000
billetes_cincuenta = cantidad_total // 50
billetes_doscientos = cantidad_total // 200
billetes_diez = cantidad_total // 10
billetes_docientos = cantidad_total // 200
resto = resto % 10
billetes_uno = cantidad_total // 1

print("Para la cantidad de $", cantidad_total ,"senecesitan:")
print( billetes_mil ,"billetes de $1000")
print(billetes_doscientos, "billetes de $200")
print(billetes_cien,"billetes de $100")
print(billetes_cincuenta, "billetes de $50")
print(billetes_diez,"billetes de $10")
print(billetes_cinco, "billetes de $5")
print( billetes_uno ,"billetes de $1")

"""
FUNCIONA
"""