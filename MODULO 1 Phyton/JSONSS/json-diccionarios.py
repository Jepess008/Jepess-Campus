# CREAR ARCHIVO JSON CON UNA ESTRUCTURA DE DATOS DICCIONARIO

import json

midic = {1:"Lapiz", 2:"Borrador", 3:"Cuaderno", 4:"Lapiciero", "valor": 2500}
midic2 = {
    "Influencers":[
        {
            "name": "Jaxon",
            "edad": 42,
            "work at": "Tech News"
        },
        {
            "name": "Miller",
            "edad": 35,
            "work at": "It days"
        }
    ]
    
}
with open("MODULO 1/JSONSS/diccionario.json", "w") as archivo:
    #json.dump(midic,archivo)
    json.dump(midic2,archivo)

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

    