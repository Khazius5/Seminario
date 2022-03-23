# Necesitamos procesar las notas de los estudiantes de este curso. Queremos saber:
#       • cuál es el promedio de las notas;
#       • cuántos estudiantes están por debajo del promedio.

def Lectura_Alumnos():
    """Lectura de Alumnos HASTA que se ingrese -1"""
    dic = {}
    al = input("Ingrese el Legajo del Alumno: \n")
    while (al != "-1"):
        nota = int(input("Ingrese la nota numerica de \n".format(al)))
        dic[al] = nota
        al = input("Ingrese el Legajo del Alumno: \n")
    return dic

def Recorrido(dic):
    """Recorre el diccionario"""
    for elem in dic:
        print(elem)
        print(dic[elem])

def Sacar_Promedio(dic):
    notas = dic.values()
    suma = 0
    for x in notas:
        suma+= x
    #Una vez hecha la suma de todas las notas, procedemos a calcular el promedio    
    prom = suma / len(notas)
    return prom

def Alumnos_Debajo(prom,dic):
    cantidad = 0
    notas_al = dic.values()
    for n in notas_al:
        if (n < prom):
            cantidad+= 1
    return cantidad

alumnos_seminario = Lectura_Alumnos()
promedio = Sacar_Promedio(alumnos_seminario)


print("El promedio entre los alumnos es de: " , promedio)
print("La cantidad de alumnos que tienen nota por debajo del promedio son: ", Alumnos_Debajo(promedio,alumnos_seminario))