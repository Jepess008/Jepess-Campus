def calNotaDef():
    notaFInal= nota1*0.3 + nota2*0.3 + nota3*0.4
    return notaFInal

estudiantes={}
while True:
    codigo= int(input("Ingrese EL Codigo del estudiante: "))
    nombre= input("Ingrese el nombre del estudiante: ")
    nota1= float(input("Ingrese la nota 1 del estudiante:  "))
    nota2= float(input("Ingrese la nota 2 del estudiante:  "))
    nota3= float(input("Ingrese la nota 2 del estudiante:  "))
    estudiantes[codigo] = {}
    estudiantes[codigo]["nombre"]=nombre
    estudiantes[codigo]["nota1"]= nota1
    estudiantes[codigo]["nota2"]= nota2
    estudiantes[codigo]["nota3"]= nota3
    
    opc= input("Desea agregar otro estudiante \n 1. SI \n 999. NO")
    if opc== "999":
        break

print("\n\n *** INFORME ***")
print("=" *30)
for k in estudiantes.keys():
    n= calNotaDef()
    if n >=3 and n<= 5:
        print(estudiantes[k]["nombre"], f"nota final es: {n} El estudiante Aprobo la materia")
    else:
        print(estudiantes[k]["nombre"], f"nota final es: {n} El estudiante No Aprobo la materia")
print("=" *30)