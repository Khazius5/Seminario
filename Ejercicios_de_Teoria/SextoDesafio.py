#Escribir un programa que ingrese desde teclado una cadena de caracteres e imprima cuántas
#letras “a” contiene.

cont = 0
cadena = input("Ingrese una cadena de carcateres")
for car in cadena:
    if (car == "a"):
        cont = cont + 1
print("---------------------------")
print(cont)