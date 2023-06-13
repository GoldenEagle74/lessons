"""
Напишите программу которая автоматически зайдет на https://store.steampowered.com/ в поле поиска отправит стратегии
и соберет названия всех стратегий на 1 странице.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Установите путь к драйверу Firefox WebDriver
webdriver_service = Service('/usr/bin/geckodriver')

# Задайте параметры Firefox WebDriver
firefox_options = Options()
firefox_options.add_argument('-headless')  # Запустить Firefox в фоновом режиме

# Создайте экземпляр Firefox WebDriver
driver = webdriver.Firefox(service=webdriver_service)

# Откройте веб-страницу Steam
driver.get('https://store.steampowered.com/?l=russian')

# Найдите поле поиска и введите 'стратегии'
search_field = driver.find_element(By.ID, 'store_nav_search_term')
search_field.send_keys('стратегии')
search_field.send_keys(Keys.RETURN)

# Ожидание загрузки результатов поиска
driver.implicitly_wait(5)

# Найдите все элементы с названиями стратегий
strategy_titles = driver.find_elements(By.CSS_SELECTOR, '.search_name .title')

# Выведите названия стратегий
for title in strategy_titles:
    print(title.text)

# Закройте браузер
driver.quit()

