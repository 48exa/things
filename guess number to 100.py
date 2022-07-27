import random
import time

number = random.randint(1, 100)
allowednums = range(1,101)
win = False
round = ''
playGame = 'default'

def wait() :
    time.sleep(0.3)

print(number)
guess = input("Guess a number between 1 and 100.\n=> ")

def checkLoop():
    global win
    global guess
    global round
    global number
    while win == False:
        if guess < str(number):
            print("The number you guessed is below the correct value")
            wait()
            guess = input("Guess again: ")
        elif guess > str(number):
            print("The number you guessed is above the correct value")
            wait()
            guess = input("Guess again: ")
        elif guess == str(number):
            print("you guessed the right number! It was " + str(number))
            win = True
            round = 'complete'
            wait()
            
            
     
checkLoop()


if round == 'complete':
    playGame = input("Do you want to play again? y/n\n => ")

print(playGame)

if playGame == "y" or playGame == "Y":
    number = random.randint(1,100)
    print(number)
    guess = input("Guess a number between 1 and 100.\n=> ")
    round = ''
    win = False
    checkLoop()
            
if playGame == "n" or playGame == "N":
    win = True
    print("\nI hope you enjoyed!")
    input("Press enter to quit.")


