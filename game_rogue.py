import random
from random import randint

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


    def apdate(self,new_cord):
        self.matrix[self.Y0][self.X0] = ' '
        self.Y0 =  new_cord[1]
        self.X0 = new_cord[0]
        self.matrix[self.Y0][self.X0] = '1'





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
        if self.type_of_person == 'человек' or 'Человек':
            self.health = 100
        elif self.type_of_person == 'эльф' or 'Эльф':
            self.health = 90
        elif self.type_of_person == 'гном' or 'Гном':
            self.health = 120
        return self.health

    def get_armor(self):
        if self.type_of_person == 'человек' or 'Человек':
            self.armor = 10
        elif self.type_of_person == 'эльф' or 'Эльф':
            self.armor = 8
        elif self.type_of_person == 'гном' or 'Гном':
            self.armor = 12
        return self.armor

    def get_speed(self):
        if self.type_of_person == 'человек' or 'Человек':
            self.speed = 5
        elif self.type_of_person == 'эльф' or 'Эльф':
            self.speed = 8
        elif self.type_of_person == 'гном' or 'Гном':
            self.speed = 3
        return self.speed

    def get_damage_range(self):
        if self.type_of_person == 'человек' or 'Человек':
            self.attack_range = 1
        elif self.type_of_person == 'эльф' or 'Эльф':
            self.attack_range = 2
        elif self.type_of_person == 'гном' or 'Гном':
            self.attack_range = 1
        return self.attack_range

    def get_attack_damage(self):
        if self.type_of_person == 'человек' or 'Человек':
            self.attack_damage = 20
        elif self.type_of_person == 'эльф' or 'Эльф':
            self.attack_damage = 25
        elif self.type_of_person == 'гном' or 'Гном':
            self.attack_damage = 22
        return self.attack_damage

"""тут я хочу прописать метод атаки персонажа"""
    #def start_attack (self):


def move(direction, cord0, cord, exit,
         input):  # direction - это направление движения, которое можно реализовать в main цикле
    cord1 = [cord0[0], cord0[1]]
    if direction == 'w':
        cord0[1] -= 1
    elif direction == 'a':
        cord0[0] -= 1
    elif direction == 's':
        cord0[1] += 1
    elif direction == 'd':
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
    def __init__(self, name, health, armor, attack_range, attack_damage, speed, radius_finding):
        self.health = health
        self.radius_finding  = radius_finding

class Items:
    def __init__(self, room, value, rare):
        self.room = room
        self.value = value
        self.rare = rare #тут будет редкость с рандомом вероятности появления предмета

    def parametres(self, name_item):
        if name_item == 'Кинжал':
            damage_item = 5

def main():
    global type_of_person
    print('''Добро пожаловать в подземелье, 
Выбор расы во многом поможет Вам справиться с трудностями
Отличительные черты человека: защита и урон, эльфа - скорость, а гнома - уровень здооровья''')

    type_of_person = str(input(f'Выберите расу персонажа: человек, эльф или гном '))
    name_person= input('Назовите Вашего персонажа: ')

    """if type_of_person == 'человек' or 'Человек':
        person1 = Character(name_person, 100, 10, 1, 20, 5)
    elif type_of_person == 'эльф' or 'Эльф':
        person1 = Character(name_person, 90, 10, 2, 25, 7)
    elif type_of_person == 'гном' or 'Гном':
        person1 = Character(name_person, 120, 12, 1, 22, 3)"""
    person1 = Character(name_person, type_of_person)
    print(person1.health)

    print('''Имя: {},уровень жизни : {}, уровень защиты: {}, дальность атаки: {}, урон: {} и скорость: {}
            '''.format(person1.name, person1.health, person1.armor, person1.attack_range, person1.attack_damage, person1.speed))


    rooms = [0]*3
    for i in range(3):
        rooms[i] = room()
        rooms[i].generation()
        rooms[i].display()
        n = i
        while True:
            new_cord = move(input('Введите напраление "w", "a", "s", "d"'), rooms[n].cord0, rooms[n].cord, rooms[n].exit, rooms[n].input)
            rooms[n].apdate(new_cord)
            if rooms[n].input[0]==rooms[n].cord0[0] and rooms[n].input[1]==rooms[n].cord0[1] and n!=0:
                n=n-1

            elif rooms[n].exit[0] - 1 == rooms[n].cord0[0] and rooms[n].exit[1] == rooms[n].cord0[1]:
                n = n + 1





            if rooms[i].exit[0] - 1 == rooms[i].cord0[0] and rooms[i].exit[1] == rooms[i].cord0[1]:
                break
            rooms[n].display()
    print('Вы поюедили!!')

main()


