"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""
class SpaceObject:
    def __init__(self, size):
        self.size = size

class Star(SpaceObject):
    def __init__(self, size, brightness):
        super().__init__(size)
        self.brightness = brightness
    def light(self): print(self.brightness)

class Planet(SpaceObject):
    def __init__(self, size, population, increase):
        super().__init__(size)
        self.start_population = population
        self.increase = increase
    def population(self, years): print(self.start_population + years * self.increase)
    