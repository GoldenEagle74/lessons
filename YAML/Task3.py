"""
Сохраните информацию из character.json в yaml файл(Имя файла - ваша фамилия)
"""
import json, yaml


with open('character.json') as f, open('Щанников.yaml', 'w+') as g: yaml.dump(json.loads(f.read()),g)