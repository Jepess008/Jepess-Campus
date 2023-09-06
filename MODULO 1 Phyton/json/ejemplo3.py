import json

with open("MODULO 1/json/Ahorradores.json", "r") as archivo:
    ahorradores= json.load(archivo)

contador= 1
dian=[]

for cuenta in ahorradores["cliente"]:
    if cuenta["Saldo"]> 35000000:
        dian.append({
            "Consecutivo":contador,
            "NumCuenta":cuenta["NumCuenta"],
            "Saldo": cuenta["Saldo"]
        })
    contador += 1

with open("Dian.json", "w") as archivo:
    json.dump(dian,archivo,indent=4)

