hangmanStages = ['''
  +---+
  |   |
      1
      /
      6
      |
=========''', '''
  +---+
  |   |
  O   2
      /
      6
      |
=========''', '''
  +---+
  |   |
  O   3
  |   /
      6
      |
=========''', '''
  +---+
  |   |
  O   4
 /|   /
      6
      |
=========''', '''
  +---+
  |   |
  O   5
 /|\  /
      6
      |
=========''', '''
  +---+
  |   |
  O   6
 /|\  /
 /    6
      |
=========''', '''
  +---+
  |   |
  O   D
 /|\  E
 / \  A
      D
=========''', '''
  +---+
  |   |
      W
  O   I
 /|\  N
 / \  |
=========''']

guessWord = input("Enter a word to guess, alternatively enter 'X' to have a random word chosen for you: " )

def dashWord(word):
    wordLength = len(guessWord)
    dashedWord = "_ " * wordLength
    return dashedWord

turn = 0
stage = 0

while turn < 7 :
    print(hangmanStages[stage])
    print("Word: ", dashWord(guessWord))
    wordGuess = input("Guess a word: ")
    if wordGuess == guessWord:
        print(hangmanStages[7]) # stage 7 is the frame where you win, the program stops at 6 by default
        break
    else:
        turn += 1
        stage += 1

    




