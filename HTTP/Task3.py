"""
Изучите API сервиса https://rickandmortyapi.com/
Получите имя, родную планету и список эпизодов  всех персонажах начиная с вашего номера в журнале и заканчивая ваш номер*5
Сохраните в .json файл.
"""
import requests
import json

start_id = 19
end_id = start_id * 5

characters = []

for character_id in range(start_id, end_id + 1):
    response = requests.get(f'https://rickandmortyapi.com/api/character/{character_id}')
    if response.status_code == 200:
        data = response.json()
        character_data = {
            "name": data["name"],
            "planet": data["origin"]["name"],
            "episodes": data["episode"]
        }
        characters.append(character_data)

with open('characters.json', 'w') as file:
    json.dump(characters, file, indent=4)

