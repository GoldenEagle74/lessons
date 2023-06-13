"""
Напишите скрипт который принимает 2 аргумента - путь и имя папки. И создаем папку по указанному пути.
"""
import sys
import os

# Проверка количества аргументов
if len(sys.argv) == 3:
    path, folder_name = sys.argv[1], sys.argv[2]

    try:
        # Создание папки
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Папка '{folder_name}' успешно создана в пути '{path}'.")
    except OSError:
        print(f"Ошибка: не удалось создать папку '{folder_name}' в пути '{path}'.")
else:
    print("Некорректное количество аргументов. Пожалуйста, укажите путь и имя папки.")

