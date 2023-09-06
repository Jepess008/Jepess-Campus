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
            n= int(input(msg))
            return n
        except ValueError:
            print("Error! . Ingrese un número entero valido.")

def msgError(msg):
    print=("Invalido................................" , msg)   
    input("------------> Presione la tecla para continuar")  


def menu():
    while True:
        print("\n*****")
        print(" MENU ")
        print("******\n")
        print("1. Agregar un empelado")
        print("2. Modificar empleado")
        print("3. Buscar empleado")
        print("4. Eliminar empleado")
        print("5. Listar empleados")
        print("6. Listar nomina de un empleado")
        print("7. Listar nomina de todos los empleados")
        print("8. Salir")
        op= leerInt("\n>> Opción(1 a 8)? ")
        if op < 1 or op > 8:
            msgError("Opcion no valida")
            continue
        return op
    
empleados={}
while True:
    op=menu()
    if op==1:   
        while True:
                documento = int(input("Ingrese el documento del empleado"))
                name=input("Ingrese nombre del empleado")
                horas= int(input("Ingrese la cantidad de horas trabajadas; recuerde que debe estar en el rango de horas permitidas de 1 a 160"))
                valorHora= int(input("Ingrese el valor de la hora trabajada; recuerde que debe estar en el rango de $8000 y 150000\n: "))
                empleados[documento]={}
                empleados[documento]["nombre"]= name
                empleados[documento]["horas"]=horas
                empleados[documento]["valorHora"]=valorHora
                opc= int(input("Desea ingresar otro empleado? \n 1. SI \n 2. NO"))
                if opc==2:
                    break
    elif op==2:
        while True:
            buscDoc= int(input(" Ingrese el documento del empleado a modificar: "))
            for k in empleados.keys():
              if k == documento:
                print(" se encontro el empleado en la posicion")
                break
              else:
                print(" Usuario no encontrado, digite de nuevo: ")       
    print(" Que deseas modificar? \n 1. Nombre \n 2.Horas trabajadas \n 3.Valor de la hora ")
    while True:
        op= leerIntm("\n Ingrese una opcion")
        if op >=1 or op <= 3:
            if op==1:
                newNombre=input("Ingrese el nuevo nombre: ")
                empleados[documento]["nombre"]= newNombre
                print("El cambio de nombre fue exitoso")
            elif op==2:
                newHoras= int(input("Ingrese las nuevas horas: "))
                empleados [documento] ["horas"]= newHoras
                print("Las horas fueron modificadas con exito")
            elif op==3:
                newValor= int(input("Ingrese el nuevo valor:  "))
                empleados[documento]["valorHora"]= newValor
                print("El valor fue modificado")
            break
        else:
            print("Digite un nùmero de acuerdo a las opciones presentadas")
    