"""
Функций sorted принимает в качестве дополнительного параметра key(Можете почитать документацию).
С помощью lambda-функции отсортируйте этот список словарей по именам
"""
grades = [{'name': 'Jennifer', 'final': 95},
     {'name': 'David', 'final': 92},
    {'name': 'Aaron', 'final': 98}]
grades = sorted(grades, key = lambda x: list(x.values())[0])

