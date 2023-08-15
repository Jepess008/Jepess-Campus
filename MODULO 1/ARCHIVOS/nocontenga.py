import io

fd = open("MODULO 1/ARCHIVOS/mbox-short.txt", "r", encoding="utf-8")
contador=0
for linea in fd:
    if  "Subject" in linea:
        contador += 1
fd.close()

print("El número de líneas que contienen la palabra Subject es: ", contador) 