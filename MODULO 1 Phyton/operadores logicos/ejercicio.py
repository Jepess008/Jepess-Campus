nombre= input("Ingrese el nombre del estudiante")
nota= int(input("Ingrese la nota cuantitativa del estudiante"))

if nota >= 0 and nota <60:
    print(f"nota del estudiante 'D' {nombre} {nota}")
elif nota >=60 and nota <79:
    print(f"nota del estudiante 'C' {nombre} {nota}")
elif nota >=80 and nota <89:
    print(f"nota del estudiante 'B'{nombre} {nota}")
elif nota>=90 and nota <=100:
    print(f"nota del estudiante 'A'{nombre} {nota}")
else:
    print("Inserte un valor en el rango de 0-100")    
