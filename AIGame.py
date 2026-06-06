import random
import time

# ==============================
# DREAMSCAPE EXPLORER
# ==============================

locations = [
    "Crystal Forest",
    "Floating Islands",
    "Shadow Caves",
    "Golden Desert",
    "Frozen Citadel",
    "Ancient Ruins",
    "Moonlit Lake",
    "Sky Temple"
]

enemies = [
    "Void Beast",
    "Shadow Knight",
    "Crystal Golem",
    "Dream Serpent",
    "Ancient Guardian",
    "Phantom Mage"
]

treasures = [
    "Legendary Sword",
    "Mystic Orb",
    "Dragon Crown",
    "Golden Relic",
    "Ancient Scroll",
    "Phoenix Feather"
]

events = [
    "You discover a hidden path.",
    "A mysterious traveler gives you advice.",
    "You find a healing spring.",
    "A magical storm appears.",
    "You uncover forgotten knowledge."
]

player = {
    "name": "",
    "health": 100,
    "attack": 10,
    "gold": 0,
    "inventory": []
}

world = []

def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)
    print()

def create_world():
    global world
    world = random.sample(locations, len(locations))

def show_stats():
    print("\n===== PLAYER STATS =====")
    print(f"Name: {player['name']}")
    print(f"Health: {player['health']}")
    print(f"Attack: {player['attack']}")
    print(f"Gold: {player['gold']}")
    print(f"Inventory: {', '.join(player['inventory']) if player['inventory'] else 'Empty'}")
    print("========================\n")

def random_event():
    event = random.choice(events)
    slow_print(f"\n✨ {event}")

    bonus = random.randint(5, 20)

    if "healing" in event.lower():
        player["health"] += bonus
        slow_print(f"You gained {bonus} health!")
    elif "traveler" in event.lower():
        player["attack"] += 2
        slow_print("Your attack increased!")
    elif "knowledge" in event.lower():
        player["gold"] += 15
        slow_print("You found 15 gold!")
    else:
        player["gold"] += 5

def find_treasure():
    treasure = random.choice(treasures)

    if treasure not in player["inventory"]:
        player["inventory"].append(treasure)
        player["attack"] += 5
        slow_print(f"\n🎁 You found a {treasure}!")
        slow_print("Attack increased by 5!")
    else:
        player["gold"] += 20
        slow_print("\nYou found duplicate treasure.")
        slow_print("Sold for 20 gold.")

def battle():
    enemy = random.choice(enemies)

    enemy_health = random.randint(30, 80)
    enemy_attack = random.randint(5, 15)

    slow_print(f"\n⚔️ A wild {enemy} appears!")

    while enemy_health > 0 and player["health"] > 0:

        print("\n1. Attack")
        print("2. Heal")
        print("3. Run")

        choice = input("> ")

        if choice == "1":
            damage = random.randint(
                player["attack"] - 3,
                player["attack"] + 5
            )

            enemy_health -= damage

            slow_print(
                f"You dealt {damage} damage!"
            )

            if enemy_health <= 0:
                reward = random.randint(20, 50)
                player["gold"] += reward

                slow_print(
                    f"You defeated the {enemy}!"
                )

                slow_print(
                    f"You gained {reward} gold!"
                )

                return

        elif choice == "2":

            heal = random.randint(10, 25)

            player["health"] += heal

            slow_print(
                f"You healed {heal} HP."
            )

        elif choice == "3":

            if random.random() < 0.5:
                slow_print(
                    "You escaped!"
                )
                return
            else:
                slow_print(
                    "Escape failed!"
                )

        damage = random.randint(
            enemy_attack - 2,
            enemy_attack + 4
        )

        player["health"] -= damage

        slow_print(
            f"{enemy} hits you for {damage} damage!"
        )

        print(
            f"Your HP: {player['health']} | "
            f"Enemy HP: {enemy_health}"
        )

    if player["health"] <= 0:
        slow_print("\n💀 You have fallen...")

def explore(location):

    slow_print(f"\n📍 Exploring {location}")

    encounter = random.randint(1, 100)

    if encounter <= 40:
        battle()

    elif encounter <= 70:
        find_treasure()

    else:
        random_event()

def shop():

    while True:

        print("\n===== SHOP =====")
        print("1. Buy Health (+30 HP) - 20 Gold")
        print("2. Buy Sword Upgrade (+5 Attack) - 50 Gold")
        print("3. Exit Shop")

        choice = input("> ")

        if choice == "1":

            if player["gold"] >= 20:
                player["gold"] -= 20
                player["health"] += 30
                slow_print("Health restored!")
            else:
                slow_print("Not enough gold.")

        elif choice == "2":

            if player["gold"] >= 50:
                player["gold"] -= 50
                player["attack"] += 5
                slow_print("Attack increased!")
            else:
                slow_print("Not enough gold.")

        elif choice == "3":
            return

def ending():

    slow_print("\n🌟 FINAL RESULTS 🌟")

    show_stats()

    score = (
        player["gold"]
        + len(player["inventory"]) * 50
        + player["attack"] * 5
    )

    print(f"Final Score: {score}")

    if score > 500:
        slow_print(
            "Legendary Dreamwalker!"
        )
    elif score > 300:
        slow_print(
            "Master Explorer!"
        )
    else:
        slow_print(
            "A Brave Adventurer!"
        )

def main():

    slow_print("===== DREAMSCAPE EXPLORER =====")

    player["name"] = input(
        "Enter your hero's name: "
    )

    create_world()

    for location in world:

        if player["health"] <= 0:
            break

        print("\n----------------")
        print(f"Current Area: {location}")
        print("----------------")

        print("1. Explore")
        print("2. View Stats")
        print("3. Visit Shop")

        choice = input("> ")

        if choice == "1":
            explore(location)

        elif choice == "2":
            show_stats()
            explore(location)

        elif choice == "3":
            shop()
            explore(location)

    ending()

if __name__ == "__main__":
    main()