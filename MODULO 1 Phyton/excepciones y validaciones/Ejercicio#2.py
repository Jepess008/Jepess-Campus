"""Búsqueda de palabra clave: Escribe un programa que solicite al usuario que ingrese una oración y una
palabra clave específica. El programa debe verificar si la palabra clave está presente en la oración y
mostrar un mensaje apropiado. Si la palabra clave se encuentra, el programa debe detenerse y mostrar
un mensaje de éxito. Si la palabra clave no se encuentra en la oración, el programa debe continuar
pidiendo al usuario que ingrese otra oración hasta que se encuentre la palabra clave o el usuario ingrese
"salir" para terminar el programa."""

while True:
    clave=input(" ingrese la clave")
    if clave=="":
        print("ingrese una clave correcta")
        continue
    break
while True:
    frase= input("ingrese la frase")
    if frase =="":
        print("ingrese una frase correcta")
        continue
    break
while True:
    frase!= "Salir"
    if clave in frase:
        print(" encontraste la clave")
    break