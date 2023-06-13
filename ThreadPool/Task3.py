"""
Создайте функцию которая из файла Names.txt берет имена, превращает его в путь до файла и помещает в очередь.
Создайте функцию которая создает txt файл  по пути из очереди.
Запустите все в разных потоках.
"""
import queue
import threading
import concurrent.futures
import os

def process_names(names_queue, output_directory):
    while True:
        try:
            name = names_queue.get(block=False)
            file_path = os.path.join(output_directory, name + ".txt")
            create_file(file_path)
        except queue.Empty:
            break

def create_file(file_path):
    with open(file_path, "w") as file:
        file.write("This is a sample file.")

def main():
    names_queue = queue.Queue()
    output_directory = "output"
    os.makedirs(output_directory, exist_ok=True)

    with open("Names.txt", "r") as file:
        names = file.read().splitlines()

    for name in names:
        names_queue.put(name)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(process_names, names_queue, output_directory)

if __name__ == "__main__":
    main()

