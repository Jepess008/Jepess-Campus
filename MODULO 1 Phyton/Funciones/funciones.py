#Sintaxis general
"""def nombre_funcion([parama1, param2, ....., param 4]): #puedo tener parametros vacios o varios parametros #los corchetes me informan que las varibles son opciones
    cuerpo_funcion
"""
def leerInt(msg):
    while True:
        try:
            n= int(input(msg))
            return n
        except ValueError:
            print("Error! . INgrese un número entoero valido.")

#Funcion que sume 2 numeros
def sumar(num1, num2):
    s=num1+num2
    return s

a= leerInt("Ingrese un número")
b= leerInt("Ingrese otro número")
print("El resultado de la suma es:", sumar(a,b))
