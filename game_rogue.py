import random
from random import randint
import socket
width = 20
height = 20
width_room = 3
height_room = 3
value_full = '%'
value_empty = '*'

matrix_zero_empty = [['#' for j in range(width)] for i in range(height)]
for y in range(height):
    for x in range(width):
        matrix_zero_empty[x][y] = value_empty
for rows in matrix_zero_empty:
    print(" ".join(rows))

matrix_zero_empty[4][6] = '@'
for rows in matrix_zero_empty:
    print(" ".join(rows))

class Character:
    def __init__(self, name, health, armor, attack_range, attack_damage, speed):
        self.name = name
        self.health = health
        self.armor = armor
        self.attack_range = attack_range
        self.attack_damage = attack_damage
        self.coords = None #хрен знает, может убрать?
        self.speed = speed

    """def rases(self):
        if type_of_person == "человек" or "Человек":
            self.health = 100
            self.armor = 10
            self.speed = 1
            self.attack_damage = 20
            self.attack_range = 1"""


def main():

    print('''Добро пожаловать в подземелье, 
Выбор расы во многом поможет Вам справиться с трудностями
Отличительные черты человека: защита и урон, эльфа - скорость, а гнома - уровень здооровья''')

    type_of_person = input(f'Выберите расу персонажа: человек, эльф или гном ')
    name_person= input('Назовите Вашего персонажа: ')

    if type_of_person == 'человек' or 'Человек':
        person1 = Character(name_person, 100, 10, 1, 20, 5)
    elif type_of_person == 'эльф' or 'Эльф':
        person1 = Character(name_person, 90, 10, 2, 25, 7)
    elif type_of_person == 'гном' or 'Гном':
        person1 = Character(name_person, 120, 12, 1, 22, 3)

    print('''Имя: {},уровень жизни : {}, уровень защиты: {}, дальность атаки: {}, урон: {} и скорость: {}
            '''.format(person1.name, person1.health, person1.armor, person1.attack_range, person1.attack_damage, person1.speed))

main()


