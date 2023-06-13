"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""
import multiprocessing

def sum_even_numbers():
    result = sum(range(2, 1000001, 2))
    print("Сумма четных чисел:", result)

def sum_odd_numbers():
    result = sum(range(1, 1000001, 2))
    print("Сумма нечетных чисел:", result)

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=sum_even_numbers)
    process2 = multiprocessing.Process(target=sum_odd_numbers)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

