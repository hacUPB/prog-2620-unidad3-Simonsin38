edad_usuario = int(input("Introduzca su edad: "))
saldo_billetera = float(input("Introduzca su saldo: "))
tiene_suscripcion_premium = False
precio = 60
descuento = precio*0.9
A = edad_usuario >= 17
B = saldo_billetera >= 60 or tiene_suscripcion_premium == True and saldo_billetera >= 50
compra_exitosa = A and B
print("¿Puede comprar el juego?: ", compra_exitosa)