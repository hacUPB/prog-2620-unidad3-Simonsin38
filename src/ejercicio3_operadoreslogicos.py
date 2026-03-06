promedio = float(input("Ingrese su promedio académico"))
socio_economico = int(input("Ingrese su nivel socioecnómico"))

BecaPro = promedio >= 9.0 
BecaNiv = socio_economico == 1 and promedio > 8.0
BecaSi = BecaPro or BecaNiv

print("¿Tiene beca?:", BecaSi)

