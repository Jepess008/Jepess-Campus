# Leer un archivo json para recuperar la estructura de datos diccionarios

import json

with open("MODULO 1/JSONSS/diccionario.json", "r") as archivo:
    midic2= json.load(archivo)

if not archivo.closed:
    print("cerrando el archivo")
    archivo.close()

print("Diccionario: ", midic2)
print("Diccioanrio: ", midic2["Influencers"][1]["name"])