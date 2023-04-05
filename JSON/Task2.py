"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: ***
"""
task = ["oleg",24,["Belarus","Russia"]]
import json


with open('Щанников 2', 'w+') as file: json.dump({['name','age','countries'][i]:task[i] for i in range(len(task))}, file, indent=4)
