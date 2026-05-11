from abc import ABC, abstractmethod

class Hero(ABC):

    def __init__(self, name, lvl, hp, strength):
        self.name = name
        self.lvl = lvl
        self.__hp = hp
        self.strength = strength

    def greet(self):
        print(f"Hello I'm {self.name}, my level is {self.lvl}")

    def rest(self):
        print(f"{self.name} resting! ")
        self.__hp += 1
        print(f"health is healing, status hp: {self.__hp}")

    def get_hp(self):
        return self.__hp

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def __init__(self, name, lvl, hp, strength):
        self.name = name
        self.lvl = lvl
        self.__hp = hp
        self.strength = strength
        super().__init__(name, lvl, hp, strength)

    def attack(self):
        print(f"{self.name} attacking by sword! ")

class Mage(Hero):
    def __init__(self, name, lvl, hp, strength):
        self.name = name
        self.lvl = lvl
        self.__hp = hp
        self.strength = strength
        super().__init__(name, lvl, hp, strength)

    def attack(self):
        print(f"{self.name} attacking, using magic! ")

class Assasin(Hero):
    def __init__(self, name, lvl, hp, strength):
        self.name = name
        self.lvl = lvl
        self.__hp = hp
        self.strength = strength
        super().__init__(name, lvl, hp, strength)


    def attack(self):
        print(f"{self.name} attacking from stealth! ")
print()
warrior = Warrior("John Wuik", 75, 1000, 1200)
mage = Mage("Harry Potter", 5, 25, 85)
assasin = Assasin("Hitman", 10, 800, 1000)

print()
warrior.greet()
mage.greet()
assasin.greet()

print()
warrior.attack()
mage.attack()
assasin.attack()
print(f"{warrior.name} health status: {warrior.get_hp()}")
print(f"{mage.name} health status: {mage.get_hp()}")
print(f"{assasin.name} health: {assasin.get_hp()}")

print()
warrior.rest()
mage.rest()
assasin.rest()
print()
print(f"{warrior.name} health status: {warrior.get_hp()}")
print(f"{mage.name} health status: {mage.get_hp()}")
print(f"{assasin.name} health: {assasin.get_hp()}")