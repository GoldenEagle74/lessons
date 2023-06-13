"""
Напишите скрипт который в качестве параметра из командной строки принимает имя файла. Читает команды в этом файле и выполняет их
Протестируйте скрипт на файле comands.txt
"""
import sys
import subprocess

# Проверка количества аргументов
if len(sys.argv) == 2:
    filename = sys.argv[1]

    try:
        # Чтение команд из файла и выполнение
        with open(filename, 'r') as file:
            commands = file.readlines()

        for command in map(str.strip, commands):
            subprocess.run(command, shell=True)

        print("Команды выполнены успешно.")
    except IOError:
        print(f"Ошибка: не удалось прочитать файл '{filename}'.")
else:
    print("Некорректное количество аргументов. Пожалуйста, укажите имя файла с командами.")

