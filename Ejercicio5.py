# Ejercicio 5
'''Dada una compra, si su valor es mayor a 1000 Bs tendra un descuento de 20%,
de lo contrario tendra un descuento del 5%'''

compra= float(input("ingresa el monto de la compra: "))
descuento= 0

if compra > 0:
    if compra > 1000:
        descuento = compra * 0.20
        False
        if compra < 1000:
            descuento = compra * 0.5

print("el total a pagar es:", compra - descuento)
print("el descuento aplicado es:", descuento)