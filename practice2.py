

#Shopping Cart Program
foods = []
prices = []
quantities = []
totals = []
while True:
    print()
    food = input("What food would you like to buy (q to quit) : ")
    if food.lower() == "q":
         break
    else:
         foods.append(food)
         print()
         quantity = int(input(f"How many {food} would you like to buy : "))
         quantities.append(quantity)
         print()
         price = float(input(f"Insert the price of a {food} :Rs. "))
         prices.append(price)

x = len(foods)
print()
print("-----YOUR SHOPPING BILL-----")
print()
for y in range(0,x) :
     print(foods[y], end = " ")
     print("*",end = " ")
     print(quantities[y], end = " ")
     print("=",end = " ")
     total = prices[y] * quantities[y]
     totals.append(total)
     print(f"Rs.{total:.2f}")
     
Amount = 0
for total in totals:
     Amount += total

print()
print(f"Your Total is Rs.{Amount:.2f}")