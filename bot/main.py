from fuzzywuzzy import fuzz
from database import *
per = fuzz.token_sort_ratio
d = {'Расписание':schedule,'Тренер':couch,'Плата':payment,'Звонок':call,'Где':location}
def main(req):
    for key in d:
        if per(key,req) >= 40: return d[key]()
while True: print(main(input('Введите ваш запрос: ')))

