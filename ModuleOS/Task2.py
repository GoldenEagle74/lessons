"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""
import os


os.system('for i in $(seq 1 10); do mkdir target/$i -p; done')
