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
            print("Error! . Ingrese una letra valida.", e.message)

vocales=[]

#PROGRAMA GENRAL
while True:
    letra = leerString("Ingrese una letra: ")
    letra.lower()
    vocales.append(letra)
    opc= int(input("Deseas ingresar otra letra. \n 1. SI \n 2. NO "))
    if opc==2:
        break



a=vocales.count("a")
print("la cantidad de 'a' son", a)
e=vocales.count("e")
print("la cantidad de 'e' son", e)
i=vocales.count("i")
print("la cantidad de 'i' son", i)
o=vocales.count("o")
print("la cantidad de 'o' son", o)
u=vocales.count("u")
print("la cantidad de 'u' son", u)