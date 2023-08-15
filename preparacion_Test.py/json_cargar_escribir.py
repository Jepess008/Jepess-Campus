import json

def actualizar_data(dicdata):
    with open(ruta, "w") as f:
        json.dump(dicdata, f)

def cargarInfo():
    fd= open(ruta, "a+")
    fd.seek(0)
    #verificar si tengo datos
    dic={}
    try:
        dic=json.load(fd)
    except Exception as e:
        dic={}
    fd.close()
    return dic


ruta = "Jepess Campus/MODULO 1/sofware review/InstitutoAcme.json"