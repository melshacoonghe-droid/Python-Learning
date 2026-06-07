import random
import json
import os

# ==========================================
# PROCEDURAL DUNGEON RPG
# ==========================================

SAVE_FILE = "rpg_save.json"


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.attack = 15
        self.level = 1
        self.exp = 0
        self.gold = 0
        self.potions = 3

    def heal(self):
        if self.potions > 0:
            heal_amount = random.randint(20, 40)
            self.hp = min(self.max_hp, self.hp + heal_amount)
            self.potions -= 1
            print(f"\nYou healed {heal_amount} HP.")
        else:
            print("\nNo potions available.")

    def gain_exp(self, amount):
        self.exp += amount
        print(f"\nGained {amount} EXP.")

        while self.exp >= self.level * 50:
            self.exp -= self.level * 50
            self.level += 1
            self.max_hp += 20
            self.attack += 5
            self.hp = self.max_hp

            print("\nLEVEL UP!")
            print(f"Level: {self.level}")
            print(f"Attack: {self.attack}")
            print(f"Max HP: {self.max_hp}")

    def display(self):
        print("\n======== PLAYER ========")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Attack: {self.attack}")
        print(f"EXP: {self.exp}")
        print(f"Gold: {self.gold}")
        print(f"Potions: {self.potions}")
        print("========================")


class Enemy:
    def __init__(self, level):
        names = [
            "Goblin",
            "Skeleton",
            "Bandit",
            "Orc",
            "Dark Mage",
            "Slime",
            "Wolf"
        ]

        self.name = random.choice(names)
        self.level = level

        self.hp = 30 + (level * 10)
        self.attack = 5 + (level * 3)

    def display(self):
        print(f"\n{self.name} (Lv.{self.level})")
        print(f"HP: {self.hp}")
        print(f"ATK: {self.attack}")


class Dungeon:
    def __init__(self):
        self.floor = 1

    def next_floor(self):
        self.floor += 1


def save_game(player, dungeon):
    data = {
        "name": player.name,
        "hp": player.hp,
        "max_hp": player.max_hp,
        "attack": player.attack,
        "level": player.level,
        "exp": player.exp,
        "gold": player.gold,
        "potions": player.potions,
        "floor": dungeon.floor
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

    print("\nGame Saved.")


def load_game():
    if not os.path.exists(SAVE_FILE):
        return None, None

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    player = Player(data["name"])

    player.hp = data["hp"]
    player.max_hp = data["max_hp"]
    player.attack = data["attack"]
    player.level = data["level"]
    player.exp = data["exp"]
    player.gold = data["gold"]
    player.potions = data["potions"]

    dungeon = Dungeon()
    dungeon.floor = data["floor"]

    return player, dungeon


def battle(player, enemy):
    print("\nA battle begins!")

    while player.hp > 0 and enemy.hp > 0:

        print("\n1. Attack")
        print("2. Heal")

        choice = input("> ")

        if choice == "1":
            damage = random.randint(
                player.attack - 5,
                player.attack + 5
            )

            enemy.hp -= damage

            print(
                f"\nYou hit the {enemy.name} "
                f"for {damage} damage!"
            )

        elif choice == "2":
            player.heal()

        else:
            print("Invalid action.")
            continue

        if enemy.hp <= 0:
            print(f"\nYou defeated {enemy.name}!")

            exp_gain = enemy.level * 20
            gold_gain = enemy.level * 15

            player.gain_exp(exp_gain)

            player.gold += gold_gain

            print(
                f"Found {gold_gain} gold!"
            )

            return True

        enemy_damage = random.randint(
            enemy.attack - 2,
            enemy.attack + 2
        )

        player.hp -= enemy_damage

        print(
            f"{enemy.name} attacks "
            f"for {enemy_damage} damage!"
        )

        print(
            f"Your HP: "
            f"{max(player.hp,0)}"
        )

    return False


def treasure_room(player):
    print("\nTREASURE ROOM!")

    reward = random.randint(1, 4)

    if reward == 1:
        gold = random.randint(50, 120)
        player.gold += gold

        print(
            f"You found {gold} gold!"
        )

    elif reward == 2:
        player.potions += 2

        print(
            "You found 2 potions!"
        )

    elif reward == 3:
        player.attack += 2

        print(
            "Attack permanently increased!"
        )

    else:
        player.max_hp += 10
        player.hp += 10

        print(
            "Max HP permanently increased!"
        )


def shop(player):
    while True:
        print("\n=== SHOP ===")
        print("1. Potion (30 Gold)")
        print("2. Attack Upgrade (100 Gold)")
        print("3. Leave")

        choice = input("> ")

        if choice == "1":
            if player.gold >= 30:
                player.gold -= 30
                player.potions += 1

                print("Potion purchased.")
            else:
                print("Not enough gold.")

        elif choice == "2":
            if player.gold >= 100:
                player.gold -= 100
                player.attack += 3

                print("Attack upgraded.")
            else:
                print("Not enough gold.")

        elif choice == "3":
            break


def random_event(player, dungeon):
    event = random.randint(1, 100)

    if event <= 50:
        enemy = Enemy(dungeon.floor)

        enemy.display()

        victory = battle(
            player,
            enemy
        )

        if not victory:
            print(
                "\nYou were defeated..."
            )
            return False

    elif event <= 75:
        treasure_room(player)

    elif event <= 90:
        shop(player)

    else:
        print(
            "\nA peaceful room."
        )

        heal = random.randint(
            10,
            25
        )

        player.hp = min(
            player.max_hp,
            player.hp + heal
        )

        print(
            f"Recovered {heal} HP."
        )

    return True


def boss_battle(player, dungeon):
    print("\nBOSS FLOOR!")

    boss = Enemy(
        dungeon.floor + 3
    )

    boss.name = "Dungeon Lord"

    boss.hp *= 2
    boss.attack += 8

    boss.display()

    return battle(player, boss)


def main_menu():
    print("\n====================")
    print("DUNGEON EXPLORER RPG")
    print("====================")
    print("1. New Game")
    print("2. Load Game")
    print("3. Quit")

    return input("> ")


def game_loop(player, dungeon):

    while True:

        print(
            f"\n===== FLOOR "
            f"{dungeon.floor} ====="
        )

        player.display()

        print("\n1. Explore")
        print("2. Save")
        print("3. Quit")

        choice = input("> ")

        if choice == "1":

            if dungeon.floor % 5 == 0:

                victory = boss_battle(
                    player,
                    dungeon
                )

                if not victory:
                    print(
                        "\nGame Over."
                    )
                    break

                print(
                    "\nBoss defeated!"
                )

            else:
                alive = random_event(
                    player,
                    dungeon
                )

                if not alive:
                    break

            dungeon.next_floor()

        elif choice == "2":
            save_game(
                player,
                dungeon
            )

        elif choice == "3":
            print(
                "\nThanks for playing!"
            )
            break


def start_game():

    while True:

        choice = main_menu()

        if choice == "1":

            name = input(
                "\nHero name: "
            )

            player = Player(name)

            dungeon = Dungeon()

            game_loop(
                player,
                dungeon
            )

        elif choice == "2":

            player, dungeon = load_game()

            if player is None:
                print(
                    "\nNo save file found."
                )
            else:
                print(
                    "\nSave loaded."
                )

                game_loop(
                    player,
                    dungeon
                )

        elif choice == "3":
            break

        else:
            print(
                "Invalid choice."
            )


if __name__ == "__main__":
    start_game()