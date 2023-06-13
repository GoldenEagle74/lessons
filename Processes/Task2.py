"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""
import multiprocessing

def calculate_room_area(width, length, height):
    area = 2 * (width * height + length * height)
    with open('room_data.txt', 'w') as file:
        file.write(f'Площадь комнаты из 4 стен: {area} кв.м\n')

def calculate_paint_consumption():
    with open('room_data.txt', 'a') as file:
        with open('room_data.txt', 'r') as read_file:
            lines = read_file.readlines()
            for line in lines:
                if 'Площадь комнаты из 4 стен' in line:
                    area = float(line.split(': ')[1].split(' ')[0])
                    paint_consumption = area * 5
                    file.write(f'Расход краски: {paint_consumption} л\n')

if __name__ == '__main__':
    width = 5
    length = 7
    height = 3

    process1 = multiprocessing.Process(target=calculate_room_area, args=(width, length, height))
    process2 = multiprocessing.Process(target=calculate_paint_consumption)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

