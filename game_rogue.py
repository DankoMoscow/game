import random
from random import randint
key_list = ['w', 'a', 's', 'd']

class room:
    def __init__(self):
        self.X = random.randint(5,10)
        self.Y = random.randint(5,10)
        matrix = [[' '] * self.X for i in range(self.Y)]
        self.matrix = matrix

    def generation(self):
        self.Y0 = random.randint(1, self.Y - 2)
        self.X0=1
        self.exit = [self.X,random.randint(1, self.Y - 2)]
        self.input = [0,self.Y0]
        self.matrix[self.Y0][self.X0] = 1
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if i==0 or j ==0 or i == len(self.matrix)-1 or j==len(self.matrix[i])-1:
                    self.matrix[i][j] = 'X'
        self.matrix[self.input[1]][self.input[0]] = ' '
        self.matrix[self.exit[1]][self.X-1] = ' '
        self.cord0 = [self.X0,self.Y0]
        self.cord = [self.X,self.Y]

    def update(self,new_cord, first_coor_monster, second_coor_monster):
        self.matrix[self.Y0][self.X0] = ' '
        self.Y0 =  new_cord[1]
        self.X0 = new_cord[0]
        self.f_coor_monster = first_coor_monster
        self.s_coor_monster = second_coor_monster
        self.matrix[self.Y0][self.X0] = '1'
        self.matrix[self.f_coor_monster][self.s_coor_monster] = '*' #хочу, чтобы звёздочка убиралась на каждой итерации
        return self.Y0 , self.X0
        """
        тут пытаюсь создать обновляющееся поле для монстра
        """

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
        self.coords = None #хрен знает, может убрать?
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

    def start_attack(self, another):
        number = random.randint(0, 30)
        if number <25:
            another.health -= self.attack_damage
        elif number >= 25:
            another.health -= 2 * self.attack_damage #это шанс на критический урон
            print("Вы нанесли критический урон")

    """
    метод защиты, который наследуется монстром в том числе
    """
    def start_defence(self, another):
        number = random.randint(0,20)
        if self.armor >= number:
            self.health += another.attack_damage
        print  (number)

    def take_item(self):
        """
        прописать про дистанцию между персонажем и предметом, если она <=1
        то персонаж может его поднять. Пока не знаю как связать этот класс и класс предметов
        """

#тут будут методы персонажа

    def move(direction, cord0, cord, exit, input):  # direction - это направление движения, которое можно реализовать в main цикле
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
        return cord0


class Monster(Character):
    def __init__(self, name_monster,first_coor_monster, second_coor_monster):
        self.first_coor_monster = first_coor_monster
        self.second_coor_monster = second_coor_monster
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
            self.health = 5
        elif self.name_monster == 'Орк':
            self.health = 20
        elif self.name_monster == 'Разбойник':
            self.health = 15
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

    def move(self):
        global key_list, direction
        direction = random.choices(key_list)[0]
        if direction == 'w':
            if self.second_coor_monster > 1:
                self.second_coor_monster -= 1
            else:
                self.second_coor_monster = self.second_coor_monster

        elif direction == 's':
            if self.second_coor_monster < len(room.matrix):
                self.second_coor_monster += 1
            else:
                self.second_coor_monster = self.second_coor_monster

        elif direction == 'd':
            if self.first_coor_monster < len(room.matrix):
                self.first_coor_monster += 1
            else:
                self.first_coor_monster = self.first_coor_monster

        elif direction == 'a':
            if self.first_coor_monster > 1:
                self.first_coor_monster -= 1
            else:
                self.first_coor_monster = self.first_coor_monster

        return self.first_coor_monster, self.second_coor_monster


class Items:
    def __init__(self, room, value, rare):
        self.room = room
        self.value = value
        self.rare = rare #тут будет редкость с рандомом вероятности появления предмета

    def parametres(self, name_item):
        if name_item == 'Кинжал':
            damage_item = 5
            Character.take_item()

def main():
    global type_of_person
    print('''Добро пожаловать в подземелье, 
Выбор расы во многом поможет Вам справиться с трудностями
Отличительные черты человека: защита и урон; эльфа - скорость, а гнома - уровень здооровья''')

    type_of_person = str(input(f'Выберите расу персонажа: человек, эльф или гном '))
    while type_of_person != ('эльф' or 'Эльф' or 'человек' or 'Человек' or 'гном' or 'Гном'):
        print("Вы некорректно выбрали расу персонажа ")
        type_of_person = str(input(f'Выберите расу персонажа: человек, эльф или гном '))

    name_person= input('Назовите Вашего персонажа: ')

    person1 = Character(name_person, type_of_person) #создаём экземпляр класса
    person1.get_armor()
    person1.get_attack_damage()
    person1.get_damage_range()
    person1.get_speed()
    person1.get_health()

    print(f'''Имя: {person1.name}, уровень жизни : {person1.health}, уровень защиты: {person1.armor}, 
дальность атаки: {person1.attack_range}, урон: {person1.attack_damage} и скорость: {person1.speed}''')

    first_coor_monster_random = random.randint(1, 5) #создаём координаты для рандомного монстра
    second_coor_monster_random = random.randint(1, 5) #создаём координаты для рандомного монстра

    list_enemy = ('Гоблин', 'Орк', 'Разйбойник')
    name_enemy = random.choice(list_enemy)
    monster = Monster(name_enemy, first_coor_monster_random, second_coor_monster_random) #указываем ему его координаты
    monster.get_monster_health()
    monster.get_monster_damage()
    monster.get_monster_armor()
    monster.get_monster_range()

    rooms = [0]*3
    for i in range(3):
        rooms[i] = room()
        rooms[i].generation()
        rooms[i].display()
        n = i
        while True:
            new_cord = Character.move(input('Введите напраление "w", "a", "s", "d"'), rooms[n].cord0, rooms[n].cord, rooms[n].exit, rooms[n].input)
            """
            это боёвка
            """
            button_attack = str(input('Желаете напасть на врага? Если да - нажмите f'))
            if button_attack == ('f' or 'F'):
                if...
                    """тут надо сделать проверку условия, что если дистанция между монстром и игроком
                    #меньше или  оавна person1.range_damage, то можно провести атаку)"""
                    person1.start_attack(monster)
                    print(f'Здоровье монстра после атаки: {monster.health}')
                else:
                    print('Дистанция слишком велика для атаки')
            person1.start_defence(monster) #это должно идти после атаки монстра
            new_cord1, new_cord2 = monster.move()
            rooms[n].update(new_cord, new_cord1, new_cord2)

            if rooms[n].input[0]==rooms[n].cord0[0] and rooms[n].input[1]==rooms[n].cord0[1] and n!=0:
                n=n-1

            elif rooms[n].exit[0] - 1 == rooms[n].cord0[0] and rooms[n].exit[1] == rooms[n].cord0[1]:
                n = n + 1

            if rooms[i].exit[0] - 1 == rooms[i].cord0[0] and rooms[i].exit[1] == rooms[i].cord0[1]:
                break
            rooms[n].display()
    print('ВЫ ПОБЕДИЛИ !!!')

main()
