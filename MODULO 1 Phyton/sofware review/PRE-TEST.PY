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

def msgError(msg):
    print(" ----> ¡ERROR!" , msg)
    input("----> Presione la tecla Enter para continuar .....")

def leerIva(msg):
    pass



def menu():
    print("-"*40)
    print("Bienvenido al Micromecardo ACME acontinuacion presentamos las opciones:\n MENU")
    print("-"*40)
    print("1.PRODUCTOS")
    print("2.VENTAS")
    print("3.INFORME")
    print("4.SALIR")
    print("-"*40)
    opcion= leerInt("Ingrese una opcion de acuerdo a lo que desea realizar:  ")
    if opcion<1 or opcion>4:
        msgError("OPCION NO VALIDA")
    return opcion

def addProducto():
    producto={}
    codigo= leerInt("Ingrese el codigo del producto a ingresar: ")
    nombre= leerString("Ingrese el nombre del producto a ingresar")
    valor= leerInt("Ingrese el valor del producto")
    cantidad= leerInt("Ingrese la cantidad de producto a ingresar")
    tipoIva= leerInt("Ingrese el tipo de iva para el producto que va ingresar")


def ventaProduc():
    pass

def informe():
    pass


# PROGRAMA EN GENERAL

while True:
    opcion = menu()
    if opcion==1:
        addProducto()

    elif opcion==2:
        ventaProduc()

    elif opcion==3:
        informe()
    
    elif opcion==4:
        op=leerInt("Desea continuar o salir del sofware\n 1.= SI\n 2.= NO ")
        if op==1:
            continue
        else:
            print("Gracias por ultilizar nuestro sofware, nos vemos pronto!! :D ")
            break