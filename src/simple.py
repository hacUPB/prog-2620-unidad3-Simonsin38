compra = int(input("Ingrese el valor de la compra: "))
domicilio = 0
total = 0
if compra < 100000:
    domicilio = 9000
total = compra + domicilio


print(f"El valor a pagar es de ${total}")