"""
Из файла Task1.csv выведите данные в формате:
Имя - Звание
"""
import csv


with open('Task1.csv', 'r') as f:
    reader = list(csv.reader(f, delimiter=';'))
    [print('{} - {}'.format(*[x for x in row if row.index(x) in [reader[0].index(header) for header in ['Имя','Звание']]])) for row in reader[1:]]