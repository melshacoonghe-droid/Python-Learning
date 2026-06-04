import secrets
import string
import random

print("=" * 40)
print("🔐 Welcome to the Password Generator")
print("=" * 40)

# Password length
while True:
    try:
        length = int(input("\nEnter desired password length: "))
        if length >= 4:
            break
        print("Password length should be at least 4.")
    except ValueError:
        print("Please enter a valid number.")

# Character options
print("\nSelect what to include in your password:")

use_lower = input("✅ Lowercase letters (a-z)? (y/n): ").lower() == "y"
use_upper = input("✅ Uppercase letters (A-Z)? (y/n): ").lower() == "y"
use_digits = input("✅ Numbers (0-9)? (y/n): ").lower() == "y"
use_symbols = input("✅ Symbols (!@#$%^&*)? (y/n): ").lower() == "y"

# Build character pool
character_pool = ""

if use_lower:
    character_pool += string.ascii_lowercase

if use_upper:
    character_pool += string.ascii_uppercase

if use_digits:
    character_pool += string.digits

if use_symbols:
    character_pool += string.punctuation

if not character_pool:
    print("\n❌ Error: You must select at least one character type.")
    exit()

# Specific word option
include_word = input(
    "\nDo you want a specific word included in the password? (y/n): "
).lower()

special_word = ""

if include_word == "y":
    special_word = input("Enter the word to include: ")

    if len(special_word) >= length:
        print(
            "\n❌ The chosen word is longer than or equal to the password length."
        )
        exit()

# Generate password
remaining_length = length - len(special_word)

password_chars = [
    secrets.choice(character_pool)
    for _ in range(remaining_length)
]

# Insert special word
password_chars.extend(list(special_word))

# Shuffle so the word isn't always at the end
random.shuffle(password_chars)

password = "".join(password_chars)

print("\n" + "=" * 40)
print("🎉 Your Password Has Been Generated!")
print("=" * 40)
print(password)
print("=" * 40)