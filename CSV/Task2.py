"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""
import csv


with open('Task1.csv', 'r') as f: print({tuple(row[:2]):{row[2]:row[3]} for row in list(csv.reader(f, delimiter=';'))[1:]})
