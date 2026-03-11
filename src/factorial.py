# Crear una función, que calcula el factorial de un número y la retorna.
def factorial(numero:int):
    # Si el número es 0 el factorial es 1
    # Si el número es menor que 0 retornar -1
    # Multiplicar desde 1 hasta número y acumular el resultado
    if numero >= 0:
        acumulador = 1
        for factor in range(1, numero + 1):
          acumulador = acumulador * factor
    else:
        acumulador = -1
    
    return acumulador
a = int(input("Introduzca un número: "))

resultado = factorial(a)
if resultado == -1:
    print("Error")
else: 
    print(f"{a}! = {resultado}")




