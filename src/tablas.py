# n = float(input("Intrese el número: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n*i} ")

print("Ingrese 10 valores: ")
suma = 0
for i in range(10):
    valor = int(input(f"Ingrese el valor {i+1}: "))
    suma = suma + valor
print(suma)