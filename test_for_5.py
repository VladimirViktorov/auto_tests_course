import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestDriwer(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        text = "text"
        block = browser.find_element(By.CLASS_NAME, "first_block")
        input1 = block.find_element(By.CLASS_NAME, "form-control.first") # Список текстовых полей
        input1.send_keys(text)
        input2 = block.find_element(By.CLASS_NAME, "form-control.second") # Список текстовых полей
        input2.send_keys(text)
        input3 = block.find_element(By.CLASS_NAME, "form-control.third") # Список текстовых полей
        input3.send_keys(text)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be absolute value of a number")
        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        text = "text"
        block = browser.find_element(By.CLASS_NAME, "first_block")
        input1 = block.find_element(By.CLASS_NAME, "form-control.first") # Список текстовых полей
        input1.send_keys(text)
        input2 = block.find_element(By.CLASS_NAME, "form-control.second") # Список текстовых полей
        input2.send_keys(text)
        input3 = block.find_element(By.CLASS_NAME, "form-control.third") # Список текстовых полей
        input3.send_keys(text)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()
