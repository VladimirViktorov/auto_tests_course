import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

links = "http://selenium1py.pythonanywhere.com/"
answer = ""

@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1', 
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    input = WebDriverWait(browser, 12).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.textarea'))
        )
    input.send_keys(str(math.log(int(time.time()))))
    button = WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
    button.click()
    text_element = WebDriverWait(browser, 12).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )
    text = text_element.text
    
    assert text == "Correct!", text
    