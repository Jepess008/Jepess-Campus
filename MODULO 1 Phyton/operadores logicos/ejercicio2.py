hora= int(input("Ingrese la hora en su formato"))
minutos= int(input("Ingrese los minutos en su formato"))
segundos= int(input("Ingrese los segundo en su formato"))
horario= input("Horario 'AM' O 'PM'")

if hora == 12 and horario == "AM":
    print(f"la hora militar es {0} : {minutos} : {segundos}")
elif hora == 12 and horario == "PM":
    print(f"la hora militar es {hora} : {minutos} : {segundos}")
elif horario == "AM":
    hora= hora
    print( f"la hora militar es {hora} : {minutos} : {segundos}")
elif horario == "PM":
    hora= hora + 12 
    print(f"la hora militar es {hora} {minutos} {segundos}")
