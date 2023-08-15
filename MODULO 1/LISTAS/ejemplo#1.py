#EJEMPLO 1
# HACER UN PROGRAMA QUE AYUDE A UN PROFESOR CON LAS NOTAS DE (0,5) DE ESTUDIANTES.
#EL PROFESOR INGRESA LA NOTA DE LOS 10 ESTUDIANTES QUE TIENE Y EL PROGRAMA LE MUESTRA.
# EL PROMEDIO DE LAS NOTAS, LA NOTA MAYOR, LA NOTA MENOR Y LAS TRES PRIMERAS NOTAS DE MAYOR A MENOR

def leerFloat(msg):
    while True:
        try:
            n= float(input(msg))
            if n<0 or n>5:
                print("Error. Ingrese una nota validad de (0,5).")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! . Ingrese una nota valido.")

lstNotas=[]
for est in range(1,11):
    nota = leerFloat(f"Ingrese nota estudiante {est}: ")
    lstNotas.append(nota)

notMen = min(lstNotas)
print("La nota menor es: ", notMen)
notMay= max(lstNotas)
print("La nota mayor es: ", notMay)

promNotas = sum(lstNotas)/10
print("El promedio de las notas es: ", promNotas)

tresNotas= lstNotas.sort(reverse=True)
tresNotas= lstNotas[0:3]
strNotas= ""
for nota in tresNotas:
    strNotas += str(nota) + ","
print("Las tres mejores notas son: ", strNotas)