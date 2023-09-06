# numero perfecto lo consigo con los divisores exactos = 0 y que sumados me den ese mismo número

# n= int(input("ingrese el número a evaluar"))
# a= 1
# acumulador= 0
# while(a<n):
#     if n%a==0:
#         acumulador= acumulador+a
#     a=a+1

# if acumulador == n:
#     print(f"El número {n} es perfecto ':D'")

# else:
#     print(f"El número {n} No es perfecto ':D'")


# n = 0
# while n>=0:
#     n= int(input("ingrese un número \n"))
#     if n <0:
#         break
#     contador=0
#     for i in range(1,n+1):
#         if n%i ==0:
#             contador += 1

#     if contador==2:
#         print(f"el número {n} es un número primo")     

#     else:
#         print(f"el número {n} no es un número primo")        
    
#     contador==0

#     n= int(input("ingrese un número \n"))

n=0
mayor=0
menor=float("inf")

while n>=0:
    n=int(input("ingrese un #"))
    if n<0:
        break
        print("NO ES POSIBLE EVALUAR ESTE #")
    contador= 0

    for i in range(9):
        
        if i>mayor:
            mayor=i
        if i<menor:
            menor=i
    print(f"el # mayor es {mayor} el # menor es {menor}")        

    contador=0



