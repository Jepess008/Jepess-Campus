import json
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

def actualizar_data(dicdata):
    with open(ruta, "w") as f:
        json.dump(dicdata, f)


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

def menuEst():
    print("-"*40)
    print("Bienvenido al apartado Estudiantes acontinuacion presentamos las opciones:\n MENU")
    print("-"*40)
    print("1.Agregar Estudiante")
    print("2.Modificar Estudiantes")
    print("3.Eliminar Estudiante")
    print("4.Buscar Estudiante")
    print("5.Salir")
    print("-"*40)
    opcion= leerInt("Ingrese una opcion de acuerdo a lo que desea realizar:  ")
    if opcion<1 or opcion>5:
        msgError("OPCION NO VALIDA")
    return opcion

def menuReport():
    print("-"*40)
    print("Bienvenido al apartado de Reportes acontinuacion presentamos las opciones:\n MENU")
    print("-"*40)
    print("1.Listado de notas promedio por grado")
    print("2.Terna de excelencia por grado")
    print("3.Terna de excelencia del colegio ")
    print("-"*40)
    opcion= leerInt("Ingrese una opcion de acuerdo a lo que desea realizar:  ")
    if opcion<1 or opcion>3:
        msgError("OPCION NO VALIDA")
    return opcion

def ingNotas():
    notas=[]
    while True:
        nota=leerInt("Ingrese la nota del estudiante: ")
        notas.append(nota)
        op= leerInt("Desea ingresar otra nota? \n 1. SI \n 2. NO: ")
        if op==1:
            continue
        else:
            break
    return notas
    


def addEst():

    colegio= cargarInfo()
    while True:
        grado= leerString("Ingrese el grado al que pertenece el estudiante: ")
        if not (grado in colegio):
            colegio[grado]={}
        id= leerInt("Ingrese el codigo del estudiante a registrar: ")
        nombre= leerString("Ingrese el nombre del estudiante: ")
        sexo= leerString("Ingrese el sexo del estudiante Masculino = 'M' Femenino = 'F': ")
        colegio[grado][id]= {}
        colegio[grado][id]["nombre"]=nombre.upper()
        colegio[grado][id]["sexo"]= sexo.upper()
        actualizar_data(colegio)
        op=leerInt("Desea ingresar otro estudiante? \n 1. SI \n 2. NO")
        if op==1:
            continue
        else:
            break


def modEst():
    colegio=cargarInfo()
    while True:
        grado=leerString("Ingrese el grado del estudiante: ")
        if grado in colegio:
            break
        print("No existe el grado, Digita de nuevo")
    
    while True:
        busqidd= leerInt("Ingrese el id del estudiante que desea modificar")
        if str(busqidd) in colegio[grado]:
            print("Se encontro el estudiante ")
            print(busqidd)
            break   
        else:
            print("Usuario no encontrado: ") 
        print(busqidd)
    print(" Que deseas modificar? \n 1. Nombre \n 2.Sexo \n 3.Notas")

    op= leerInt("\n Ingrese una opcion")
    
    if  op<1 or op>3:
        print("Ingrese una opcion correcta")
    elif op==1:
        newNombre=leerString("Ingrese el nombre del estudiante: ")
        colegio[grado][str(busqidd)]["nombre"]= newNombre
        print("Cambio realizado")
    elif op==2:
        newSexo=input("Ingrese el Sexo del estudiante: ")
        colegio[grado][str(busqidd)]["sexo"]= newSexo
        print("El sexo del estudiante fue modificado con exito")
    elif op==3:
        newNotas= int(input("Ingrese el nuevo valor:  "))
        colegio[grado][str(busqidd)]["Notas"]= newNotas
        print("Las notas fueron modificadas")
    input("Presione cualquier tecla para volver al menu")

    actualizar_data(colegio)

def delEst():
    colegio=cargarInfo()
    while True:
        grado=leerString("Ingrese el grado del estudiante: ")
        if grado in colegio:
            break
        print("No existe el grado, Digita de nuevo")
    while True:
        busqidd= leerInt("Ingrese el idd del estudiante que desea eliminar")
        if str(busqidd) in colegio[grado]:
            colegio[grado].pop(str(busqidd))
            print("Usuario eliminado correctamente ")
            break   
        else:
            print("Usuario no encontrado: ")
    actualizar_data(colegio)   

def busEst():
   colegio=cargarInfo()
   while True:
        grado=leerString("Ingrese el grado del estudiante: ")
        if grado in colegio:
            break
        print("No existe el grado, Digita de nuevo")

   while True:
        busqidd= (input("Ingrese el documento que desea consultar"))
        if busqidd in colegio[grado]:
            print("Se encontro el usuario ")
            print(colegio[grado][str(busqidd)])
            break   
        else:
            print("Usuario no encontrado, El empleado no ha sido ingresado: ")
def estudiantes():

    opcion=menuEst()
    if opcion==1:
        addEst()
    
    elif opcion==2:
        modEst()

    elif opcion==3:
        delEst()

    elif opcion==4:
        busEst()
    
    elif opcion==5:
        print("saliendo")


def notas():
    colegio= cargarInfo()
    while True:
        grado=leerString("Ingrese el grado del estudiante: ")
        if grado in colegio:
            break
        print("No existe el grado, Digita de nuevo")

    estudiantes= []
    for y in colegio[grado].keys():
        nombre= colegio[grado][y]["nombre"]
        estudiantes.append(nombre) 
    estudiantes.sort()
    for x in range(len(estudiantes)):
        print(f"\nestudiante {estudiantes[x]}")
        nota= ingNotas()
        for z in colegio[grado].keys():
            if colegio[grado][z]["nombre"]== estudiantes[x]:
                id=z
                break
        colegio[grado][id]["notas"]= nota
        promedio= sum(nota)/len(nota)
        colegio[grado][id]["promedio"]= promedio 
        print(f"las notas de {estudiantes[x]} fueron : {nota}")
    actualizar_data(colegio)


def listGrado():
    colegio= cargarInfo()
    while True:
        grado=leerString("Ingrese el grado del estudiante: ")
        if grado in colegio:
            break
        print("No existe el grado, Digita de nuevo")
    print(f"Notas de los Estudiantes grado: {grado}")
    print("{:<14} {:<15} {:<20}".format("identificacion", "Estudiante", "promedio"))
    for x in colegio[grado].keys():
        id=x
        name = colegio[grado][x]["nombre"]
        promedio= colegio[grado][x]["promedio"]
        print("{:<14} {:<15} {:<20}".format(id,name, promedio))
    input("presione cualquier tecla para continuar")
    
    

def ternaGrado():
    colegio=cargarInfo()
    while True:
        grado=leerString("Ingrese el grado del estudiante: ")
        if grado in colegio:
            break
        print("No existe el grado, Digita de nuevo")
    
    mejores={}
    for x in colegio[grado].keys():
        name = colegio[grado][x]["nombre"]
        promedio= colegio[grado][x]["promedio"]
        mejores[name]=promedio
        print(mejores)
    mejores=dict(sorted(mejores.items(), key=lambda item:item[0]))
    print("{:<15} {:<20}".format(name, promedio))

def ternaColegio():
    pass

def reportes():
    opcion=menuReport()
    if opcion==1:
        listGrado()
    
    elif opcion==2:
        ternaGrado()

    elif opcion==3:
        ternaColegio()
    

def cargarInfo():
    fd= open(ruta, "a+")
    fd.seek(0)
    #verificar si tengo datos
    dic={}
    try:
        dic=json.load(fd)
    except Exception as e:
        dic={}
    fd.close()
    return dic


# PROGRAMA PRINCIPAL

ruta = "Jepess Campus/MODULO 1/sofware review/InstitutoAcme.json"

while True:
    op= menu()
    if op==1:
        estudiantes()
    elif op==2:
        notas()
    elif op==3:
        reportes()
    elif op==4:
        print("Gracias por usar SisNotACME")
        break
    
