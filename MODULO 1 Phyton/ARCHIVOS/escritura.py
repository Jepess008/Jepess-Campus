fd = open("MODULO 1/ARCHIVOS/prueba2.txt", "w")
lst =["Primer Linea\n" , "Segunda Linea\n"]
fd.writelines(lst)
fd.close()
