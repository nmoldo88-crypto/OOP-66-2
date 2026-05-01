# class dog:
#     spesies = "Canis familiars"
#
#
# def __init__(self, name, age):
#
#     self.name = Buddy
#     self.age = 3
#
# def bark(self):
#     print(f"{self.name} says woof!")
#
# def get_age(self):
#     return self.age
#     print(f"{self.name}s age {self.age} likes a milk")
import _xxsubinterpreters


# dog1 = Dog("Buddy", 3)
    # dog2 = Dog("Max", 5)
    # print(dog1.name)
    # print(dog2.age)
    # print(dog1.species)
    # dog1.bark()
    # dog2.bark()

# name = ("Buddy")
# age = 3
# print(f"{name}s age {age} and he likes a milk")
#
# class BankAccount:
#     def __init__(self, owner, balance = 0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited {amount}. New balance: {self.balance}")
#         else:
#             print("Amount must be positive")
#
#     def Withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdraw {amount}. New balnce = {self.balance}")
#         else:
#             print("Insufficient funds or invalid amount")
#
#     def show_balance(self):
#         print(f"{self.owner}s Balance: {self.balance}")
# account = BankAccount("Alice", 100)
# account.deposit(50)
# account.Withdraw(30)
# account.show_balance()

class Hero:
    def __init__(self, name="John Doe", lvl=0, hp=100):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return "Just method"

    # Add a new method (you write this part)
    def introduce(self):
        # Should print: "I am [name], level [lvl], with [hp] HP."
        pass