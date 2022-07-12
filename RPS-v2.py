import random

#Dashed line for easy viewing
d = "-----------------------------------"
# All possible choises for the PC and the system to make it choose one answer at random
possible_choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_choices)

print(d)

# System how user chooses
user_choice = input("Choose! (rock, paper or scissors): ")

print(d)

# Printing user and PC choice for troubleshooting
print("You chose: ", user_choice)
print("The computer chose: ", computer_choice)

# Scoreboard
compScore = 0
userScore = 0

# Function to calculate who won
def winningCalc(A, B):
    pc = 0
    user = 0
    if A == "rock" and B == "scissors":
        pc += 1
        print("The computer won, as rock beats scissors")
    if A == "paper" and B == "rock":
        pc += 1
        print("The computer won, as paper beats rock")
    if A == "scissors" and B == "paper":
        pc += 1
        print("The computer won, as scissors beats paper")
    if A == "scissors" and B == "rock":
        user += 1
        print("You won, as rock beats scissors")
    if A == "rock" and B == "paper":
        user += 1
        print("You won, as paper beats rock")
    if A == "paper" and B == "scissors":
        user += 1
        print("You won, as scissors beats paper")
    if A == B:
        print("you tied")
# Print a dash 
    print(d)
# Show current score
    compScore = pc
    userScore = user
    print("Your score: ", userScore)
    print("Computer's score: ", compScore)


# GAME STARTS HERE

winningCalc(user_choice, computer_choice)

print(d)

play = 0
pplay = input("Keep playing? (y/n): ")
if pplay == "y":
    play = 0
if pplay == "n":
    play = 1

while play == 0:
    print ("-------N-E-W---G-A-M-E-------")
    user_choice = ""
    user_choice = input("Choose! (rock, paper or scissors): ")
    computer_choice = ""
    computer_choice = random.choice(possible_choices)
    print(d)
    print("You chose: ", user_choice)
    print("The computer chose: ", computer_choice)
    print(d)
    winningCalc(user_choice, computer_choice)
    play = 0
    pplay = input("Keep playing? (y/n): ")
    if pplay == "y":
     play = 0
    if pplay == "n":
     play = 1

if play == 1:
    print("I hope you enjoyed")

print(d)

# ISSUES: game does not save leaderboard date when entering a new game
# while loop is messy and can likely be compacted, i think turning more things into functions
