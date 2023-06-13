"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
import threading

class ReminderThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.reminder_event = threading.Event()
        self.reminder_lock = threading.Lock()

    def run(self):
        self.reminder_lock.acquire()
        reminder_text = input("О чем вам напомнить? ")
        delay = int(input("Через сколько секунд? "))
        self.reminder_lock.release()

        self.reminder_event.wait(delay)
        if self.reminder_event.is_set():
            return

        print("Напоминание:", reminder_text)

reminder_thread = ReminderThread()
reminder_thread.start()

reminder_thread.reminder_lock.acquire()
reminder_thread.reminder_lock.release()

reminder_thread.reminder_event.wait(10)
if not reminder_thread.reminder_event.is_set():
    reminder_thread.reminder_event.set()

print("Программа завершается")

