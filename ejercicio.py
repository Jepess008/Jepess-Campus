segundos = float(input("ingrese el número de segundos"))
hora= segundos// 3600
minutos = (segundos % 3600) // 60
segundos = (segundos % 3600 ) % 60 
print(f"Hora = {hora}")
print(f"Minutos = {minutos}")
print(f"Segundos = {segundos}")



# 1 hora = 3600 segundo
# 1 minuto = 60 segundos