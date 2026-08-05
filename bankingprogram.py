
balance = 0

def show_balance():
    print(f"Your current balance is Rs.{balance:.2f}")

def deposit():
    amount = float(input("How much would you like to deposit? : Rs."))
    global balance

    if amount < 0:
        print("Invalid amount")
    else:
        balance += amount
        print(f"Rs.{amount:.2f} has been successfully deposited")
        print(f"Your new balance is Rs.{balance:.2f}")

def withdraw():
    amount = float(input("How much would you like to withdraw? :Rs."))
    global balance

    if amount > balance :
        print("Insufficent Funds")
    elif amount < 0 :
        print("Invalid amount")
    else:
        balance -= amount
        print(f"Rs.{amount:.2f} has been successfully withdrawn")
        print(f"Your new balance is Rs.{balance:.2f}")

    
def main():
    running = True
    options = ["1. Show Balance", "2. Deposit", "3. Withdraw", "4. Exit"]
    while running:
         print ("********************************")
         print("Welcome to the Banking Program")
         print ("********************************")
         print()
         for option in options:
             print(option)

         choice = input("Please select an option (1-4): ")

         match choice:
             case "1":
                 show_balance()
             case"2":
                  deposit()
             case "3":
                  withdraw()
             case "4":
                  print("Thank you! Have a nice day!")
                  running = False


if __name__ == "__main__":
    main()
