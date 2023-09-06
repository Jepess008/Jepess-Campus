import io

fd = open("MODULO 1/ARCHIVOS/mbox-short.txt", "r", encoding="utf-8")
contador=0
for linea in fd:
    contador += 1

fd.close()

print("cantidad de líneas: ", contador)