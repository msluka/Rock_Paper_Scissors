import random

player_wins = 0
computer_wins = 0

while player_wins < 3 and computer_wins < 3:

    print("Let's play rock, paper, or scissors")

    player_choice = input("Choose and write - rock, paper, or scissors?: \n").lower()

    choices = ["rock", "paper", "scissors"]

    if player_choice not in choices:
        print("Invalid choice!")
        continue # Go back to the start of the loop

    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}\n")

    if (player_choice == "rock" and computer_choice == "scissors") or (
            player_choice == "scissors" and computer_choice == "paper") or (
            player_choice == "paper" and computer_choice == "rock"):
        winner = "Player"
    elif player_choice == computer_choice:
        winner = "Tie"
    else:
        winner = "Computer"

    if winner == "Player":
        player_wins += 1
        print("You won")
    elif winner == "Computer":
        computer_wins += 1
        print("Computer won")
    else:
        print("It's a tie")
    print("")
    print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}.")
    print("")

if player_wins > computer_wins:
    print("Congratulations! You won..")

if computer_wins > player_wins:
    print("Computer won!.")