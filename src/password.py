# Genere una constante de texto que será la contraseña. Luego pida al usuario que ingrese la contraseña. 
# Mientras la contraseña no sea la correcta, debe continuar a pedir la contraseña.
# Si esta es correctam, se deja continuar al resto del programa.

password = "ocY58x"
contraseña = input("Introduzca su contraseña: ")
contador = 3
while password != contraseña and contador > 0:
    print("Contraseña incorrecta")
    contraseña = input("Introduzca su contraseña: ")
    contador -= 1
    print(f"Le quedan {contador} intentos")
    if contador == 0:
        print("Acceso Denegado")
    else:
        if contraseña == password:
            print("Acceso concedido")



    
