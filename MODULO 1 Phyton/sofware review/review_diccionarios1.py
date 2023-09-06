#! /usr/bin/env python3
"""Se realiza la compra de N artí culos, en donde se ingresa el co digo del artí culo y la cantidad y mediante el uso
de diccionarios para los nombres y valores unitarios de los artí culos, el programa debe obtener el nombre
de cada artí culo, cantidad comprada, valor unitario, valor total de acuerdo con la cantidad comprada y
finalmente calcular el valor total de la compra.
Se suministra el diccionario de nombres de artí culo y otro con los valores unitarios."""


articulos = {1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
valores = {1:2500,2:3800,3:1200,4:35000,5:3700}
compra={}
total=0

while True:
    codigo= int(input("Ingrese el codigo del articulo\n 1. Lapiz \n 2. Cuadernos \n 3. Borrador \n 4. Calculadora \n 5. Escuadra\n :----> "))
    if codigo >=1 or codigo <=5:
        compra[codigo]={}
        compra[codigo]["articulo"]=articulos
        compra[codigo]["valor"]= valores
    else:
        print("Ingrese un codigo valido")

    cantidad= input("Ingrese la cantidad de articulos a comprar: ")
    
    opc= input("Desea agregar otro articulo? \n 1. SI \n NO")
    if opc== "NO":
        break


print("\n\n *** INFORME ***")
print("=" *30)
for k in compra.keys():
    h= cantidad * compra[valores[k]["valor"]]
    total += h
    print(" El articulo" + compra[k]["articulo"])
    print("=" *30)
    print("Con valor por unidad de :" + compra[k]["valor"])
    print("=" *30)
    print("Con un precio total del articulo de :" + k)
    print("=" *30)
    print("Con un valor total de factura de :" + total)
    print("=" *30)