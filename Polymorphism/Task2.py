"""
Создать базовый класс ОЛИМПИАДНЫЕ ЗАДАНИЯ (данные об участнике, количество тестовых примеров,
количество пройденных тестов).
Создать производные классы ЗАДАНИЯ «ВСЕ ИЛИ НИЧЕГО»
(задается максимальное количество баллов за задание (даются только когда все тесты пройдены)
и ЗАДАНИЯ «ЧЕМ БЫСТРЕЕ, ТЕМ ЛУЧШЕ» (задается время участника на решение,
лучшее время всех участников, максимальное количество баллов за задание,
процент снижения балла в минуту отставания от лучшего времени).
Для заданных примеров задач, которые решали участники,
упорядочить участников по росту набранных баллов и определить суммарное количество баллов,
набранных заданным участником олимпиады.
Для проверки использовать действия над списком,
в котором разместить объекты разных производных классов.
"""
class ОЛИМПИАДНЫЕ_ЗАДАНИЯ:
    def __init__(self, data, count_all, count_pass):
        self.data = data
        self.count_all = count_all
        self.count_pass = count_pass

class ЗАДАНИЯ_ВСЕ_ИЛИ_НИЧЕГО(ОЛИМПИАДНЫЕ_ЗАДАНИЯ):
    def __init__(self, data, count_all, count_pass, max_points):
        super().__init__(data, count_all, count_pass)
        self.max_points = max_points
    def __str__(self): return self.max_points * self.count_pass if self.count_all == self.count_pass else 0


class ЗАДАНИЯ_ЧЕМ_БЫСТРЕЕ_ТЕМ_ЛУЧШЕ(ОЛИМПИАДНЫЕ_ЗАДАНИЯ):
    def __init__(self, data, count_all, count_pass, time, best_time, max_points, per):
        super().__init__(data, count_all, count_pass)
        self.time = time
        self.best_time = best_time
        self.max_points = max_points
        self.per = per
    def __str__(self): return self.max_points * self.count_pass * (((1-self.per/100)**self.time-self.best_time) if self.time > self.best_time else 1)
student1, student2 = ЗАДАНИЯ_ВСЕ_ИЛИ_НИЧЕГО('Иванов Иван Геннадиевич', 20, 15, 3), ЗАДАНИЯ_ЧЕМ_БЫСТРЕЕ_ТЕМ_ЛУЧШЕ('Петров Петр Васильевич', 20, 18, 60, 50, 3, 5)
res = sorted[student1.__str__, student2.__str__]
print(res)
