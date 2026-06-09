import random

print("=== Rock, Paper, Scissors ===")

choices = ["rock", "paper", "scissors"]

while True:
    player = input("\nChoose Rock, Paper, or Scissors: ").lower()

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

    play_again = input("\nPlay again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break