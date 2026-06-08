import random
import time

# ==========================
# AI NUMBER GUESSING GAME
# ==========================

games_played = 0
games_won = 0
best_score = None

AI_MESSAGES = [
    "Interesting guess...",
    "Let's see how close you are.",
    "Analyzing your choice...",
    "Hmm... that's not quite it.",
    "Processing your guess..."
]


def choose_difficulty():
    print("\nDIFFICULTY LEVELS")
    print("1. Easy (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard (1 - 500)")

    while True:
        choice = input("\nChoose difficulty (1-3): ")

        if choice == "1":
            return 1, 50
        elif choice == "2":
            return 1, 100
        elif choice == "3":
            return 1, 500
        else:
            print("Invalid choice.")


def give_temperature_hint(diff):
    diff = abs(diff)

    if diff == 0:
        return "🎯 PERFECT!"
    elif diff <= 3:
        return "🔥 BURNING HOT!"
    elif diff <= 10:
        return "🥵 HOT!"
    elif diff <= 20:
        return "🌡️ WARM"
    elif diff <= 50:
        return "❄️ COOL"
    else:
        return "🧊 ICE COLD"


def play_game():
    global games_played, games_won, best_score

    low, high = choose_difficulty()
    secret = random.randint(low, high)

    attempts = 0
    hints_used = 0

    start_time = time.time()

    print(f"\n🤖 AI: I have chosen a secret number between {low} and {high}.")
    print("You get 3 hints.")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            print(f"\n🤖 AI: {random.choice(AI_MESSAGES)}")

            distance = guess - secret
            print(give_temperature_hint(distance))

            if guess < secret:
                print("📈 Higher!")
            elif guess > secret:
                print("📉 Lower!")
            else:
                end_time = time.time()
                elapsed = round(end_time - start_time, 2)

                print("\n" + "=" * 40)
                print("🎉 YOU WON!")
                print("=" * 40)

                print(f"Secret Number : {secret}")
                print(f"Attempts      : {attempts}")
                print(f"Time Taken    : {elapsed} seconds")
                print(f"Hints Used    : {hints_used}")

                games_played += 1
                games_won += 1

                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print("🏆 NEW BEST SCORE!")

                break

            if hints_used < 3:
                use_hint = input("\nUse a hint? (y/n): ").lower()

                if use_hint == "y":
                    hints_used += 1

                    if hints_used == 1:
                        if secret % 2 == 0:
                            print("💡 Hint: Number is EVEN.")
                        else:
                            print("💡 Hint: Number is ODD.")

                    elif hints_used == 2:
                        midpoint = (low + high) // 2

                        if secret > midpoint:
                            print("💡 Hint: Number is in the UPPER half.")
                        else:
                            print("💡 Hint: Number is in the LOWER half.")

                    elif hints_used == 3:
                        print(f"💡 Hint: The number is between {max(low, secret - 10)} and {min(high, secret + 10)}")

        except ValueError:
            print("❌ Enter a valid number.")


while True:
    print("\n" + "=" * 50)
    print("🎯 ULTIMATE AI NUMBER GUESSING GAME")
    print("=" * 50)

    play_game()

    print("\n📊 STATISTICS")
    print(f"Games Played : {games_played}")
    print(f"Games Won    : {games_won}")

    if best_score:
        print(f"Best Score   : {best_score} attempts")

    again = input("\nPlay Again? (y/n): ").lower()

    if again != "y":
        print("\n🤖 AI: Thanks for playing!")
        break