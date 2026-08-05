import random
import time

def spin_row():
    symbols = ["🪙", "💰", "💵", "💶", "🤑"]
    final = []                                     # An alternative code return [random.choice(symbols) for _ in range(3)]
    for symbol in range(3):
        random_symbol = random.choice(symbols)
        final.append(random_symbol)
    return final

def print_row(row):
    print("--------------------------")
    print(" | " .join(row))
    print("--------------------------")

def get_payout(row):
    if row[0] == row[1] == row[2] :
        if row[0] == "🪙" :
            pay = bet * 2
        elif row[0] == "💰" :
            pay = bet * 3
        elif row[0] == "💵" :
            pay = bet * 5
        elif row[0] == "💶" :
            pay = bet * 10
        elif row[0] == "🤑" :
             pay = bet * 20

    else:
        pay = 0
    return pay
        
        
print("Welcome to the Slot Machine Game!")
print()
print("Symbols: 🪙  💰 💵 💶 🤑")
print()


balance = 100
round = 1

while balance > 0 :
     
     time.sleep(1)
     print(f"Round : {round}")
     print(f"Your balance is {balance} coins.")

     bet = input("How many coins would you like to bet? : ")

     if not bet.isdigit() :
         print("Invalid input")
         continue
     else:
         bet = int(bet)

     

     if bet <= 0 :
         print("Bet must be greater than 0")
         continue
     if bet > balance :
         print("Insufficent balance. Try Again")
         continue

     balance -= bet 
     print("Spinning.......")
     time.sleep(1)

     row = spin_row()
     print_row(row)

     payout = get_payout(row)
     balance += payout

     if payout > 0 :
         print(f"Congratulations! You won {payout} coins!")
     else:
         print("You Lost! Better Luck Next Time!")

     if balance <= 0:
         print("You have run out of coins. Game Over!")
         break

     play_again = input("Would you like to play again? (y/n): ").lower()

     if play_again != "y" :
         break
     else:
         round += 1


print("Thank you for playing! ")
print(f"You have played {round} rounds and your final balance is {balance} coins.")   

