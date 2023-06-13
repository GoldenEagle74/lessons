"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""
import requests

def save_random_cat_images():
    for i in range(2):
        response = requests.get('https://cataas.com/cat')
        with open(f'random_cat_{i+1}.jpg', 'wb') as file:
            file.write(response.content)

def save_original_images():
    for i in range(2):
        response = requests.get('https://cataas.com/cat?filter=original')
        with open(f'original_cat_{i+1}.jpg', 'wb') as file:
            file.write(response.content)

def save_pixelated_images():
    for i in range(2):
        response = requests.get('https://cataas.com/cat?filter=pixel')
        with open(f'pixel_cat_{i+1}.jpg', 'wb') as file:
            file.write(response.content)

# Вызов функций сохранения изображений
save_random_cat_images()
save_original_images()
save_pixelated_images()

