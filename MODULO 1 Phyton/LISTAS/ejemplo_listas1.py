def buscarElem(lst,elem):
    for i in range(len(lst)):
        if lst[i] == elem:
            return i
    return -1

def encontrarElem(lst,elem ):
    for e in lst:
        if e == elem:
            return True
    return False


miLista=[]
miLista=list()
print(miLista,len(miLista))

miLista.append("Alirio")
print (miLista, len(miLista))
print(miLista[0:1])

miLista.extend(["Andres", "Carlos", "Cristian", "Diana"])
print(miLista,len(miLista))

miLista.pop()
print(miLista, len(miLista))

miLista.insert(2,"Lilian")
print(miLista,len(miLista))

miLista.remove("Carlos")
print(miLista, len(miLista))

#OPERACIONES DE LISTA

# COMO RECORRO LA LISTA
#  RECORRIDO POR INDICE
for pos in range(len(miLista)):
    print(pos,"----->", miLista[pos])

#  RECORRIDO POR ELEMENTO
print("="*30)
for elem in miLista:
    print(elem)

#  BUSCAR UN ELEMENTO, SI ESTA, DEVULVE LA POSICION Y SI NO DEVUELVE -1

pos=buscarElem(miLista, "Carlos")
print(pos)

pos=buscarElem(miLista, "Andres")
print(pos)

#  BUSCAR UN ELEMENTO EN LA LISTA. SI ESTA, DEVULVE TRUE Y SI NO DEVUELVE FALSE
esta= encontrarElem(miLista, "Andres")
print(esta)

