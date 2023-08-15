import json

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                print("Error! El codigo debe ser entero postivo.")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero valido")

def msgError(msg):
    print("----> ¡ERROR!" + msg)
    input("---> Presione ENTER para continuar")

def leerString(msg):
    while True:
        try:
            n= input(msg)
            if n.strip() == "":
                print("Error!! ingrese un nombre valido.")
                continue
            return n
        except Exception as e:
            print("Error! . Ingrese una letra valida.", e.message)

def leerFloat(msg):
    while True:
        try:
            n = float(input(msg))
            if n < 1:
                print("Error! El codigo debe ser entero postivo.")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero valido")

jugadores={}

while True:
    nombre= leerString("Ingrese el nombre del jugador: ")
    edad= leerInt("Ingrese la edad del jugador: ")
    peso= leerFloat("Ingrese el peso del jugador: ")
    jugadores[nombre]={}
    jugadores[nombre]["edad"]= edad
    jugadores[nombre]["peso"]= peso
    op=leerInt("Desea ingresar la informacion de otro jugador? 1.Si 2.No: ")
    if op==1:
        continue
    else:
        print("Gracias por usar el Sofware")
        break

with open("Jugadores.json", "w") as archivo:
    json.dump(jugadores,archivo,indent=4)

print(jugadores)
