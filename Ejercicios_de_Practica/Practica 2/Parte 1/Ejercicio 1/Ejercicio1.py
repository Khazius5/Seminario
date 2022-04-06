text = open("C:\\Python Github\\Seminario\\Ejercicios_de_Practica\\Practica 2\\Ejercicio 1\\readme.txt")

with text as file:
    c = [line for line in file.readlines() if ("http" or "https") in line]
    print(c)