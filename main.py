import math
#Area of a circle 

r = float(input("What is the radius of the circle :  "))
Area = math.pi * (r ** 2)

print(f"The Area of the circle is : {round(Area, 2)}")


# Hypotenous of a right side triangle

a = float(input("Length of one side of a triangle : "))
b = float(input("Length of other side of a triangle : "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The length of the hypotenous side is {round(c, 2)} cm")




#Python Calculator


Op = input("Insert an operator your would like ( + - * / : )")
a = float(input("Insert the first number : "))
b = float(input("Insert the second number : "))

if Op == "+" :
    c = a + b
    print(f"Your output is {c}")
elif Op == "-" :
    c = a - b
    print(f"Your output is {c}")
elif Op == "*" :
    c = a * b
    print(f"Your output is {c}")
elif Op == "/" :
    c = a/b
    print(f"Your output is {c}")
else:
    print("The operator you selected is not valid")

    

# Temperature Converter

Temp = float(input("Input the temperature : "))
unit = input("Is your temperature in celcius or farenheit (C / F ) : ")

if unit == "C" :
    Temp = (Temp * 9 / 5) + 32
    print(f"Your temperature is {round(Temp, 1)} Farenheit")
elif unit == "F" :
    Temp = (Temp - 32) * 5 / 9 
    print(f"Your Temperature is {round(Temp, 1)} Celcius")
else:
    print("Yout temperature unit is not valid")