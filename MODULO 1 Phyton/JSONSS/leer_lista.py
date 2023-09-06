# LEER UN ARCHIVO JSON PARA RECUPERAR LA ESTRUCTURA DE DATOS LISTA

import json

with open("MODULO 1/JSONSS/lista.json", "r") as archivo:
    lista=json.load(archivo)

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

for elem in lista:
    print(elem, end=", ")