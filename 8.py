from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    def calc(x, y):
        return str(int(x) + int(y)) 
    
    
    num1_element = browser.find_element(By.ID, "num1")
    num1 = num1_element.text
    num2_element = browser.find_element(By.ID, "num2")
    num2 = num2_element.text
    y = calc(num1, num2)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла