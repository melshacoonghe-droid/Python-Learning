import random

words = [
    "python", "computer", "gaming", "hangman",
    "programming", "keyboard", "monitor", "internet",
    "science", "developer"
]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

print("🎯 Welcome to Hangman!")

while True:
    print(hangman_stages[wrong_guesses])

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed Letters:", " ".join(guessed_letters))

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("❌ Wrong guess!")

    if wrong_guesses >= max_wrong_guesses:
        print(hangman_stages[wrong_guesses])
        print("\n💀 Game Over!")
        print("The word was:", word)
        break