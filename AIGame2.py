import random
import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.cleanliness = 50
        self.health = 100
        self.level = 1
        self.exp = 0
        self.day = 1

    def show_stats(self):
        print("\n" + "=" * 40)
        print(f"Day: {self.day}")
        print(f"Pet: {self.name}")
        print(f"Level: {self.level}")
        print(f"EXP: {self.exp}/100")
        print("-" * 40)
        print(f"Health      : {self.health}")
        print(f"Hunger      : {self.hunger}")
        print(f"Happiness   : {self.happiness}")
        print(f"Energy      : {self.energy}")
        print(f"Cleanliness : {self.cleanliness}")
        print("=" * 40)

    def feed(self):
        print(f"\nYou fed {self.name}.")
        self.hunger = max(0, self.hunger - 25)
        self.exp += 10

    def play(self):
        print(f"\nYou played with {self.name}.")
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 15)
        self.hunger += 10
        self.exp += 15

    def sleep(self):
        print(f"\n{self.name} took a nap.")
        self.energy = min(100, self.energy + 35)
        self.hunger += 10
        self.exp += 8

    def clean(self):
        print(f"\nYou cleaned {self.name}.")
        self.cleanliness = 100
        self.exp += 10

    def medicine(self):
        if self.health < 100:
            print(f"\nYou gave medicine to {self.name}.")
            self.health = min(100, self.health + 25)
        else:
            print("\nYour pet is already healthy.")

    def next_day(self):
        self.day += 1

        self.hunger += random.randint(5, 15)
        self.energy -= random.randint(5, 12)
        self.cleanliness -= random.randint(4, 10)
        self.happiness -= random.randint(2, 8)

        self.hunger = min(100, self.hunger)
        self.energy = max(0, self.energy)
        self.cleanliness = max(0, self.cleanliness)
        self.happiness = max(0, self.happiness)

        self.check_health()
        self.random_event()
        self.level_up()

    def check_health(self):
        if self.hunger > 80:
            self.health -= 10

        if self.energy < 20:
            self.health -= 8

        if self.cleanliness < 20:
            self.health -= 7

        if self.happiness < 15:
            self.health -= 6

        self.health = max(0, self.health)

    def random_event(self):
        event = random.randint(1, 8)

        if event == 1:
            print("\n⭐ Your pet found a treasure!")
            self.exp += 30

        elif event == 2:
            print("\n🌧 Your pet got caught in rain.")
            self.cleanliness -= 20

        elif event == 3:
            print("\n🎉 Birthday celebration!")
            self.happiness += 25

        elif event == 4:
            print("\n🤒 Your pet caught a cold.")
            self.health -= 15

        elif event == 5:
            print("\n🍖 Found extra food!")
            self.hunger -= 20

        elif event == 6:
            print("\n😴 Your pet overslept.")
            self.energy += 20

        elif event == 7:
            print("\n🏃 Morning exercise.")
            self.health += 5
            self.energy -= 10

        else:
            print("\nNothing special happened today.")

        self.health = max(0, min(100, self.health))
        self.energy = max(0, min(100, self.energy))
        self.happiness = max(0, min(100, self.happiness))
        self.cleanliness = max(0, min(100, self.cleanliness))
        self.hunger = max(0, min(100, self.hunger))

    def level_up(self):
        while self.exp >= 100:
            self.exp -= 100
            self.level += 1
            self.health = 100
            print(f"\n🎉 {self.name} leveled up!")
            print(f"New Level: {self.level}")

    def alive(self):
        return self.health > 0


def menu():
    print("\nChoose an action")
    print("1. Feed")
    print("2. Play")
    print("3. Sleep")
    print("4. Clean")
    print("5. Give Medicine")
    print("6. View Stats")
    print("7. End Day")
    print("8. Quit")


print("=" * 45)
print("      VIRTUAL PET SIMULATOR")
print("=" * 45)

pet_name = input("Name your pet: ")
pet = Pet(pet_name)

while pet.alive():

    menu()

    choice = input("Enter choice: ")

    if choice == "1":
        pet.feed()

    elif choice == "2":
        pet.play()

    elif choice == "3":
        pet.sleep()

    elif choice == "4":
        pet.clean()

    elif choice == "5":
        pet.medicine()

    elif choice == "6":
        pet.show_stats()

    elif choice == "7":
        print("\nA new day begins...")
        time.sleep(1)
        pet.next_day()

    elif choice == "8":
        print("\nThanks for playing!")
        break

    else:
        print("\nInvalid choice.")

    if not pet.alive():
        break

if pet.health <= 0:
    print("\n💀 Your pet became too unhealthy.")
    print("Game Over.")

print("\nFinal Stats")
pet.show_stats()
print("\nGoodbye!")