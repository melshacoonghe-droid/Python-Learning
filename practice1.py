"""
#Validate user input
#User name must not contain more than 12 characters
#No spaces or digits
 
User_name = input("Type in your username : ")

if len(User_name) <=12 and User_name.isalpha():
    print(f"Congrats! Your User Name is {User_name}")
else:
    print("Your User name is not valid")
"""


"""
#Yearly compound interst Calculator
p = 0 #principle amount
r = 0 #rate
t = 0 #time in years

p = float(input("Input your principle amount : "))

while p <= 0 :
    print("Principle amount can't be zero or negative")
    p = float(input("Input your principle amount : "))

r = float(input("What is your interst rate : "))

while r <= 0 :
    print("Interst rate  can't be zero or negative")
    r = float(input("What is your interst rate : "))

t = float(input("Input the number of years you would like to compund for : "))

while t <= 0 :
    print("Years amount can't be zero or negative")
    t = float(input("Input the number of years you would like to compund for : "))

Final = p * (( 1 + (r/100)) **t)

print(f"Your final amount after {t} years would be Rs.{Final:,.2f}")

"""

"""
#Countdown Timer Normal
import time

t = int(input("Insert time in seconds : "))
for x in range(t, 0, -1):
    print(x)
    time.sleep(1)

print("TIME'S UP")
"""

"""
#Countdown Timer Digital
import time

t = int(input("Insert time in seconds : "))
for x in range(t, 0, -1):
    min = int(x / 60) % 60
    hrs = int(x / 3600)
    sec = x % 60
    print(f"{hrs:02}:{min:02}:{sec:02}")
    time.sleep(1)

print("TIME'S UP")

"""

