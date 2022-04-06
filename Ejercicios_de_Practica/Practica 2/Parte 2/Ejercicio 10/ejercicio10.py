# Trabajando con los contenidos de los archivos que pueden acceder en el curso:
# Manipule estos archivos para realizar lo siguiente:
#   • Generar una estructura con los nombres de los estudiantes y la suma de ambas notas.
#   • Calcular el promedio de las notas totales e informar que alumnos obtuvieron menos que el promedio

arch_notas1 = open('eval1.txt' , mode="r" , encoding="UTF-8")
arch_notas2 = open('eval2.txt', mode="r" , encoding="UTF-8")
arc_nombres = open('nombres_1.txt', mode="r" , encoding="UTF-8")


notas1 = arch_notas1.read().split(",")
notas2 = arch_notas2.read().split(",")
nombres = arc_nombres.read().replace(" ", "").split()

alumnos = []
nota_total= 0

for nombre, nota1 , nota2 in zip(nombres,notas1, notas2):
    alumno = {"nombre":nombre , "nota": (int (nota1) + int (nota2))}
    alumnos.append(alumno)
    nota_total += alumno["nota"]

promedio = nota_total / len(nombres)
promedio = round(promedio , 1)

for alumno in alumnos:
    if (alumno["nota"] < promedio):
        print(alumno)



arch_notas1.close()
arc_nombres.close()
arch_notas2.close()

for alumno in alumnos: 
    print(alumno)
    print("-"*10)
