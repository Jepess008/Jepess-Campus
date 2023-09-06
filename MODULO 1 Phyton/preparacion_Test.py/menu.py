def menu():
    print("-"*40)
    print("Bienvenido al SisNotACME ACME acontinuacion presentamos las opciones:\n MENU")
    print("-"*40)
    print("1.ESTUDIANTES")
    print("2.NOTAS")
    print("3.REPORTE")
    print("4.SALIR")
    print("-"*40)
    opcion= leerInt("Ingrese una opcion de acuerdo a lo que desea realizar:  ")
    if opcion<1 or opcion>4:
        msgError("OPCION NO VALIDA")
    return opcion

def msgError(msg):
    print(" ----> ¡ERROR!" , msg)
    input("----> Presione la tecla Enter para continuar .....")


def leerInt(msg):
    while True:
        try:
            n=int(input(msg))
            return n
        except ValueError:
            print("Ingrese un número")

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

while True:
    op= menu()
    if op==1:
        #estudiantes()
        pass
    elif op==2:
        pass
        #notas()
    elif op==3:
        #reportes()
        pass
    elif op==4:
        print("Gracias por usar SisNotACME")
        break
    