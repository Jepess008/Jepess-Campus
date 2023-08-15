import io

#abrirlo
fd = open("MODULO 1/ARCHIVOS/texto.txt", "r")
fd.seek(52)
#leer= fd.read()
leer2= fd.readline(6)
leer3= fd.readlines()

fd.close()

print(leer2.rstrip(), end="*")
print(leer3)