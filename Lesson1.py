# print(Kirito.name)
# print(Kirito.lvl)
# print(Kirito.hp)
# class Hero:
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp

    # def __init__(self, name = "John Doe", lvl = 0, hp = 100):
    #     self.name = name
    #     self.lvl = lvl
    #     self.hp = hp
#
    # def action(self):
    #     return "Just method"
# kirito = Hero()

# print(kirito.action())
# Kirito = Hero("Kirito", 100, 1000)
# asuna = Hero("Asuna", 101, 1001)
# class MyInt:
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return str(self.value)
#
# # print(my_list)
# # print(my_int)
# my_int = MyInt(123)
# py_int = 123
# my_list = list([1,2,3,45])
# print(my_int)
# print(py_int)
# print(my_list)
#
# my_list = list([1,2,3,45])
# my_tuple = tuple([1,2,3,45])
# print(my_list)
# print(my_tuple)
class Hero:
    def __init__(self, name = "John Doe", lvl = 0, hp = 100):
        self.name = name
        self.lvl = lvl
        self.hp = hp


    def action(self):
        return f"{self.name} base action!"


kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 101, 1001)
print(kirito.action())
print(asuna.action())