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
   #colegio=cargarInfo()
   while True:
        grado=#leerString("Ingrese el grado del estudiante: ")
        if grado in #colegio:
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
