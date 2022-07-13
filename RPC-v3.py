import random

# Quicker way to print a bunch of lines
d = "-----------------------------------"

# Leaderboard
compScore = 0
userScore = 0

# Input a score at which the program ends
score_input = input("To what score do you want to play?: ")
final_score = int(score_input)

# "Play" had a different function before I changed my code, techinically this variable is obsolete now,
# but the code still runs so why would I bother to change it
play = True
while play == True:
    possible_choices = ["rock", "paper", "scissors"] # List of all possible plays
    computer_choice = random.choice(possible_choices) # Decent way to randomise plays, I just copied this from online
    print(d) 
    user_choice = input("Choose! (rock, paper or scissors): ") # User input for choice
    print(d)
    # This was mainly for debugging, but I thought it was nice to know your own choice after you typed it so I left it in
    print("You chose: ", user_choice)
    print("The computer chose: ", computer_choice)

    print("") # Empty line to make everything less cluttered

    # I am very sure that this is not even close to the best way to do this. I just don't know how to
    # write the code smaller as of now, and its only like, 70 lines total so it really doesn't matter regardless
    if user_choice not in possible_choices:
        compScore += 1
        print("The computer won as you did not enter a valid choice (",user_choice,")")
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

    # The actual leaderboard being printed
    print("Your score: ", userScore)
    print("Computer score: ", compScore)

    # Once again, there is definitely a way to do this that is easier and takes up less lines, but this is what I came up with,
    # and it works, so why would I bother changing it
    if compScore >= final_score:
        print("")
        print("Final Scores!")
        print("Your score: ", userScore)
        print("Computer's score: ", compScore)
        if userScore > compScore:
            print("You win!")
        elif userScore < compScore:
            print("You lose!")
        print(d)
        print("I hope you enjoyed!")
        death = input()
        if death == death:
            break

    if userScore >= final_score:
        print("")
        print("Final Scores!")
        print("Your score: ", userScore)
        print("Computer's score: ", compScore)
        if userScore > compScore:
            print("You win!")
        elif userScore < compScore:
            print("You lose!")
        print(d)
        print("I hope you enjoyed!")
        death = input()
        if death == death:
            break
