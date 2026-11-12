from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    @property
    def health(self):
        return self.__health

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)

    def attack(self):
        print("Воин атакует мечом")


class Mage(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)

    def attack(self):
        print("Маг использует магию")


class Assassin(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)

    def attack(self):
        print("Ассасин атакует из-под тишка")


warrior = Warrior("Warrior", 10, 100, 50)
mage = Mage("Mage", 15, 80, 40)
assassin = Assassin("Assassin", 12, 90, 60)


heroes = [warrior, mage, assassin]

for hero in heroes:
    print("\n-------------------")
    hero.greet()
    hero.attack()
    hero.rest()
    print("Здоровье:", hero.health)
