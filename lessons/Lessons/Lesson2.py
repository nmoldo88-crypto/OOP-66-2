class Hero:
    def __init__(self,name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl

    def action(self):
        print(self.name)
        print(self.hp)
        print(self.lvl)
          