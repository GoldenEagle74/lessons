"""
Напишите программу которая автоматически собирает ваше расписание в Элжуре. и сохраняет в json файл в виде:
{день недели: {Предмет: Аудитория}
"""
import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service

# Установите путь к драйверу Firefox WebDriver
webdriver_service = Service('/usr/bin/geckodriver')

# Задайте параметры Firefox WebDriver
firefox_options = Options()
firefox_options.add_argument('-headless')  # Запустить Firefox в фоновом режиме

# Создайте экземпляр Firefox WebDriver
driver = webdriver.Firefox(service=webdriver_service)

# Переходим на страницу авторизации
driver.get('https://class.sirius.ru/authorize')

# Вводим логин и пароль
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]'))
)
password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')

username_input.send_keys('mshchannikov')
password_input.send_keys('6469918qwe')

# Нажимаем Enter
password_input.submit()

# Ожидаем загрузки страницы
schedule_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a.menu0-item[href="/journal-schedule-action/u.2437"]'))
)

# Переходим на страницу расписания
schedule_link.click()

# Ожидаем загрузки расписания
schedule_div = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'schedule'))
)

# Собираем расписание
schedule = {}

day_elements = schedule_div.find_elements(By.CLASS_NAME, 'schedule__day')

for day_element in day_elements:
    day_name_element = day_element.find_element(By.CLASS_NAME, 'schedule__day__content__header__dayweek')
    day_name = day_name_element.text.strip()

    lesson_elements = day_element.find_elements(By.CLASS_NAME, 'schedule__day__content__lesson--main')

    day_schedule = {}

    for lesson_element in lesson_elements:
        subject_element = lesson_element.find_element(By.CLASS_NAME, 'schedule-lesson')
        room_element = lesson_element.find_element(By.CLASS_NAME, 'schedule__day__content__lesson__room')

        subject = subject_element.text.strip()
        room = room_element.text.strip()

        day_schedule[subject] = room

    schedule[day_name] = day_schedule

# Закрываем браузер
driver.quit()

# Сохраняем расписание в JSON-файле
with open('schedule.json', 'w') as file:
    json.dump(schedule, file, ensure_ascii=False, indent=4)

print('Расписание успешно сохранено в файле "schedule.json".')


