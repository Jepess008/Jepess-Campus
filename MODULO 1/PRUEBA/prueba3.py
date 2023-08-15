"""Logotipo de Compay

Una marca multinacional de reciente apertura ha decidido basar su logo de empresa en los tres
caracteres más comunes en el nombre de la empresa. Ahora están probando varios
combinaciones de nombres de empresas y logotipos basados ​​en esta condición. Dada una cadena, que
es el nombre de la empresa en minúsculas, su tarea es encontrar las tres más comunes
caracteres en la cadena: 

Imprima los tres caracteres más comunes junto con el número de ocurrencias.
Ordenar en orden descendente de recuento de ocurrencias.
Si el recuento de ocurrencias es el mismo, ordene los caracteres en orden alfabético.


Por ejemplo, según las condiciones descritas anteriormente, GOOGLE tendría su logotipo
con las letras G, O, E.
Formato de entrada
Una sola línea de entrada que contiene la cadena S.
Restricciones
3 < largo(S) < 10^4
S tiene al menos 3 caracteres distintos
Formato de salida
Imprima los tres caracteres más comunes junto con su ocurrencia cuente cada uno en un
línea separada.
Ordene la salida en orden descendente de recuento de ocurrencias.
Si el recuento de ocurrencias es el mismo, ordene los caracteres en orden alfabético.
Entrada de muestra 0

aabbbccde

Salida de muestra 0

segundo 3
un 2
c 2

Explicación 0
aabbccde
Aquí, b ocurre 3 veces. Se imprime primero.
Tanto a como c ocurren 2 veces. Entonces, a se imprime en la segunda línea y c en la tercera línea porque
a viene antes de c en el alfabeto.
Nota: La cadena S tiene al menos 3 caracteres distintos."""


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

nombresEmpresa=[]

#PROGRAMA GENRAL
while True:
    nombre = leerString("Ingrese el nombre de la empresa: ")
    nombre.lower()
    nombresEmpresa.append(nombre)
    break

for indice in range(len(nombre)):
    caracter = nombre[indice]
    print("En el índice {} tenemos a '{}'".format(indice, caracter))












"""a=vocales.count("a")
print("la cantidad de 'a' son", a)
e=vocales.count("e")
print("la cantidad de 'e' son", e)
i=vocales.count("i")
print("la cantidad de 'i' son", i)
o=vocales.count("o")
print("la cantidad de 'o' son", o)
u=vocales.count("u")
print("la cantidad de 'u' son", u)"""