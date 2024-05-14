import random
class BigCat:
    def __init__(self):
        self.speed = 5
        self.strength = 5
        self.intelligence = 5
        self.health = 5
        self.durability = 5

class Lion(BigCat):
    def __init__(self):
        super().__init__()
        self.strength = 50
        self.health = 50

    def King(self, target):
        target.speed = 0
        target.strength = 0
        target.intelligence = 0
        target.health = 0
        target.durability = 0
        print("Lion wins")

class Leopard(BigCat):
    def __init__(self):
        super().__init__()
        self.strength = 30
        self.intelligence = 30
        self.health = 30

    def attack(self, target):
        if isinstance(target, Lion):
            target.King(self)
        else:
            target.health -= 15
            print("Leopard is hit")


class Cheetah(BigCat):
    def __init__(self):
        super().__init__()
        self.speed = 75
        self.strength = 25
        self.intelligence = 25
        self.health = 25
        self.durability = 25

    def run(self, target):
     while True:
        action = input("Type 'run' or 'stay': ")
        if action == 'run':
            if isinstance(target, Leopard):
                if random.random() <= 0.6:
                    print("Cheetah got away!")
                else:
                    print("Cheetah gets away, but took a hit.")
                    target.health -= 2
            elif isinstance(target, Lion):
                target.King(self)
            else:
                if random.random() <= 0.6:
                    print("Cheetah got away!")
                else:
                    print("Cheetah gets away, but took a hit.")
                    target.health -= 20
        elif action == 'stay':
            print("Cheetah stays put and gets hit")
            target.health -= 10
        else:
            print("Invalid Choice. Cheetah doesn't move and takes hit.")
            target.health -= 10



Lion_obj = Lion()
Leopard_obj = Leopard()
Cheetah_obj = Cheetah()

while True:
    Cheetah_obj.run(Leopard_obj)
    if Leopard_obj.health <= 0:
        print("Leopard Loses to Cheetah!")

    Leopard_obj.attack(Lion_obj)
    if Lion_obj.health <= 0:
        print("Lion Loses to Leopard!")

    Lion_obj.King(Cheetah_obj)
    if Cheetah_obj.health <= 0:
        print("Cheetah loses to Lion")

