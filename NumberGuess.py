#Random Number Guessing Game

import random

print("----------------------------------------")
print("Welcome to the Number Guessing Game")
print("----------------------------------------")
print()


while True:
    print("What Range of Number would you like to guess?")
    low = int(input("Enter the lower end of the range : "))
    high = int(input("Enter the upper end of the range : "))

    number = random.randint(low, high)
    
    print()
    print("Number Ready!!!")

    while True:
        print()
        answer = int(input("Enter your guess : "))
        print()
        if answer<low or answer>high:
            print(f"Please enter a number between {low} and {high}")
        elif answer > number:
            print("Lower. Try Again")
        elif answer < number:
            print("Higher. Try Again")
        elif answer == number :
            print(f"Correct!!! The number is {number}")
            break
    
    print("Congratulations! You have finished the number guessing game!")
    print()
    play_again = input("Do you want to play again? (Y/N): ").upper()
    print()
    if play_again != "Y":
        print("Thank you for playing the Number Guessing Game. Goodbye!")
        break










