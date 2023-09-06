nombre= input("Ingrese su nombre")
salario= int(input("Ingrese el salario"))

subTrans= 0
if salario <= 1200000:
    subTrans=120000
else:
    subTrans = 0

print("/n","-"*30)
print("Nombre:", nombre)
print("Salario",salario)
print("Subsidio:", subTrans)
print("-"*30, "\n")