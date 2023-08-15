# # ejemplo con un argumento
# for i in range(5):
#     print(i, end=', ')

# # ejemplo con dos argumentos
# for i in range(-1, 5):
#     print(i, end=", ")

# ejemplo con 3 argumentos .... el primer numero me indica desde donde inicia el ciclo, el segundo me indica hasta donde debe llegar (limite) y el ultimo indica la cantidad de saltos que va dar durante el ciclo
# for i in range(-1, 5, 2):
#     print(i, end=", ")

# for i in range(5, 1, -2):
#     print(i , end=", ")

# EJERCICIO 1
# IMPRIMIR LOS NUMEROS PARA QUE HAY DE 1 A 100

# for par in range(2, 101, 2):
#     print(par, end=", ")

# EJERCICIO 2
# HACER UN PROGRAMA QUE CALCULO EL FACTORIAL DE UN NUMERO.

# n= int(input("digitar el valor del número"))
# factorial = 1
# for i in range(1, n+1):
#     factorial= factorial * i

# print(f"EL factorial de {n} es: {factorial}")
    
#EJERCICIO 3
# DETERMINAR ES IMPRIMIR SI UN NUMERO ES PRIMO O NO

n = int(input("ingrese el número"))

primo=True
culpable= 0
for i in range(2,n):
    if n % i ==0:
        primo = False
        culpable = i
if primo:
    print("el número No es primo")

else:
    print("el número es primo", culpable)