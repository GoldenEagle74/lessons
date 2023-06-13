"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
import threading

def warning_message():
    while True:
        with print_lock:
            print("Вводите быстрее")
        time.sleep(3)

print_lock = threading.Lock()
warning_thread = threading.Thread(target=warning_message)
warning_thread.daemon = True
warning_thread.start()

bomb_code = input("Введите код от бомбы: ")

if bomb_code == "12345":
    print("Бомба разминирована")
else:
    print("Вы взорвались")

