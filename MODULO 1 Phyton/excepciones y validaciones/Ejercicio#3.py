contador=0
num=0
frase= input("Ingrese la frase")

while num < len(frase):
    letra= frase[num]. lower()
    if letra == "q":
        break
    elif letra in "aeiou":
        contador += 1
    num += 1
print(f"la cantidad todal de vocales es {contador}")

