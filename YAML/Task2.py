"""
Из файла info.yaml выведите имя и id Ливерпуля
"""
import yaml


with open('info.yaml') as f:
    r = yaml.safe_load(f)
    print(*[r[0][i] for i in ['name','id']])