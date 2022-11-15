import random
from random import randint
from math import fabs

key_list = ['w', 'a', 's', 'd']


class room:
    def __init__(self):
        self.X = random.randint(5, 10)
        self.Y = random.randint(5, 10)
        self.matrix = [[' '] * self.X for i in range(self.Y)]

    def generation(self):
        self.Y0 = random.randint(1, self.Y - 2)
        self.X0 = 1
        self.exit = [self.X, random.randint(1, self.Y - 2)]
        self.input = [0, self.Y0]
        self.matrix[self.Y0][self.X0] = '๏'
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if i == 0 or j == 0 or i == len(self.matrix) - 1 or j == len(self.matrix[i]) - 1:
                    self.matrix[i][j] = '╬'
        self.matrix[self.input[1]][self.input[0]] = ' '
        self.matrix[self.exit[1]][self.X - 1] = ' '
        self.cord0 = [self.X0, self.Y0]
        self.cord = [self.X, self.Y]
        """
        начальная кордината монстра
        """
        while True:
            self.Y0_monster0 = random.randint(1, self.Y - 2)
            self.X0_monster0 = random.randint(1, self.X - 2)
            self.cord_monster0 = [self.X0_monster0, self.Y0_monster0]
            if self.matrix[self.cord_monster0[1]][self.cord_monster0[0]] != '๏':
                self.matrix[self.cord_monster0[1]][self.cord_monster0[0]] = '☿'
                break

    def update_character(self, new_cord):
        self.matrix[self.Y0][self.X0] = ' '
        self.Y0 = new_cord[1]
        self.X0 = new_cord[0]
        self.matrix[self.Y0][self.X0] = '๏'

    def update_monster(self, new_cord_monster, alive_or_ded):
        self.matrix[self.Y0_monster0][self.X0_monster0] = ' '
        if alive_or_ded == 'жив':
            self.Y0_monster0 = new_cord_monster[1]
            self.X0_monster0 = new_cord_monster[0]
            self.matrix[self.Y0_monster0][self.X0_monster0] = '☿'

    def display(self):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')

            print()
        print()


class Character:
    def __init__(self, name, type_of_person):
        self.type_of_person = type_of_person
        self.name = name
        self.health = 0
        self.armor = 0
        self.attack_range = 0
        self.attack_damage = 0
        self.coords = None  # хрен знает, может убрать?
        self.speed = 0

    def get_health(self):
        if self.type_of_person == ('человек' or 'Человек'):
            self.health = 100
        elif self.type_of_person == ('эльф' or 'Эльф'):
            self.health = 90
        elif self.type_of_person == ('гном' or 'Гном'):
            self.health = 120
        return self.health

    def get_armor(self):
        if self.type_of_person == ('человек' or 'Человек'):
            self.armor = 10
        elif self.type_of_person == ('эльф' or 'Эльф'):
            self.armor = 8
        elif self.type_of_person == ('гном' or 'Гном'):
            self.armor = 12
        return self.armor

    def get_speed(self):
        if self.type_of_person == ('человек' or 'Человек'):
            self.speed = 5
        elif self.type_of_person == ('эльф' or 'Эльф'):
            self.speed = 8
        elif self.type_of_person == ('гном' or 'Гном'):
            self.speed = 3
        return self.speed

    def get_damage_range(self):
        if self.type_of_person == ('человек' or 'Человек'):
            self.attack_range = 1
        elif self.type_of_person == ('эльф' or 'Эльф'):
            self.attack_range = 2
        elif self.type_of_person == ('гном' or 'Гном'):
            self.attack_range = 1
        return self.attack_range

    def get_attack_damage(self):
        if self.type_of_person == ('человек' or 'Человек'):
            self.attack_damage = 20
        elif self.type_of_person == ('эльф' or 'Эльф'):
            self.attack_damage = 25
        elif self.type_of_person == ('гном' or 'Гном'):
            self.attack_damage = 22
        return self.attack_damage

    def start_attack(self):
        return True


    def start_defence(self, another):
        number = random.randint(0, 20)
        if self.armor >= number:
            self.health += another.attack_damage
            print(f'Защита проведена успешно, здоровье персонажа: {self.health}')

    """
    последствие атаки
    """
    def attack_result(self, another):
        number = random.randint(0, 30)
        if number < 25:
            another.health -= self.attack_damage
        elif number >= 25:
            another.health -= 2 * self.attack_damage  # это шанс на критический урон
            print("Нанесён критический урон")

    def take_item(self):
        """
        прописать про дистанцию между персонажем и предметом, если она <=1
        то персонаж может его поднять. Пока не знаю как связать этот класс и класс предметов
        """

    def move(self, direction, cord0, cord, exit, input, cord_monster0):
        cord1 = [cord0[0], cord0[1]]
        if direction == ('w' or 'W'):
            cord0[1] -= 1
        elif direction == ('a' or 'A'):
            cord0[0] -= 1
        elif direction == ('s' or 'S'):
            cord0[1] += 1
        elif direction == ('d' or 'D'):
            cord0[0] += 1
        else:
            print('Некорректное направление')

        if exit[0] - 1 == cord0[0] and exit[1] == cord0[1]:
            pass
        elif input[0] == cord0[0] and input[1] == cord0[1]:
            pass
        elif cord0[1] < cord[1] - 1 and cord0[0] < cord[0] - 1 and cord0[1] >= 1 and cord0[0] >= 1:
            pass
        else:
            cord0[0] = cord1[0]
            cord0[1] = cord1[1]
        if cord0[0] == cord_monster0[0] and cord0[1] == cord_monster0[1]:
            cord0[0] = cord1[0]
            cord0[1] = cord1[1]
        return cord0


class Monster(Character):
    def __init__(self, name_monster):
        self.name_monster = name_monster
        self.health = 0
        self.armor = 0
        self.attack_damage = 0
        self.attack_range = 0
        self.speed = 0

    def get_monster_health(self):
        if self.name_monster == 'Гоблин':
            self.health = 40
        elif self.name_monster == 'Орк':
            self.health = 80
        elif self.name_monster == 'Разбойник':
            self.health = 55
        return self.health

    def get_monster_damage(self):
        if self.name_monster == 'Гоблин':
            self.attack_damage = 5
        elif self.name_monster == 'Орк':
            self.attack_damage = 20
        elif self.name_monster == 'Разбойник':
            self.attack_damage = 15
        return self.attack_damage

    def get_monster_range(self):
        if self.name_monster == 'Гоблин':
            self.attack_range = 1
        elif self.name_monster == 'Орк':
            self.attack_range = 1
        elif self.name_monster == 'Разбойник':
            self.attack_range = 2
        return self.attack_range

    def get_monster_armor(self):
        if self.name_monster == 'Гоблин':
            self.armor = 3
        elif self.name_monster == 'Орк':
            self.armor = 8
        elif self.name_monster == 'Разбойник':
            self.armor = 4
        return self.armor

    def get_monster_speed(self):
        if self.name_monster == 'Гоблин':
            self.speed = 1
        elif self.name_monster == 'Орк':
            self.speed = 1
        elif self.name_monster == 'Разбойник':
            self.speed = 2
        return self.speed

    def move(self, cord_monster0, cord, new_cord):
        cord_monster1 = [cord_monster0[0], cord_monster0[1]]
        global key_list, direction

        if (fabs(cord_monster0[0] - new_cord[0]) <= 3 and fabs(
                cord_monster0[1] - new_cord[1]) <= 3):  # здесь задаётся радиус обнаружения
            if cord_monster0[0] > new_cord[0]:
                cord_monster0[0] -= 1
            elif cord_monster0[0] < new_cord[0]:
                cord_monster0[0] += 1
            elif cord_monster0[1] > new_cord[1]:
                cord_monster0[1] -= 1
            elif cord_monster0[1] < new_cord[1]:
                cord_monster0[1] += 1
        else:
            direction = random.choices(key_list)[0]
            if direction == 'w':
                cord_monster0[1] -= 1
            elif direction == 'a':
                cord_monster0[0] -= 1
            elif direction == 's':
                cord_monster0[1] += 1
            elif direction == 'd':
                cord_monster0[0] += 1

        if cord_monster0[1] < cord[1] - 1 and cord_monster0[0] < cord[0] - 1 and cord_monster0[1] >= 1 and \
                cord_monster0[0] >= 1:
            pass
        else:
            cord_monster0[0] = cord_monster1[0]
            cord_monster0[1] = cord_monster1[1]
        if cord_monster0[0] == new_cord[0] and cord_monster0[1] == new_cord[1]:
            cord_monster0[0] = cord_monster1[0]
            cord_monster0[1] = cord_monster1[1]

        return cord_monster0

    def alive_or_ded(self):
        if self.health <= 0:
            return 'мёртв'
        else:
            return 'жив'


class Items:
    def __init__(self, room, value, rare):
        self.room = room
        self.value = value
        self.rare = rare  # тут будет редкость с рандомом вероятности появления предмета

    def parametres(self, name_item):
        if name_item == 'Кинжал':
            damage_item = 5
            Character.take_item()


def main():
    global type_of_person
    print('''Добро пожаловать в подземелье, 
Выбор расы во многом поможет Вам справиться с трудностями
Отличительные черты человека: защита и урон; эльфа - скорость, а гнома - уровень здооровья''')
    rases = ['человек', 'Человек', 'эльф', 'Эльф', 'гном', 'Гном']
    type_of_person = str(input(f'Выберите расу персонажа: человек, эльф или гном '))

    if type_of_person not in rases:
        while type_of_person not in rases:
            print("Вы некорректно выбрали расу персонажа ")
            type_of_person = str(input(f'Выберите расу персонажа: человек, эльф или гном '))

    name_person = input('Назовите Вашего персонажа: ')

    person1 = Character(name_person, type_of_person)  # создаём экземпляр класса
    person1.get_armor()
    person1.get_attack_damage()
    person1.get_damage_range()
    person1.get_speed()
    person1.get_health()

    print(f'''Имя: {person1.name}, уровень жизни : {person1.health}, уровень защиты: {person1.armor}, 
дальность атаки: {person1.attack_range}, урон: {person1.attack_damage} и скорость: {person1.speed}''')

    list_enemy = ('Гоблин', 'Орк', 'Разбойник')
    name_enemy = random.choice(list_enemy)
    monster = Monster(name_enemy)
    monster.get_monster_health()
    monster.get_monster_damage()
    monster.get_monster_armor()
    monster.get_monster_range()
    monster.alive_or_ded()

    rooms = [0] * 3
    for i in range(3):
        rooms[i] = room()
        rooms[i].generation()
        rooms[i].display()
        n = i

        while True:
            """
            необходимо реализовать нормальную боёвку и стремление монстра убить персонажа, 

            """

            if (fabs(rooms[n].X0_monster0 - rooms[n].X0) <= monster.attack_range) and (
                    fabs(rooms[n].Y0_monster0 - rooms[n].Y0) <= monster.attack_range) and monster.health > 0:
                monster.start_attack()
                monster.attack_result(person1)
                print(f'Здоровье персонажа после атаки: {person1.health}')

            if (fabs(rooms[n].X0_monster0 - rooms[n].X0) <= person1.attack_range) and (
                    fabs(rooms[n].Y0_monster0 - rooms[n].Y0) <= person1.attack_range):
                if  input('Желаете напасть на врага? Если да - нажмите f, если хотите защититься - нажмите g') == ('f' or 'F'):
                    person1.start_attack()
                    person1.attack_result(monster)
                    print(f'Здоровье монстра после атаки: {monster.health}')
                elif input() == ('g' or 'G') and monster.start_attack:
                    person1.start_defence(monster)

            new_cord = person1.move(input('Введите напраление "w", "a", "s", "d"'), rooms[n].cord0, rooms[n].cord,
                                    rooms[n].exit, rooms[n].input, rooms[n].cord_monster0)
            if monster.health > 0:
                print(f'Вы видите в комнате {monster.name_monster}')
                new_cord_monster = monster.move(rooms[n].cord_monster0, rooms[n].cord, new_cord)

            if person1.health <= 0:
                print('Вы погибли, игра закончена')
                raise SystemExit

            print(f'Ваши новые координаты после шага: {new_cord}')
            print(f'Координаты монстра{new_cord_monster}')

            rooms[n].update_character(new_cord)
            print(monster.name_monster, monster.alive_or_ded())
            rooms[n].update_monster(new_cord_monster, monster.alive_or_ded())

            if rooms[n].input[0] == rooms[n].cord0[0] and rooms[n].input[1] == rooms[n].cord0[1] and n != 0:
                n = n - 1

            elif rooms[n].exit[0] - 1 == rooms[n].cord0[0] and rooms[n].exit[1] == rooms[n].cord0[1]:
                n = n + 1

            if rooms[i].exit[0] - 1 == rooms[i].cord0[0] and rooms[i].exit[1] == rooms[i].cord0[1]:
                break
            rooms[n].display()
            print(f'В конце хода у Вас: {person1.health} здоровья')
    print('ВЫ ПОБЕДИЛИ !!!')

main()