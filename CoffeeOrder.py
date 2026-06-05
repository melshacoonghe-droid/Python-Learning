#user orders coffee from a coffee shop

#Types of Coffee available at the shop
A = "Americano"
B = "Espresso"
C = "Latte"
D = "Cappuccino"
E = "Mocha"
F = "Hot Chocolate"

print("Hi, What would you like to order today A =", A , "B =" ,B , "C=", C, "D =", D, "E=", E, "or F=", F, "? (Please input the Letter of your order )")
Customer_Order = input()

if Customer_Order == "A":
    print("The bill for your",A,"is Rs.700")
elif Customer_Order == "B":
    print("The bill for your",B,"is Rs.650")
elif Customer_Order == "C":
    print("The bill for your",C,"is Rs.800")
elif Customer_Order == "D":
    print("The bill for your",D,"is Rs.850")
elif Customer_Order == "E":
    print("The bill for your",E,"is Rs.600")
else: 
    print("The bill for your",F,"is Rs.750")

print("Thank you for ordering. Have a nice day.")