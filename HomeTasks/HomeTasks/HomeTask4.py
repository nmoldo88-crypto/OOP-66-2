# 📝 Домашнее
# задание №4
#
# Тема: Магические методы в классах
# 🎯 Цель
#
# Закрепить работу с магическими методами:
# __add__
# __sub__
# __mul__
# __truediv__  и научиться работать с логикой внутри класса.
#
# 📌 Задание
# Создайте класс Money.
#
# 🔹 Атрибуты класса В конструкторе должны быть два атрибута:
# amount — сумма денег
# currency — валюта
# Пример:
# money1 = Money(100, "USD")
# money2 = Money(5000, "KGS")
#
# 🔹 Курсы валют В началe файла создайте словарь курсов валют относительно сома.
#
# Пример:
# rates = {
#     "KGS": 1,
#     "USD": 89,
#     "EUR": 96,
#     "RUB": 1.2
# }
#
# Где:
# ключ — валюта
# значение — сколько сомов стоит 1 единица валюты
#
# 🔹 Метод конвертации В классе должен быть метод:
#
# convert_to_kgs()
#
# Этот метод должен переводить любую валюту в сомы.
#
# Пример:
#
# 100 USD → 8900 KGS
#
# 🔹 Магические методы
# Реализуйте следующие магические методы:
#
# __add__
# Сложение денег.
#
# money1 + money2
#
# Если валюты разные, сначала нужно конвертировать их в сомы, затем выполнить сложение.
# __sub__
#
# Вычитание денег.
#
# money1 - money2
# Также нужно учитывать конвертацию валют.
#
# __mul__
#
# Умножение денег на число.
#
# Пример: money * 3
# __truediv__
#
# Деление денег на число.
#
# Пример: money / 2
#
# 🔹 Метод
# __str__
# Чтобы объект красиво выводился.
#
# Пример: print(money)
#
# Вывод: 100 USD
#
# 📌 Пример использования
#
# money1 = Money(100, "USD")
# money2 = Money(5000, "KGS")
#
# result = money1 + money2
#
# print(result)
rates = {
    "KGS": 1,
    "USD": 87.45,
    "EUR": 102.73,
    "RUB": 1.19
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency



    def convert_to_kgs(self):
        return float(self.amount * rates[self.currency])




    def __add__(self, other):
        total_kgs = self.convert_to_kgs() + other.convert_to_kgs()
        return Money(total_kgs / rates[self.currency], self.currency)

        # money1.self = self
        # money2.other = other

# money1 + money2
    def __sub__(self, other):
        total_kgs = self.convert_to_kgs() - other.convert_to_kgs()
        return Money(total_kgs / rates[self.currency], self.currency)

        # money1.self = self
        # money2.other = other

# money1 - money2

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        return NotImplemented




# money1.self = self
# money2.other = other
# money1 * 3

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount / other, self.currency)
        return NotImplemented
        # money1.self = self
        # money2.other = other

    def __str__(self):
        return f"{self.amount} {self.currency}"


# result = money1 + money2
#         print(result)

money1 = Money(100, "USD")
money2 = Money(5000, "KGS")
# print(money1)
# print(money2)
print(f"money1: {money1}")
print(f"money2: {money2}")
print(f"100 USD в сомах: {money1.convert_to_kgs()} KGS")
print(f"5000 KGS в долларах: {money2.amount / rates['USD']:.2f} USD")
print()

# Сложение
result = money1 + money2
print(f"{money1} + {money2} = {result}")

# Вычитание
result = money1 - money2
print(f"{money1} - {money2} = {result}")

# Умножение
result = money1 * 3
print(f"{money1} * 3 = {result}")

# Деление
result = money1 / 2
print(f"{money1} / 2 = {result}")
# 100 USD -> 87450 KGS