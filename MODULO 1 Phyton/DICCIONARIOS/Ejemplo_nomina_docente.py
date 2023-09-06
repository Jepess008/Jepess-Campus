diccionario_categoria={1:25000, 2: 30000, 3: 40000, 4: 45000, 5: 60000}

totalHonorarios= 0
docentes= {}
while True:
    cedula= int(input("Ingrese la cedula del docente: "))
    nombre= input("Ingrese el nombre del docente: ")
    categoria= int(input("Categoria del docente: "))
    horas= int(input("Ingrese el número de horas laboradas por el docente: "))
    docentes[cedula] = {}
    docentes[cedula]["nombre"]=nombre
    docentes[cedula]["categoria"]= categoria
    docentes[cedula]["horas"]= horas
    
    opc= input("Desea agregar otro docente (S/N)")
    if opc.lower()== "n":
        break

print("\n\n *** INFORME ***")
print("=" *30)
for k in docentes.keys():
    h= docentes[k]["horas"] * diccionario_categoria[docentes[k]["categoria"]]
    totalHonorarios += h
    print(docentes[k]["nombre"], f"----- $ {h:,}")
print("=" *30)
print(f"Total de los Honorarios de los docentes: ${totalHonorarios:,}")