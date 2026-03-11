def menu():
    opcion = 0
    while opcion < 1 or opcion > 4:
        print("1. Suma\n2. Resta \n3. Multiplicación \n4. División")
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 4:
            print("Opción no válida...\n")
    
    return opcion
operación = menu()
print(f"el usuario eligió la opción {operación}")

if operación.lower() == "suma":
    print("Suma")
elif operación == 2:
    print("División")