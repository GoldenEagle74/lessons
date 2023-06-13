"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""
import os
import glob
import threading
import time

def replace_ids(file_path):
    with open(file_path, 'r+') as file:
        content = file.read()
        updated_content = content.replace('ids', 'id')
        file.seek(0)
        file.write(updated_content)
        file.truncate()

def process_file(file_path):
    replace_ids(file_path)
    print(f"Файл {file_path} обработан")

start_time = time.time()

files = glob.glob('Files/*.txt')  # Поиск файлов в папке files с расширением .txt

threads = []
for file_path in files:
    thread = threading.Thread(target=process_file, args=(file_path,))
    thread.start()
    threads.append(thread)

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения программы: {execution_time} секунд")

