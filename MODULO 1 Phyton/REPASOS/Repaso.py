#Diserñar una funcion que calcule la media de tres números leidos en teclado y poner un ejemplo de su aplicacion

def leerInt(msg):
    while True:
        try:
            n= int(input(msg))
            return n
        except ValueError:
            print("Error! . INgrese un número entoero valido.")

def media(n1, n2, n3):
    m = (n1+n2+n3)/3
    return m

a=leerInt("Ingrese el primer número:")
b=leerInt("Ingrese el primer número:")
c=leerInt("Ingrese el primer número:")
promedio= media(a, b, c)
print(f"el promedio de la media de {a}, {b} , {c} es {promedio}")
