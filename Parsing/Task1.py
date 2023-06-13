"""
Соберите данные с чартов яндекс музыки https://music.yandex.ru/chart
Внимательно изучите источник, посмотрите как именно на сайт приходит информация.
Сохраните данные в json файл в формате:
{
место в чарте: (исполнитель,трек)
}
"""
import requests
from bs4 import BeautifulSoup
import json

# Загрузка веб-страницы
url = 'https://music.yandex.ru/chart'
response = requests.get(url)
html_content = response.content

# Создание объекта BeautifulSoup с использованием lxml парсера
soup = BeautifulSoup(html_content, 'lxml')

# Нахождение элементов с информацией о треках
track_elements = soup.find_all('div', 'lightlist__cont')


for track in track_elements:
    titles = list(map(lambda x: x.text.strip(), track.find_all('a', 'd-track__title')))
    artists = list(map(lambda x: x.text.strip(), track.find_all('span', 'd-track__artists')))

chart_data = {index:(title,artist) for index, (title, artist) in enumerate(zip(titles,artists))}

with open('chart_data.json', 'w', encoding='utf-8') as file:
    json.dump(chart_data, file, ensure_ascii=False, indent=4)

print("Данные успешно сохранены в файл chart_data.json")

