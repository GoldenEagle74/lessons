"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.
"""
import sys

# Проверка количества аргументов
if len(sys.argv) == 3:
    content, filename = sys.argv[1], sys.argv[2]

    try:
        # Запись содержимого в файл
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Запись в файл '{filename}' успешно выполнена.")
    except IOError as e:
        print(f"Ошибка: не удалось записать в файл '{filename}'.")
else:
    print("Некорректное количество аргументов. Пожалуйста, укажите содержимое и имя файла.")

