"""
Создайте программу выводящую информацию о системе вида:
Операционная система - ХХХ
Имя компьютера - ХХХ
Имя пользователя - ХХХ
"""
import os


print('''Операционная система - {}
Имя компьютера - {}
Имя пользователя - {}'''.format(*os.uname()[:2],os.getlogin()))
