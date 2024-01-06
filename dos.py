from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = 'http://localhost:1404/os.html'

# Опции для запуска Chrome в фоновом режиме
options = Options()
options.add_argument('--headless')

# Создание экземпляра WebDriver с опциями
driver = webdriver.Chrome(options=options)

# Открытие сайта 10 раз
for _ in range(20):
    driver.get(url)

# Циклическое обновление каждую секунду
for _ in range(10):
    time.sleep(1)
    driver.refresh()

# Закрытие браузера
driver.quit()
