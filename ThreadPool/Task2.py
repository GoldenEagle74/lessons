"""
Создайте функцию которая выводит на экран все делители числа.
Создайте очередь и добавьте в нее числа.
Создайте пул потоков и запустите в пуле функцию с очередью.
"""
import queue
import concurrent.futures

def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    number_queue = queue.Queue()
    numbers = [24, 36, 48, 60, 72, 84]

    for num in numbers:
        number_queue.put(num)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(find_divisors, list(number_queue.queue))

    for num, divisors in zip(numbers, results):
        print(f"Делители числа {num}: {divisors}")

if __name__ == "__main__":
    main()

