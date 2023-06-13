"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""
import queue
import threading
import time

def add_student(queue, stop_event):
    while not stop_event.is_set():
        surname = input("Введите фамилию студента (или 'off' для завершения): ")
        if surname.lower() == "off":
            stop_event.set()
        else:
            queue.put(surname)

def remove_student(queue, stop_event):
    while not stop_event.is_set() or not queue.empty():
        if not queue.empty():
            surname = queue.get()
            print(f"Студент {surname} отчислен.")
        time.sleep(1)

def main():
    student_queue = queue.Queue()
    stop_event = threading.Event()

    # Создание пула потоков с двумя рабочими потоками
    thread_pool = []
    for _ in range(2):
        thread = threading.Thread(target=remove_student, args=(student_queue, stop_event))
        thread_pool.append(thread)
        thread.start()

    add_student(student_queue, stop_event)

    # Ожидание завершения всех потоков в пуле
    for thread in thread_pool:
        thread.join()

if __name__ == "__main__":
    main()

