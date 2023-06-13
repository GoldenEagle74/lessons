"""
Запустите фоновый процесс который следит за сроком подписки пользователя( для примера 10 секунд) если время подписки вышло выведите надпись "Ваша подписка закончилась."
и завершите работу программы. В основной программе сыграйте с пользователем в игру "угадай число".
"""
import multiprocessing
import time
import random

def subscription_checker(stop_event):
    subscription_duration = 10
    time.sleep(subscription_duration)
    print("Ваша подписка закончилась.")
    stop_event.set()

def guess_number_game(stop_event):
    number = random.randint(1, 100)
    while not stop_event.is_set():
        guess = int(input("Введите число: "))
        if guess == number:
            print("Поздравляю, вы угадали число!")
            stop_event.set()
        elif guess < number:
            print("Число больше.")
        else:
            print("Число меньше.")

if __name__ == '__main__':
    stop_event = multiprocessing.Event()

    subscription_process = multiprocessing.Process(target=subscription_checker, args=(stop_event,))
    subscription_process.start()

    guess_number_game(stop_event)

    subscription_process.join()
    subscription_process.terminate()

