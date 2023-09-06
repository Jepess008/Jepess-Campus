# programa en general
def leerInt(msg):
    while True:
        try:
            n= int(input(msg))
            return n
        except ValueError:
            print("Error! . Ingrese un número entero valido.")

def msgError(msg):
    print(" ----> ¡ERROR!" + msg)
    input("----> Presione la tecla Enter para continuar .....")

def menu():
    while True:
        print("\n*****")
        print(" MENU ")
        print("******\n")
        print("1. SUMAR")
        print("2. RESTAR")
        print("3. MULTIPLICAR")
        print("4. DIVIDIR")
        print("5. POTENCIA")
        print("6. FACTORIAL")
        print("7. SALIR")
        op= leerInt("\n>> Opción(1 a 7)? ")
        if op < 1 or op > 7:
            msgError("Opcion no valida")
            continue
        return op

def sumar():
    print("\n" *3, "*** 1. Sumar ***")
    n1= leerInt("Ingrese un número: ")
    n2= leerInt("Ingrese otro número: ")
    print("\n ==> El resultado de la suma es: ", n1+n2)
    input("-----> Presione  cualquier tecla para volver al menu....")

def restar():
    print("\n" *3, "*** 2. Restar ***")
    n1= leerInt("Ingrese un número: ")
    n2= leerInt("Ingrese otro número: ")
    print("\n ==> El resultado de la resta es: ", n1-n2)
    input("-----> Presione  cualquier tecla para volver al menu....")


def multiplicar():
    print("\n" *3, "*** 3. Multiplicar ***")
    n1= leerInt("Ingrese un número: ")
    n2= leerInt("Ingrese otro número: ")
    print("\n ==> El resultado de la multiplicacion es: ", n1*n2)
    input("-----> Presione  cualquier tecla para volver al menu....")

def dividir():
    print("\n" *3, "*** 4. Dividir ***")
    n1= leerInt("Ingrese un número: ")
    n2= leerInt("Ingrese otro número: ")
    print("\n ==> El resultado de la division es: ", n1/n2)
    input("-----> Presione  cualquier tecla para volver al menu....")


def potencia():
    print("\n" *3, "*** 5. Potencia ***")
    n1= leerInt("Ingrese un número: ")
    n2= leerInt("Ingrese otro número: ")
    print("\n ==> El resultado de la Potenciacion es: ", n1**n2)
    input("-----> Presione  cualquier tecla para volver al menu....")

def factorial():
    print("\n" *3, "*** 6. Factorial ***")
    n1= leerInt("Ingrese un número: ")
    f= 1
    for i in range(1, n1+1):
        f *= i
    print("\n ==> El resultado del factorial  es: ",f)
    input("-----> Presione  cualquier tecla para volver al menu....")



while True:
    opcion= menu()

    if opcion==1:
        sumar()
    elif opcion==2:
        restar()
    elif opcion==3:
        multiplicar()
    elif opcion==4:
        dividir()
    elif opcion==5:
        potencia()
    elif opcion==6:
        factorial()
    elif opcion ==7:
        print("\n ** Gracias por usar la MiniCalculadora**")
        break
    else:
        msgError("Opcion Invalida. ")