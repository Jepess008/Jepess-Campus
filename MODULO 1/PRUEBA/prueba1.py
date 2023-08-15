valor= int(input("ingrese el valor del producto"))
cantidad= int(input("ingrese la cantidad de productos a comprar"))
IVA= 15/100
preVen= valor*cantidad
preBru= (preVen*IVA) + preVen
desc= preBru - (preBru*5/100) 

if preBru> 1000 :
    print(f" El valor a pagar es {desc} tiene descuento")

if preBru< 1000:
    print(f" El valor a pagar es {preBru}")