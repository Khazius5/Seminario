#Dada una frase y un string ingresados por teclado (en ese orden), e informe la cantidad de
#veces que se encuentra el string en la frase. No distingir entre mayúsculas y minúsculas

frase = input("Ingrese la frase a evaluar: \n")
word = input("Ingrese lo que quiera buscar dentro de la frase: \n")

frase = frase.lower()
word = word.lower()
cont = frase.count(word)
print(f"Las veces que aparece {word} en la frase son: {cont}")


## Parte 2 ## 

#Retomamos el código visto en la teoría, que informaba si los caracteres “@” o “!” formaban
#parte de una palabra ingresada

cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !): \n")

if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
elif map(lambda c: c in cadena, ("@" or "!")):
    print("Ingresaste alguno de estos símbolos: @ o !")
else:
    print("Clave válida")
