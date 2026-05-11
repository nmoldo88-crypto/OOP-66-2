# Что нужно сделать
# ✅ 1. Создать базовый класс Hero
# У героя должны быть:
# name — имя
#
#
# lvl — уровень
#
#
# hp — здоровье
# Метод:
# action() — выводит строку:
#  "{name} готов к бою!"

# ✅ 2. Создать два дочерних класса
# MageHero — наследник Hero
# Дополнительно:
# mp — мана
# Переопределить метод action() так, чтобы вывод был:
#  "Маг {name} кастует заклинание! MP: {mp}"WarriorHero — наследник MageHero (!)
# Переопределить action() так:
 # "Воин {name} рубит мечом! Уровень: {lvl}"


from abc import ABC, abstractmethod


# Task 1-3: Hero classes
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} готов к бою!")


class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")


class WarriorHero(Hero):
    def __init__(self, name, lvl, hp):
        super().__init__(name, lvl, hp)

    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")


# Task 3: BankAccount with encapsulation
class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance  # Protected attribute
        self.__password = password  # Private attribute
        self.bank_name = bank_name

    def login(self, password):
        """Checks if password matches"""
        return password == self.__password

    @property
    def full_info(self):
        """Read-only property"""
        return f"Герой: {self.hero.name}, Уровень: {self.hero.lvl}, Баланс: {self._balance}"

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    # Task 4: Magic method __str__
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    # Task 4: Magic method __add__
    def __add__(self, other):
        # Check if heroes are of the same class
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        else:
            raise TypeError("Ошибка: Нельзя сложить счета героев разных классов!")

    # Task 4: Magic method __eq__
    def __eq__(self, other):
        # Heroes are equal if they have same class and level
        return (type(self.hero) == type(other.hero)) and (self.hero.lvl == other.hero.lvl)


# Task 5: Abstract SmsService
class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        """Send OTP code to phone number - must be implemented"""
        pass


class KGSms(SmsService):
    def send_otp(self, phone):
        """Returns XML-like string format"""
        return f"<text>Код: 1234</text><phone>{phone}</phone>"


class RUSms(SmsService):
    def send_otp(self, phone):
        """Returns dictionary format"""
        return {"text": "Код: 1234", "phone": phone}


# Testing the complete solution
if __name__ == "__main__":
    # Create heroes
    mage1 = MageHero("Merlin", 80, 500, 150)
    mage2 = MageHero("Merlin", 80, 500, 200)
    warrior = WarriorHero("Conan", 50, 900)

    # Create bank accounts
    acc1 = BankAccount(mage1, 5000, "1234", "Simba")
    acc2 = BankAccount(mage2, 3000, "0000", "Simba")
    acc3 = BankAccount(warrior, 2500, "1111", "Simba")

    # Test actions
    mage1.action()
    warrior.action()

    # Test __str__ magic method
    print(acc1)
    print(acc2)

    # Test class/static methods
    print("Банк:", acc1.get_bank_name())
    print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

    # Test __add__ magic method
    print("\n=== Проверка __add__ ===")
    try:
        result = acc1 + acc2
        print("Сумма счетов двух магов:", result)
    except TypeError as e:
        print(e)

    try:
        result = acc1 + acc3
        print("Сумма мага и воина:", result)
    except TypeError as e:
        print(e)

    # Test __eq__ magic method
    print("\n=== Проверка __eq__ ===")
    print("Mage1 == Mage2 ?", acc1 == acc2)  # True - same class and level
    print("Mage1 == Warrior ?", acc1 == acc3)  # False

    # Test SMS services
    sms_kgs = KGSms()
    sms_rus = RUSms()

    print("\n", sms_kgs.send_otp("+996777123456"))
    print(sms_rus.send_otp("+996777123456"))


