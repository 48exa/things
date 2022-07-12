import random

d = "-----------------------------------"
possible_choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_choices)
print(d)
user_choice = input("Choose! (rock, paper or scissors): ")
print(d)
print("You chose: ", user_choice)
print("The computer chose: ", computer_choice)
compScore = 0
userScore = 0

print(d)

if computer_choice == "rock" and user_choice == "scissors":
    compScore += 1
    print("The computer won, as rock beats scissors")
if computer_choice == "paper" and user_choice == "rock":
    compScore += 1
    print("The computer won, as paper beats rock")
if computer_choice == "scissors" and user_choice == "paper":
    compScore += 1
    print("The computer won, as scissors beats paper")
if computer_choice == "scissors" and user_choice == "rock":
    userScore += 1
    print("You won, as rock beats scissors")
if computer_choice == "rock" and user_choice == "paper":
    userScore += 1
    print("You won, as paper beats rock")
if computer_choice == "paper" and user_choice == "scissors":
    userScore += 1
    print("You won, as scissors beats paper")
if computer_choice == user_choice:
    print("you tied")

print(d)

print("Your score: ", userScore)
print("Computer score: ", compScore)

print(d)
