"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""
from time import sleep
class Hero:
    def __init__(self, name, health, armor, power, weapon) -> None:
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Поприветствуйте героя ->', self.name)
        print('Уровень здоровья:', self.health)
        print('Уровень брони:', self.armor)
        print('Уровень силы:', self.power)
        print('Текущее оружие:', self.weapon)

    def strike(self, enemy):
        print(
            '-> УДАР! ' + self.name + ' атакует ' + enemy.name +
            ' с силой ' + str(self.power) + ', используя ' + self.weapon + '\n')
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(
            enemy.name + ' покачнулся(-ась).\nКласс брони упал до '
            + str(enemy.armor) + ', а уровень здоровья до '
            + str(enemy.health) + '\n')

class Magician(Hero):
    def hello(self):
        print('-> НОВЫЙ ГЕРОЙ. С магической тростью появился маг по имени', self.name)
        self.print_info()
        sleep(4)
    def attack(self, enemy):
        print('-> УДАР! Маг', self.name, 'атакует', enemy.name, f'{self.weapon}!')
        enemy.armor -= 16
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print('Мощный взрыв поразил противника. \nТеперь его броня: '+str(enemy.armor) + ', а уровень здоровья: ' + str(enemy.health) + '\n')
        sleep(5)