'''
Una tienda ofrece una promoción, por la compra de 3 artículos, el costo del elemento de menor valor tiene un descuento del 50%
'''


objeto_1 = int(input("Ingrese el valor del primer artículo: "))
objeto_2 = int(input("Ingrese el valor del segundo artículo: "))
objeto_3 = int(input("Ingrese el valor del tercer artículo: "))
total = 0
if objeto_1 < objeto_2 and objeto_3:
    total = objeto_1*0.5 + objeto_2 + objeto_3
else:
    if objeto_2 < objeto_1 and objeto_3:
        total = objeto_2*0.5 + objeto_3 + objeto_1
    else:
        total = objeto_3*0.5 + objeto_2 + objeto_1
print(f"Debe pagar ${total}")

    