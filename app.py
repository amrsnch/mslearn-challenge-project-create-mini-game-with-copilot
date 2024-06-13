#template for console based rock papaer scissors game
import random

def rock_paper_scissors():
    """
    Driver function of a game, where user plays rock paper scissors with computer.
    (could have usd numbers as input to simplify the game, but used strings for better user experience. 
    Also numbers would made time complexity better tbh, but it's a game so it's fine.)
    """
    player_score = 0
    computer_score = 0

    pretty_printer("Welcome to the Rock Paper Scissors Game!")
    
    choices = ["rock", "paper", "scissors"]

    while player_score < 3 and computer_score < 3:
        pretty_printer(f"Player score: {player_score} Computer score: {computer_score}")
        
        user_choice = input("Enter your choice (rock, paper or scissors): ")
        
        computer_choice = random.choice(choices)

        print(f"Computer choice is: {computer_choice}")

        if user_choice not in choices:
            #handling invalid choice
            print("Invalid choice, please enter a valid choice.")
            continue

        if user_choice == computer_choice:
            print("It's a draw")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You won this round!")
            player_score += 1
        else:
            print("Computer won this round!")
            computer_score += 1
    
    if player_score == 3:
        pretty_printer("You won the game!")
    else:
        pretty_printer("Computer won the game!")

def pretty_printer(string):
    """
    Function to print a string in a pretty way.
    """
    print(f"\n------------------------------------------------------------\n {string}\n------------------------------------------------------------")

rock_paper_scissors()