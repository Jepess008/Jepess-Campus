import json

data= {}
data["clientes"]=[]

data["clientes"].append({
    "first_name": "Theodoric",
    "last_name": "Rivers",
    "age": 36,
    "amount": 1.11
})

with open("data.json", "w") as archivo:
    json.dump(data,archivo,indent=4)

print(data)