def menu():
    opcion = 0
    while 1 > opcion or opcion > 3:
        print("Dirección del Viento (seleccione una) \n 1. En contra \n 2. A favor \n 3. Cruzado o nulo")
        opcion = int(input("Introduzca una opción: "))
        if 1 > opcion or opcion > 3:
            print("Opción Inválida")
    return opcion
combustible = float(input("Ingrese el combustible en kg: "))
ruta = float(input("Ingrese la ruta en km: "))
waypoints = ruta // 50
consumo = 0
comb_lim = 556 
cons_base = 2.4
while waypoints > 0 and combustible > comb_lim:
    opcion = menu()
    if opcion == 1:
        consumo = cons_base * 1.15
    elif opcion == 2:
        consumo = cons_base * 0.85
    else:
        consumo = cons_base
    combustible = combustible - consumo*100
    ruta = ruta - 50
    print(f"Quedan aproximadamente {ruta}km restantes")
    print(f"Combustible: {combustible}kg")
    waypoints = waypoints - 1
    
if waypoints == 0:
    print("Ruta Terminada")
if combustible < 556:
    print("ALERTA CRÍTICA, ATERRIZAR INMEDIATAMENTE EN EL AEROPUERTO MÁS CERCANO")