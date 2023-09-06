def leerInt(msg):
    while True:
        try:
            n= int(input(msg))
            if n<1 or n==0:
                print("Error!! ingrese un codigo valido, este no puede ser negativo ni 0")
                print("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! . Ingrese un número entero valido de codigo.")

def leerString(msg):
    while True:
        try:
            n= input(msg)
            if n.strip() == "":
                print("Error!! ingrese un nombre valido.")
                print("Digite cualquier tecla para continuar...")
                continue
            return n
        except Exception as e:
            print("Error! . Ingrese un nombre valido.", e.message)

def leerProgAcademico():
    print("Seleccione el programa Academico al cual pertenece")
    print("1: Técnico en Sistemas")
    print("2: Técnico en Desarrollo de video juegos")
    print("3: Técnico en Animación Digital")
    if progAca<0 or progAca>4:
        if progAca ==1:
            return 800_000
        elif progAca==2:
            return 1_000_000
        elif progAca==3:
            return 1_200_000
    else:
        print("Error!!!!-----Ingrese un # de acuerdo a la lista del programa")
def leerIndBeca():
    print("Seleccione la beca por rendimiento academico.")
    print("1: Beca por rendimiento academico. Descuento del 50 porciento sobre el valor de la matricula")
    print("2: Beca cultural- Deportes. Descuento del 40 porciento sobre el valor de la matricula")
    print("3: Sin Beca")
    if beca<0 or beca>4:
        if beca ==1:
            return 0.5
        elif beca==2:
            return 0.4
        elif beca==3:
            return 1
    else:
        print("Error!!!!-----Ingrese un # de acuerdo a la lista del programa")

def calMatricula():
    valorNeto= progAca + (progAca*beca)
    return valorNeto



# Programa general
cod= leerInt("Ingrese el codigo del estudiante: ")
nom= leerString("Ingrese el nombre del estudiante: ")
progAca=leerProgAcademico("Ingrese el programa al que pertenece el estudiante")
beca= leerIndBeca()
valorNeto= calMatricula(progAca, beca)
print("\n", "-"*40)
print("Estudiante: ", nom)
print(f"El valor neto a pagar es: f{valorNeto:,.0f}")