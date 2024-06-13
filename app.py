#template for console based rock papaer scissors game
import random

def rock_paper_scisors():
    player_score = 0
    computer_score = 0

    print("Welcome to the Rock Paper Scissors Game!")
    
    choices = ["rock", "paper", "scissors"]

    while player_score < 3 and computer_score < 3:
        print(f"\n\n------------------------------------------------------------\n Player score: {player_score} Computer score: {computer_score}\n------------------------------------------------------------\n\n")
        user_choice = input("Enter your choice: rock, paper or scissors: ")
        computer_choice = random.choice(choices)
        print(f"Computer choice is: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a draw")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You won this round!")
            player_score += 1
        else:
            print("Computer won this round!")
            computer_score += 1
    
    if player_score == 3:
        print("You won the game!")
    else:
        print("Computer won the game!")

rock_paper_scisors()