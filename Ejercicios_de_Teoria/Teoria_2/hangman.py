import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
words = 'python arbol abeja casa perro madera tetera gato cerdo celular tarjeta procesador escuela lapiz auto programacion software sistemas archivos '.split()

def getRandomWord(word_List):
    """Esta funcion retorna una palabra random de las anterior mencionadas"""
    word_Index = random.randint(0, len(word_List) - 1)
    return word_List[word_Index]

def displayBoard(missed_Letters, correct_Letters, secret_Word, add_Letter):
    print(HANGMAN_PICS[len(missed_Letters)])
    print()
    if (len(secret_Word) > 5):
        print("Aqui una ayuda! Esta palabra contiene la letra: ", add_Letter)
        print()
    print('Letras incorrectas:', end=' ')
    for letter in missed_Letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_Word)

    for i in range(len(secret_Word)): # Reemplaza los espacios en blancos por la letra correcta
        if secret_Word[i] in correct_Letters:
            blanks = blanks[:i] + secret_Word[i] + blanks[i+1:]

    for letter in blanks: # Muestra la palabra secreta con espacios 
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    """Funcion para leer una letra"""
    while True:
        print('Adivina una letra.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Por favor inserta una sola letra.')
        elif guess in alreadyGuessed:
            print('Ya ingresaste esta letra, ingrese otra.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return guess

def playAgain():
    """Esta funcion retorna verdadero si el jugador desea volver a jugar"""
    print('¿Quieres jugar de nuevo? (si o no)')
    return input().lower().startswith('s')

def Help(word_List):
    if len(word_List) > 5: 
        Additional_Letter = word_List[0]
    else:
        Additional_Letter = " "
    return Additional_Letter


print('A H O R C A D O')
missed_Letters = ''
correct_Letters = ''
secret_Word = getRandomWord(words)
Help_Letter = Help(secret_Word)
game_Over = False

while True:
    displayBoard(missed_Letters, correct_Letters, secret_Word, Help_Letter)

    #Llamar a la funcion que nos hace leer una letra 
    guess = getGuess(missed_Letters + correct_Letters)

    if guess in secret_Word:
        correct_Letters = correct_Letters + guess

        # Verifica si el jugador gano.
        found_All = True
        for i in range(len(secret_Word)):
            if secret_Word[i] not in correct_Letters:
                found_All = False
                break
        if found_All:
            print('Si! La palabra secreta es "' + secret_Word + '"! Ganaste!')
            game_Over = True
    else:
        missed_Letters = missed_Letters + guess

        # Hace un check sobre si el jugador se quedó sin intentos.
        if len(missed_Letters) == len(HANGMAN_PICS) - 1:
            displayBoard(missed_Letters, correct_Letters, secret_Word)
            print('Te quedaste sin intentos !\n Despues de ' + str(len(missed_Letters)) + ' intentos fallidos y ' + str(len(correct_Letters)) + ' letras correctas, la palabra era "' + secret_Word + '"')
            game_Over = True

    # Pregunta al jugador si quiere volver a jugar solo si el juego terminó.
    if game_Over:
        if playAgain():
            missed_Letters = ''
            correct_Letters = ''
            game_Over = False
            secret_Word = getRandomWord(words)
            Help_Letter = Help(secret_Word)
        else:
            break