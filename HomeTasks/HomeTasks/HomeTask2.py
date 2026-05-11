import random


# Родительский класс
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет! Меня зовут {self.name}, мой уровень {self.level}")

    def attack(self):
        damage = self.strength * self.level
        print(f"{self.name} атакует и наносит {damage} урона!")

    def rest(self):
        heal = 10 * self.level
        self.health += heal
        print(f"{self.name} отдыхает и восстанавливает {heal} здоровья.")
        print(f"Текущее здоровье: {self.health}")


# Дочерний класс Warrior
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        damage = (self.strength * self.level) + self.stamina
        print(f"{self.name} атакует мечом и наносит {damage} урона!")


# Дочерний класс Mage
class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        if self.mana >= 10:
            damage = (self.strength * self.level) + self.mana
            self.mana -= 10
            print(f"{self.name} кастует заклинание и наносит {damage} урона!")
            print(f"Осталось маны: {self.mana}")
        else:
            print(f"{self.name} не хватает маны!")


# Дочерний класс Assassin
class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        damage = (self.strength * self.level) + self.stealth
        print(f"{self.name} атакует из-под тишка и наносит {damage} урона!")


# Создаем объекты
warrior = Warrior("Артур", 5, 120, 25, 30)
mage = Mage("Мерлин", 5, 80, 15, 50)
assassin = Assassin("Рико", 5, 90, 20, 40)


# Функция определения победителя
def determine_winner(player, computer):

    # Ничья
    if type(player) == type(computer):
        return "Ничья!"

    # Победы игрока
    elif (
        isinstance(player, Warrior) and isinstance(computer, Assassin)
    ) or (
        isinstance(player, Assassin) and isinstance(computer, Mage)
    ) or (
        isinstance(player, Mage) and isinstance(computer, Warrior)
    ):
        return "Игрок победил!"

    else:
        return "Компьютер победил!"


# Игра
def play_game():

    print("=" * 40)
    print(" Камень, Ножницы, Бумага")
    print("=" * 40)

    print("Выберите героя:")
    print("1 - Warrior")
    print("2 - Mage")
    print("3 - Assassin")

    # Выбор игрока
    while True:
        choice = input("Ваш выбор: ")

        if choice == "1":
            player_hero = warrior
            break

        elif choice == "2":
            player_hero = mage
            break

        elif choice == "3":
            player_hero = assassin
            break

        else:
            print("Введите 1, 2 или 3!")

    # Компьютер выбирает случайного героя
    heroes = [warrior, mage, assassin]
    computer_hero = random.choice(heroes)

    # Вывод выбора
    print(f"Вы выбрали: {type(player_hero).__name__}")
    print(f"Противник: {type(computer_hero).__name__}")

    # Результат
    result = determine_winner(player_hero, computer_hero)

    print("hero" + "=" * 40)
    print(result)
    print("=" * 40)

    # Атака
    print("⚔️ Бой:")
    player_hero.attack()
    computer_hero.attack()


# Запуск игры
play_game()