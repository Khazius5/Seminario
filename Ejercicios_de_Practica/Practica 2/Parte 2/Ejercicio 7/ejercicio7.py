# Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la
# misma es un Heterograma (tenga en cuenta que el contenido del enlace es una traducción del
# inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma
# es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres

frase = input("Ingrese la frase: \n")

f1 = list(frase)
f2 = set(f1)

if (len(f1) == len(f2)):
    print("La frase es Heterograma")
else: 
    print("La frase no es Heterograma")