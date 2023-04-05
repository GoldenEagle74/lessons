"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: [
{
name:***
time:***
cities:***
}
]
"""
task = ["oleg",24,["Belarus","Russia"],(24,1),["Moscow","Vladikavkaz",'Krasnodar',"Rostov","Nalchik"]]
import json


keys = ['name', 'age', 'countries', ['name','time','cities']]
with open('Щанников 3', 'w+') as file: json.dump({keys[:2][i]:task[i] for i in range(2)} | {keys[2]: [{keys[3][:2][i]:task[i+2][0] for i in range(2)} | {keys[3][2]:[]}, {keys[3][i]:task[i+2][0] for i in range(3)}]}, file, indent=4)