a=float(input("ingrese el lado a"))
b=float(input("ingrese el lado b"))
c=float(input("ingrese el lado c"))
p=(a+b+c)/2

if p>a and p>b and p>c:
    area= (p*(p-a) * (p-b) * (p-c))**0.5
    print(f" El area del triangulo es = {area}")
else:
    print("error al ingresar los datos")    


#elevar un número a 0,5 para sacar la raiz cuadrada