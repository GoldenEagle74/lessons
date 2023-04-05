"""
Создайте класс Person у которого будут свойства name и age.
Добавьте метод экземпляра который выводит информацию о человеке.
Создайте метод класса который генерирует новый объект класса
который ставить возраст человека: сегодняшний год - год который передают в метод.
(подсказка: тут можно использовать метод today().year класса date из модуля datetime)
Создайте статический метод который проверяет является ли совершеннолетним человек возраст которого передается в метод.
"""
from datetime import date


class Person:
    name = 'Bogdan'
    age = 17
    
    def instancemethod(self):
        print(self.name, self.age)
    
    @classmethod
    def classmethod(cls, year):
        man = Person()
        man.name = 'Nikita'
        man.age = date.today().year - year
        return man
        
    @staticmethod
    def staticmethod(age):
        return age >= 18