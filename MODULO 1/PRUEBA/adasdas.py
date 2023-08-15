#! /usr/bin/env python3
idd=[]
nombre=[]
horas=[]
valor=[]
#CREAMOS EL MENU
def leerIntm(msg):
    while True:
        try:
            n=int(input(msg))
            return n
        except ValueError:
            print=("Invalido ingrese un número Valido")

def leerInt(msg):
    while True:
        try:
            n=int(input(msg))
            return n
        except ValueError:
            print=("Invalido ingrese un número Valido")

def msgError(msg):
    print=("Invalido................................" , msg)   
    input("------------> Presione la tecla para continuar")  

def menu():
        while True:
            print ("\n ----------------------------------------------------------------")
            print ("\n MENU")
            print("-------------------------------------------------------------------\n")
            print ("1. Agregar un empelado")
            print ("2. Modificar empleado")
            print ("3. Buscar empleado")
            print ("4. Eliminar empleado")
            print ("5. Listar empleados")
            print ("6. Listar nomina de un empleado")
            print ("7. Listar nomina de todos los empleados")
            print ("8. Salir")
            opcion = leerInt("\n Ingrese una opción ")
            if opcion <=1 or opcion>=8:
                    print ("Digite un número de acuerdo a las opciones presentadas")
                    continue
            return opcion

#CREAMOS LAS FUNCIONES
def addEmpleado():
        documento = int(input("Ingrese el documento del empleado"))
        idd.append(documento)
        name=input("Ingrese nombre del empleado")
        name.lower()
        nombre.append(name)
        hora= int(input("Ingrese la cantidad de horas trabajadas"))
        if hora >=1 or hora <= 160:
            horas.append(hora)
        else:
            print ("La cantidad de horas trabajadas no esta en el rango de horas permitidas")
        costo=int(input("Ingrese el valor de la hora trabajada"))
        if costo>=8000 or costo<=150000:
            valor.append(costo)
        else:
            print("El costo de la hora no corresponde al rango de pago por la empresa")


def modEmpleado():
    while True:
        busidd= int(input(" Ingrese el id del empleado a modificar: "))
        if busidd in idd:
            indice=idd.index(busidd)
            break
        print(" Usuario no encontrado, digite de nuevo: ")
    print(" Que deseas modificar? \n 1. Nombre \n 2.Horas trabajadas \n 3.Valor de la hora ")
   
    while True:
        op= leerIntm("\n Ingrese una opcion")
        if op >=1 or op <= 3:
            if op==1:
                newNombre=input("Ingrese el nuevo nombre: ")
                nombre [indice]= newNombre
                print("El cambio de nombre fue exitoso")
            elif op==2:
                newHoras= int(input("Ingrese las nuevas horas: "))
                horas [indice]= newHoras
                print("Las horas fueron modificadas con exito")
            elif op==3:
                newValor= int(input("Ingrese el nuevo valor:  "))
                valor[indice]= newValor
                print("El valor fue modificado")
            break
        else:
            print("Digite un nùmero de acuerdo a las opciones presentadas")

def busEmpleado():
    while True:
        busidd= int(input(" Ingrese el id del empleado a Buscar: "))
        if busidd in idd:
            indice=idd.index(busidd)
            empleado= nombre[indice]
            iddEmpleado= idd[indice]
            horasEmpleado=horas[indice]
            valorEmpleado=valor[indice]
            print(f"El empleado {empleado} con documento {iddEmpleado} cuenta con la cantidad de horas de {horasEmpleado} por un valor de hora de {valorEmpleado}")
            break    
        print(" Usuario no encontrado, digite de nuevo: ")
    
def delEmpleado():
    while True:
        busidd= int(input(" Ingrese el id del empleado a Eliminar: "))
        if busidd in idd:
            indice=idd.index(busidd)
            idd.pop(indice)
            nombre.pop(indice)
            horas.pop(indice)
            valor.pop(indice)
            print("El empleado fue eliminado correctamente: ")
            break    
        print(" Usuario no encontrado, digite de nuevo: ")

def lisEmpleado():
    for indice in range(len(idd)):
        print(f"El nombre del empleado es: {nombre[indice]}, el documento del empleado es: {idd[indice]}, la cantidad de horas es: {horas[indice]}, por valor de cada hora de: {valor[indice]}")
        if indice==4:
            print("\n 1.Desea seguir consultado? .\n 2. Salir, No desea consultar mas")
            while True:
                op= leerIntm("\n Ingrese una opcion")
                if op ==1 or op == 2:
                    if op==1:
                        continue
                    else:
                        break

def lisNomEmpleado():
    pass

def lisNomAll():
    pass




#Programa en General
while True:
    opcion=menu()

    if opcion==1:
        addEmpleado()
    elif opcion==2:
        modEmpleado()
    elif opcion==3:
        busEmpleado()
    elif opcion==4:
        delEmpleado()
    elif opcion==5:
        lisEmpleado()
    elif opcion==6:
        lisNomEmpleado()
    elif opcion==7:
        lisNomAll()
    elif opcion==8:
        print ("Gracias por usar nuestro Sofware\n 'Nos vemos pronto'")
        break
else:
    msgError("Opcion Invalida") 