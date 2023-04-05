"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""
class Hero:
    def __init__(self, name, health, armor, power, weapon, rank) -> None:
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.__rank = rank

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
        if enemy.health <= 0: self.setrank('Победитель арены')
        elif self.health <= 0: self.delrank()

    def getrank(self):
        return self.__rank

    def setrank(self, newrank):
        self.__rank = newrank

    def delrank(self):
        del self.__rank0

knight = Hero('Ричард', 50, 25, 20, 'меч', '444')
knight.print_info()
rascal = Hero('Хелен', 20, 5, 5, 'лук', '444')
rascal.print_info()
knight.strike(rascal)