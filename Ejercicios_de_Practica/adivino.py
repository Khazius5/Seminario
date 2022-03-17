## Adivina adivinador....
import random
numero_aleatorio = random.randrange(100)
gane = False
print("Tenés 5 intentos para adivinar un entre 0 y 99")
intento = 1
veces = 5
while intento < 6 and not gane:
    numero_ingresado = int(input('Ingresa tu número: '))
    veces-=1
    if numero_ingresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(intento))
        gane = True
    else:
        intento += 1
        print('Mmmm ... No.. ese número no es... Seguí intentando. Te quedan ', veces, ' intentos ')
if not gane:
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))