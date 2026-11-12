import random


class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Воин атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print("Маг кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print("Ассасин атакует из-под тишка!")


warrior = Warrior("Warrior", 10, 100, 50, 80)
mage = Mage("Mage", 15, 80, 40, 100)
assassin = Assassin("Assassin", 12, 90, 60, 95)


heroes = [warrior, mage, assassin]

for hero in heroes:
    print("\n-------------------")
    hero.greet()
    hero.attack()
    hero.rest()
    print("Здоровье:", hero.health)



print("\n===== ИГРА =====")

print("Выберите героя:")
print("1. Warrior")
print("2. Mage")
print("3. Assassin")

choice = input("Ваш выбор: ")

characters = {
    "1": warrior,
    "2": mage,
    "3": assassin
}

if choice not in characters:
    print("Неверный выбор!")
else:
    player = characters[choice]

    opponents = [hero for hero in heroes if hero != player]
    enemy = random.choice(opponents)

    print("\nВы выбрали:", player.name)
    print("Противник:", enemy.name)

    print("\nВаш герой:")
    player.attack()

    print("\nПротивник:")
    enemy.attack()


    if type(player) == type(enemy):
        print("\nНичья!")
    elif isinstance(player, Warrior) and isinstance(enemy, Assassin):
        print("\nВы победили!")
    elif isinstance(player, Assassin) and isinstance(enemy, Mage):
        print("\nВы победили!")
    elif isinstance(player, Mage) and isinstance(enemy, Warrior):
        print("\nВы победили!")
    else:
        print("\nПротивник победил!")
