"""
Класс Vector3D
Экземляр класса задается тройкой координат в трехмерном пространстве (x,y,z).
Обязательно должны быть реализованы методы:
– приведение вектора к строке с выводом кооржинат (метод __str __),
– сложение векторов оператором `+` (метод __add__),
– вычитание векторов оператором `-` (метод __sub__),
– скалярное произведение оператором `*` (метод __mul__),
"""
from math import sqrt, cos


class Vector3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return self.x,self.y,self.z
    
    def __add__(self, otherVector3D):
        return (self.x + otherVector3D.x, self.y + otherVector3D.y, self.z + otherVector3D.z)
    
    def __sub__(self, otherVector3D):
        return (self.x - otherVector3D.x, self.y - otherVector3D.y, self.z - otherVector3D.z)
    
    def __mul__(self, otherVector3D, angle):
        return(sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2) * sqrt(otherVector3D.x ** 2 + otherVector3D.y ** 2 + otherVector3D.z ** 2) * cos(angle))