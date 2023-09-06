import json

with open("MODULO 1/json/simulacro/PetShopping.json", "r") as archivo:
    store= json.load(archivo)

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


def menuact():
    print("-"*40)
    print("Bienvenido al PetShopping acontinuacion presentamos las opciones que puede modificar:\n MENU")
    print("-"*40)
    print("1.CAMBIAR RAZA")
    print("2.CAMBIAR TALLA")
    print("3.CAMBIAR PRECIO")
    print("4.CAMBIAR SERVICIOS")
    print("5.SALIR")
    print("-"*40)
    opcion= leerInt("Ingrese una opcion de acuerdo a lo que desea realizar:  ")
    if opcion<1 or opcion>5:
        msgError("OPCION NO VALIDA")
    return opcion

def menu():
    print("-"*40)
    print("Bienvenido al PetShopping acontinuacion presentamos las opciones:\n MENU")
    print("-"*40)
    print("1.LISTAR MASCOTAS")
    print("2.CREAR NUEVA MASCOTA")
    print("3.MOSTRAR DATOS MASCOTAS")
    print("4.ACTUALIZAR DATOS MASCOTA")
    print("5.ELIMINAR MASCOTA")
    print("6.SALIR")
    print("-"*40)
    opcion= leerInt("Ingrese una opcion de acuerdo a lo que desea realizar:  ")
    if opcion<1 or opcion>6:
        msgError("OPCION NO VALIDA")
    return opcion

def listar():
    for i in store["pets"]:
        print(i)

def crear(store):
    tipo=leerString("Ingrese el tipo de mascota: ")
    raza=leerString("Ingrese la raza de las mascota: ")
    talla=leerString("Ingrese la talla de la mascota: ")
    precio=leerInt("Ingrese el precio de la mascota: ")
    while True:
        servicios=[]
        servicio=leerString("Ingrese el servicio de la mascota: ")
        servicios.append(servicio)
        op= leerInt("Desea ingresar otro servicio? 1: SI - 2: NO: ")

        while op==1:
            servicio=leerString("Ingrese el servicio de la mascota: ")
            servicios.append(servicio)
            op= leerInt("Desea ingresar otro servicio? 1: SI - 2: NO: ")
        else:
            break
        
    print(store)
    store["pets"].append({
        "tipo": tipo,
        "raza": raza,
        "talla":talla,
        "precio":precio,
        "servicios":servicios
    })
    with open("MODULO 1/json/simulacro/PetShopping.json", "w") as archivo:
        json.dump(store,archivo,ensure_ascii=False, indent=4)



def mostrar():
    tipo= leerString("Ingrese el tipo de mascota a listar: ")
    for i in store["pets"]:
        if i["tipo"] == tipo:
            print(i)
        
def actualizar():
    indice=0
   
    for i in store["pets"]:
        indice += 1
        print(indice,i)
        
    seleccion=leerInt(" Ingrese el indice de la mascota que desea actualizar: ")
    print("_________________________________________________________________")
    print(store["pets"][seleccion-1])
    
    op = menuact()
    if op==1:
        newRaza= leerString("Ingrese la nueva raza a modificar: ")
        store["pets"][seleccion-1]["raza"]= newRaza
        print(store["pets"][seleccion-1])
        
    with open("MODULO 1/json/simulacro/PetShopping.json", "w") as archivo:
        json.dump(store,archivo,ensure_ascii=False, indent=4)  

def eliminar():
    pass



while True:
    opcion = menu()
    if opcion==1:
        listar()

    elif opcion==2:
        crear(store)

    elif opcion==3:
        mostrar()
    
    elif opcion==4:
        actualizar()

    elif opcion==5:
        eliminar()

    elif opcion==6:
        op=leerInt("Desea continuar o salir del sofware\n 1.= CONTINUAR \n 2.= SALIR ")
        if op==1:
            continue
        else:
            print("Gracias por ultilizar nuestro sofware, nos vemos pronto!! :D ")
            break

print(store)