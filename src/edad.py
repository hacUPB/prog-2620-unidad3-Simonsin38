# Clasificador según la edad

edad = int(input("Ingrese su edad: "))

if 0 <= edad <= 125:
    if edad < 6:
        etapa = "Infancia"
    elif edad < 12:
        etapa = "Niñez"
    elif edad < 20:
        etapa = "Adolescencia"
    elif edad < 25:
        etapa = "Juventud"
    elif edad < 60:
        etapa = "Adultez"
    else:
        etapa = "Vejez"
    print(f"A sus {edad} años, usted está en la etapa de {etapa}")
else:
    print("El número ingresado no es una edad válida")

