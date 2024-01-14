import random

NAMES = ['Грит', 'Фрида', 'Грум', 'Ульрих', 'Святослав', 'Борис', 'Глеб', 'Сван', 'Свейн', 'Сигурд', 'Ушак', 'Жир', 'Малой', 'Сухой', 'Головач']


class Person:
    def __init__(self, name, health=100, attack=10, defense=5):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def set_things(things):
        ...

    def display_status(self):
        print(f"{self.name}: Здоровье - {self.health}, Атака - {self.attack}, Защита - {self.defense}")


class Paladin(Person):
    def __init__(self, name, health=200, attack=10, defense=10):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense


class Warrior(Person):
    def __init__(self, name, health=100, attack=20, defense=5):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense


class Thing:
    def __init__(self, name):
        self.name = name
        self.defence = random.randint(0, 10)
        self.attack= random.randint(0, 10)
        self.health=random.randint(0, 10)


CLASSES = [Paladin, Warrior]
fighters = []
for i in range(10):
    fighters.append(random.choice(CLASSES)(random.choice(NAMES)))

pal = Paladin('Pal')
war = Warrior('War')
war2 = Warrior('War2')
fighters2 = [pal, war, war2]


def fight(atacker, defender):
    defender.health = defender.health - (atacker.attack - defender.defense)


if __name__ == '__main__':

    thing_names = ['шапка', 'посох', 'меч', 'щит',
                   'булава', 'лук', 'кинжал','кираса',
                    'копье', 'плащ', 'ожерелье', 'ботинки', 
                    'шлем', 'пояс', 'ножны', 'штаны',
                    'кольцо', 'поножи']
    thing_list=[]

    for i in range(20):
       new_thing=Thing(random.choice(thing_names))
       thing_list.append(new_thing)

    for thing in thing_list:
        print(thing.name, thing.defence, thing.attack, thing.health)

    while len(fighters) > 1:
        atacker, defender = random.sample(fighters, 2)
        fight(atacker, defender)
        print(defender.name, defender.health)
        if defender.health <= 0:
            print(f'{defender.name} умер!')
            fighters.remove(defender)
    print(fighters)
