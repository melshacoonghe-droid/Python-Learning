#Cafe Order
foods = {"Tuna sandwich(TS)":800, "Chicken sandwich(CS)":950, "Burger and Fries(BF)":1100, "Strawberry mousse(SM)":850, "Chocolate Cake(CC)":750}
drinks = {"Coffee(C)":600, "Latte(L)":700, "Americano(A)":950, "Cappuccino(CA)":750, "Hot chocolate(H)":800, }
order_food= []
order_drink=[]
total = 0
print("------------------------------------------------------")
print("                         MENU                         ")
print("------------------------------------------------------")
print()
print("Foods")
print()
for key,value in foods.items():
    print(f"{key:<22}:Rs.{value:<6}")

print()
print("Drinks")
print()
for key,value in drinks.items():
    print(f"{key:<22}:Rs.{value:<6}")
print()
while True:
    food = input("What food would you like to order? (Enter the code name) (Q to quit) : ").upper()
    if food == "Q":
        break
    elif food == "TS" :
         food = "Tuna sandwich(TS)"
         order_food.append(food)
    elif food == "CS" :
        food = "Chicken sandwich(CS)"
        order_food.append(food)
    elif food == "BF" :
        food = "Burger and Fries(BF)"
        order_food.append(food)
    elif food == "SM" :
        food = "Strawberry mousse(SM)"
        order_food.append(food)
    elif food == "CC" :
        food = "Chocolate Cake(CC)"
        order_food.append(food)
    else:
        print("Invlid code")

while True:
    drink = input("What drink would you like to order? (Enter the code name) (Q to quit) : ").upper()
    if drink == "Q":
        break
    elif drink == "C" :
         drink = "Coffee(C)"
         order_drink.append(drink)
    elif drink == "L" :
        drink = "Latte(L)"
        order_drink.append(drink)
    elif drink == "A" :
        drink = "Americano(A)"
        order_drink.append(drink)
    elif drink == "CA" :
        drink = "Cappuccino(CA)"
        order_drink.append(drink)
    elif drink == "H" :
        drink = "Hot chocolate(H)"
        order_drink.append(drink)
    else:
        print("Invlid code")
print()
print("-------Thank You For Ordering-------")

for food in order_food:
    total += foods.get(food)

for drink in order_drink:
    total += drinks.get(drink)

print(f"Your total is Rs.{total:.2f}")