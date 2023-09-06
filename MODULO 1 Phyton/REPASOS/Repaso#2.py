#Ejercicio Dado el nombre y estrato(1,2,3,4,5)de un usuario del servicio de energía eléctrica, calcular lo que pagaría de tarifa básica del servicio de energía eléctrica,
#que depende del estrato,así:
#Estrato    TarifaBásica
#1           $10.000
#2           $15.000
#3           $30.000
#4           $50.000
#5           $65.000
#Se pide visualizar el nombre y tarifa básica

def leerInt(msg):
    while True:
        try:
            n= int(input(msg))
            if n<1 or n>5:
                print("Error!! ingrese un estrato valido (1 a 5).")
                print("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! . Ingrese un número entero valido.")

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

def calTarifaBasica(est):
    if est==1:
        return 10_000
    elif est==2:
        return 15_000
    elif est==3:
        return 30_000
    elif est==4:
        return 50_000
    else:
        est==5
        return 65_000
    


#programa general
nombre= leerString("Ingrese el nombre: ")
estrato= leerInt("Ingrese el estrato del Usuario: ")

tarifaBasica= calTarifaBasica(estrato)

print(10*"\n-")
print(f"El valor a pagar del Sr. {nombre} es de {tarifaBasica}")