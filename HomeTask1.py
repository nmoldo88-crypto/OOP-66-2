#
# 📌 Задание
#
# Вам необходимо создать класс Hero со следующими характеристиками:
# 🔹 Атрибуты
# класса: name — имя героя
# level — уровень героя
# health — здоровье героя
# strength — сила героя
# 🔹 Методы
# класса:
#
# 1greet()
# Метод должен выводить сообщение:
# Привет, я{имягероя}, мой уровень {уровень}
#
# 2 attack()
# Метод должен:
# выводить сообщение: {имя героя} наносит удар!
# уменьшать силу героя на
#
# 1rest()
# Метод должен:
# выводить cообщение:{имя героя} отдыхает…
# увеличивать здоровье героя на


class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        return f"Hello I'm {self.name}, my lvl {self.level}, my health: {self.health}, my srength: {self.strength}"


    def attack(self):
        print(f'{self.name} attacking')
        self.strength -= 1

    def rest(self):
        print(f"{self.name} resting")
        self.health += 1




hero = Hero("Palladin", 10, 200, 150)


print(hero.greet())
print(hero.strength)
hero.attack()
print(hero.strength)
hero.rest()
print(hero.greet())

Illidan= Hero("Illidan", 15, 1200, 1500)

print(Illidan.greet())
print(Illidan.strength)
Illidan.attack()
print(Illidan.strength)
Illidan.rest()
print(Illidan.greet())HomeTask

