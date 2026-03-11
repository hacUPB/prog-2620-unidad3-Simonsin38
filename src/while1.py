# Solicitar dos números al usuario e imprimir los valores pares que hay entre dichos números.
mayor = 0
menor = 0
n1 = int(input("Introduzca el primer número: "))
n2 = int(input("Introduzca el segundo número: "))
if n1 > n2:
   mayor = n1
   menor = n2
else:
    mayor = n2
    menor = n1

while menor <= mayor:
    if mayor % 2 == 0:
        print(mayor)
    mayor -= 1