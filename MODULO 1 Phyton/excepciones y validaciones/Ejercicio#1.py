"""Adivina el número: Crea un programa en el que la computadora "piense" un número secreto entre 1 y
100, y el usuario tenga que adivinarlo. El programa debe proporcionar pistas como "Demasiado bajo"
o "Demasiado alto" hasta que el usuario adivine correctamente.
El usuario que gana es el que adivine en el menor número de intentos.
Este programa se hizo en clase. Para el software review modifícalo para que el usuario tenga un limite
de 3 a 5 intentos (escoja un número al azar entre [3, 5]. Cada usuario puede tener un número de intentos
distinto) para adivinar el número."""

import random

conIntentos=0
entrar = True
validar = True
ganador = ""
intGanador = float("inf")
nombre=""
numAl=0
intentos=0
#juego
while conIntentos>0:
     
    while entrar == True:

        while validar == True:
        
            try:
                num=int(input("Ingrese un número de 1 -100"))
                if num >=0 and num <= 100:
                    validar = False 
                
            except ValueError:
                print("Ingrese un número, no es valido caracteres o letras")

        if num == numAl:
            print("GANASTE")
            if conIntentos < intGanador:
                intGanador = conIntentos
                ganador = nombre
                entrar=False

        elif num != numAl:
            conIntentos +=1
            intentos -= 1

            if numAl < num:
                print("El numero es mayor al ...")
            else:
                print("El numero es menor al ...")
            print(f"Tienes la siguiente cantidad de intentos {intentos}")

        



        
