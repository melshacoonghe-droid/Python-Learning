import random

words = ["apple", "mountain", "river", "computer", "sunshine", "library", "ocean", "forest", "planet", "camera", "keyboard", "window", "pencil", 
        "notebook", "journey", "diamond", "elephant", "butterfly", "rainbow", "volcano", "galaxy", "rocket", "castle", "village", "bridge",
        "flower", "garden", "blanket", "pillow", "airplane", "bicycle", "lantern", "compass", "treasure", "adventure", "whisper", "thunder", 
        "harmony", "freedom", "victory", "curiosity", "wisdom", "friendship", "challenge", "discovery", "creativity", "imagination", "celebration",
        "knowledge", "future","anchor", "balloon", "canyon", "desert", "emerald", "feather", "glacier", "harbor", "island", "jungle", "kitten", 
        "ladder", "meadow", "nebula", "orchard", "pebble", "quartz", "raindrop", "sapphire", "tornado", "umbrella", "valley", "waterfall", 
        "xylophone", "yacht", "zeppelin", "acorn", "backpack", "coconut", "dolphin", "engine", "firefly", "guitar", "helmet", "icicle", "jigsaw",
        "koala", "lighthouse", "moonlight", "narwhal", "owl", "penguin", "quiver", "sandcastle", "telescope", "universe", "vineyard", "wildflower",
        "zipper", "zucchini"]

wrong = 0
print("Welcome to hangman!")
print()

while True:
     wrong = 0

     word = random.choice(words)
     word_length = len(word)

     display = ["_"] * word_length
     print(" ".join(display))
     print(f"Your word has {word_length} letters.")


     while True:
          guess = input("What is yout guess : ").lower()
          display_list = list(display)
          
          if guess in word:
             print("Correct!") 
             for i in range(word_length):
                if word[i] == guess:
                   display[i] = guess
             print(" ".join(display))  
          else:
             print("Incorrect")
             wrong += 1
          
          if wrong == 1:
             print()
             print()
             print("         o    ")
             print()
             print()
          elif wrong == 2:
             print()
             print()
             print("         o    ")
             print("         |      ")
             print()
        
          elif wrong == 3:
             print()
             print()
             print("         o    ")
             print("       / | \\    ")
             print()
    
          elif wrong == 4:
             print()
             print()
             print("         o    ")
             print("       / | \\    ")
             print("        / \\ ")
    
          elif wrong == 5:
             print()
             print("         |      ")
             print("         o    ")
             print("       / | \\    ")
             print("        / \\ ")
    
          elif wrong == 6 :
             print(" _______")
             print("|        |      ")
             print("|        o    ")
             print("|      / | \\")
             print("|       / \\")
             print()
             print("Game Over!!! You Lose")
             print(f"The Word is {word}")
             break

          if display.count("_") == 0 :
             print("You have guessed everything!! You Won")
             break

     again = input("Would you like to play again? (y/n): ").lower()
    

     if again != "y" :
        print("Thank You For Playing. Good Bye")
        break
             
     


     " _______"
" |       |      "
" |       o    "
" |     / | \\"
" |      / \\ "

    
    





