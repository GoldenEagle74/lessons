"""
Напишите функцию которая через канал обмена возвращает количество валюты которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""
import multiprocessing
import time

def calculate_currency_amount(connection, money):
    currency_amount = money / 75
    connection.send([money,currency_amount])

if __name__ == '__main__':
    money_list = [100, 200, 300, 400, 500]
    processes = []

    for money in money_list:
        parent_conn, child_conn = multiprocessing.Pipe()
        process = multiprocessing.Process(target=calculate_currency_amount, args=(child_conn, money))
        processes.append((process, parent_conn))
        process.start()

    for process, parent_conn in processes:
        process.join()

    for process, parent_conn in processes:
        time.sleep(0.5)
        if parent_conn.poll():
            money, currency_amount = parent_conn.recv()
            print(f"При {money} суммах денег можно приобрести {currency_amount} валюты")

