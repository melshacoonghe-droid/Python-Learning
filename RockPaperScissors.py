#A simple game of rock, paper, scissors

import random
options = ["rock", "paper", "scissors"]

print("----------------------------------------")
print("Welcome to Rock, Paper, Scissors!")
print("----------------------------------------")

round = 0
player_score = 0
computer_score = 0
while True:
    print()
    computer = random.choice(options)
    player = input("Enter your choice (rock, paper, scissors): ").lower()

    if player not in options:
        print("Invalid choice. Please try again.")
        continue
    else:
        round += 1

    if player == computer:
        print(f"It's a tie! Both chose {player}.")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print(f"You win! {player} beats {computer}.")
        player_score += 1
    else:
        print(f"You lose! {computer} beats {player}.")
        computer_score += 1

    play_again = input(f"Would you like to play again? (Y/N): ").upper()
    if play_again != "Y":
        print()
        print(f"Final Score: Player : {player_score} / computer : {computer_score}")
        print(f"Total Rounds Played: {round}")
        print()
        print("Thank you for playing Rock, Paper, Scissors! Goodbye!")
        break


