"""
Выведите из файла character.json Имя персонажа,родную планету и список эпизодов в которых он появлялся.
"""
import json


with open("character.json", "r") as json_file:
    data = json.loads(json_file.read())

for key in ['name', ['origin', 'name'], 'episode']:
    if isinstance(key, list):
        dict = data
        for k in key: dict = dict[k]
        print(dict)
    elif len(data[key][0]) > 1: print(*data[key], sep='\n')
    else: print(data[key])

