"""ENUNCIADO
La empresa ACME desea que le construya un programa para gestionar la nómina de sus empleados. Después
de recoger los requerimientos se llegó a la decisión de gestionar los empleados y sus nóminas a través del
siguiente menú.

*** NOMINA ACME ***
MENU
1- Agregar empleado
2- Modificar empleado
3- Buscar empleado
4- Eliminar empleado
5- Listar empleados
6- Listar nómina de un empleado
7- Listar nómina de todos los empleados
8- Salir
>> Escoja una opción (1-8)?

1. Agregar empleado: Esta opción permite adicionar un empleado con su id, nombre, horas trabajadas y
valor de la hora. Los empleados pueden trabajar entre 1 a 160 Horas. Y el valor de la hora puede estar
entre $8,000 y $150,000 pesos la hora.
2. Modificar empleado: Esta opción permite cambiar cualquiera de los datos del empleado, menos el id de
empleado.
3. Buscar empleado: Esta opción permite buscar un empleado por su id, si lo encuentra, muestra la
información de este y si no, muestra un mensaje de que el empleado no ha sido ingresado
4. Eliminar empleado: Esta opción permite eliminar a un empleado por su id. Si borra al empleado, muestra
un mensaje que ha sido eliminado y si no, muestra un mensaje de que no se eliminó el empleado.
5. Listar Empleados: Esta opción permite mostrar los empleados con su información (id, nombre, horas y
valor de la hora trabajada), debe permitir paginación, esto es, se muestran los primeros 5 empleados,
luego para y muestra un mensaje para que el usuario decida si desea seguir viendo o volver al menú. Si
desea seguir viendo, le muestra los siguientes 5 empleados y así sucesivamente hasta que no haya más
empleados o la persona no desee seguir viendo.
6. Listar la nómina de un empleado: Esta opción permite mostrar la nómina de un empleado buscado por
su ID. El salario bruto se calcula como el valor de la hora por la cantidad de horas trabajadas. Si gana
menos del salario mínimo legal vigente en Colombia 2023 (por favor consulte el dato) se le debe da
subsidio de transporte. Se le debe descontar el valor de la eps y pensión correspondiente al 4% cada uno
y el salario Neto es la suma del salario bruto, el auxilio menos los descuentos.
El menú debe mostrar los datos del empleado y los datos de la nómina.
7. Listar nómina de todos los empleados: Esta opción permite mostrar la nómina de todos los empleados.
El listado debe estar paginado cada 5 empleados. El calculo de la nómina de cada empleado es el mismo
que en la opción 6.
8. Salir: Esta opción sale del programa, pero antes le pregunta al usuario si desea salir de la aplicación.
Sino no desea, vuelve al menú. Si desea salir de la aplicación muestra un mensaje de despedida y termina
el programa."""

def leerInt(msg):
    while True:
        try:
            n=int(input(msg))
            return n
        except ValueError:
            print("Ingrese un número")

def leerIntm(msg):
    while True:
        try:
            n=int(input(msg))
            return n
        except ValueError:
            print=("Invalido ingrese un número Valido")

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

def leerIntVa(msg):
    while True:
        try:
            n=int(input(msg))
            if n<8000 or n>150000:
                print("Error!!! Ingrese un valor correcto en el rango de 8.000  a 150.000: \n ")
                continue
            return n
        except ValueError:
            print("Ingrese un número")

def leerIntHo(msg):
    while True:
        try:
            n=int(input(msg))
            if n<1 or n>160:
                print("Error!!! Ingrese una hora correcta en el rango de 1  a 160: \n ")
                continue
            return n
        except ValueError:
            print("Ingrese un número")

def msgError(msg):
    print(" ----> ¡ERROR!" + msg)
    input("----> Presione la tecla Enter para continuar .....")

def leerIntMod(msg):
    while True:
        try:
            n=int(input(msg))
            if n<1 or n>3:
                print("Error!!! Ingrese una opcion correcta:  \n ")
                continue
            return n
        except ValueError:
            print("Ingrese un número")
        


def menu():
    print("-"*40)
    print("Bienvenido al Sofware de Nomina acontinuacion presentamos las opciones:\n MENU")
    print("-"*40)
    print("1.Agrega empleado")
    print("2.Modificar empleado")
    print("3.Buscar empleado")
    print("4.Eliminar empleado")
    print("5.Listar empleado")
    print("6.Listar nomina")
    print("7.Listar nomina de todos los empleados")
    print("8.Salir")
    print("-"*40)
    opcion= leerInt("Ingrese una opcion de acuerdo a lo que desea realizar:  ")
    if opcion<1 or opcion>8:
        msgError("OPCION NO VALIDA")
    return opcion

nomina={}

def addEmpleado():
    while True:
        idd= int(input("Ingrese el documento del empleado:  "))
        name= leerString("Ingrese el nombre del empleado:  ")
        horas= leerIntHo("Ingrese la cantidad de horas trabajadas:  ")
        valor=leerIntVa("Ingrese el valor de la hora:  ")
        nomina[idd]={}
        nomina[idd]["nombre"]=name
        nomina[idd]["horas"]=horas
        nomina[idd]["valor"]=valor

        opcion= int(input("Desea ingresar otro Empleado? \n 1.SI \n 2.NO "))
        if opcion==2:
            break

def modEmpleado():
    while True:
        busqidd= int(input("Ingrese el documento que desea modificar"))
        if busqidd in nomina.keys():
            print("Se encontro el usuario ")
            break   
        else:
            print("Usuario no encontrado: ")

    
    print(" Que deseas modificar? \n 1. Nombre \n 2.Horas trabajadas \n 3.Valor de la hora ")

    op= leerIntMod("\n Ingrese una opcion")
    if op==1:
        newNombre=input("Ingrese el nuevo nombre: ")
        nomina[busqidd]["nombre"]= newNombre
        print("El cambio de nombre fue exitoso")
    elif op==2:
        newHoras= int(input("Ingrese las nuevas horas: "))
        nomina [busqidd] ["horas"]= newHoras
        print("Las horas fueron modificadas con exito")
    elif op==3:
        newValor= int(input("Ingrese el nuevo valor:  "))
        nomina[busqidd]["valor"]= newValor
        print("El valor fue modificado")
    input("Presione cualquier tecla para volver al menu")

def busEmpleado():
    while True:
        busqidd= int(input("Ingrese el documento que desea consultar"))
        if busqidd in nomina.keys():
            print("Se encontro el usuario ")
            print(nomina[busqidd])
            break   
        else:
            print("Usuario no encontrado, El empleado no ha sido ingresado: ")

def delEmpleado():
    while True:
        busqidd= int(input("Ingrese el documento que desea modificar"))
        if busqidd in nomina.keys():
            nomina.pop(busqidd)
            print("Usuario eliminado correctamente ")
            break   
        else:
            print("Usuario no encontrado: ")

def listEmpleado():
      k=0
      for k in nomina.keys():
        print(f"{nomina[k]['nombre']}, {k} , {nomina[k]['horas']}, {nomina[k]['valor']}")
        if k==4:
            print("\n 1.Desea seguir consultado? .\n 2. Salir, No desea consultar mas")
            while True:
                op= leerIntm("\n Ingrese una opcion")
                if op ==1 or op == 2:
                    if op==1:
                        continue
                    else:
                        break

def listNom():
    while True:
        busqidd= int(input("Ingrese el documento que desea calcular"))
        if busqidd in nomina.keys():
            if busqidd in nomina.keys():
                hora=nomina[busqidd]["horas"]
                valor=nomina[busqidd]["valor"]
                salarioBruto= hora*valor
                eps=salarioBruto*0.04
                pension=salarioBruto*0.04
                
                auxTrasnporte=140600
                if salarioBruto<1160000:
                    salarioTotal= salarioBruto-eps-pension+auxTrasnporte
                    print(f"{nomina[busqidd]['nombre']}, {busqidd} , {nomina[busqidd]['horas']}, {nomina[busqidd]['valor']} ", salarioTotal)
                else:
                    salarioTotal=salarioBruto-eps-pension
                    print(f"{nomina[busqidd]['nombre']}, {busqidd} , {nomina[busqidd]['horas']}, {nomina[busqidd]['valor']} ", salarioTotal)
            break   
        else:
            print("Usuario no encontrado: ")
    


def listAllNom():
    k=0
    for k in nomina.keys():
        hora=nomina[k]["horas"]
        valor=nomina[k]["valor"]
        salarioBruto= hora*valor
        eps=salarioBruto*0.04
        pension=salarioBruto*0.04       
        auxTrasnporte=140600
        if salarioBruto<1160000:
            salarioTotal= salarioBruto-eps-pension+auxTrasnporte
            print(f"{nomina[k]['nombre']}, {k} , {nomina[k]['horas']}, {nomina[k]['valor']} ", salarioTotal)
        else:
            salarioTotal=salarioBruto-eps-pension
            print(f"{nomina[k]['nombre']}, {k} , {nomina[k]['horas']}, {nomina[k]['valor']} ", salarioTotal)
    if k==4:
        print("\n 1.Desea seguir consultado? .\n 2. Salir, No desea consultar mas")
        while True:
            op= leerIntm("\n Ingrese una opcion")
            if op ==1 or op == 2:
                if op==1:
                    continue
                else:
                    break



#MENU
while True:
    opcion= menu()
    if opcion==1:
        addEmpleado()

    elif opcion==2:
        modEmpleado()

    elif opcion==3:
        busEmpleado()
    
    elif opcion==4:
        delEmpleado()
    
    elif opcion==5:
        listEmpleado()
    
    elif opcion==6:
        listNom()
    
    elif opcion==7:
        listAllNom()
    
    elif opcion==8:
        print(" Gracias por utilizar nuestro Sofware Nomina")
        break
    else:
        msgError("Opcion Invalida. ")

print(nomina)



            



