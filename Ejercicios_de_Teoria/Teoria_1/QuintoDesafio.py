#Dadas dos cadenas ingresadas desde el teclado, imprimir aquella que tenga más caracteres

cadena1 = input("Ingrese la primer cadena de caracteres")
print()
cadena2 = input("Ingrese la segunda cadena de caracteres")
print()

if (len(cadena1) > len(cadena2)):
    print("La cadena mas extensa es: ", cadena1)
else:
    print("La cadena mas extensa es: ", cadena2)
