'''
Loads local file example.txt from current dir to http://suninjuly.github.io/file_input.html
'''

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://suninjuly.github.io/file_input.html"
CUR_DIR = os.path.abspath(os.path.dirname(__file__))
FILE_PATH = os.path.join(CUR_DIR, "example.txt")

with webdriver.Chrome() as browser:
    browser.get(URL)
    
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("my@mail")
    
    to_send = browser.find_element(By.ID, "file")
    to_send.send_keys(FILE_PATH)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    time.sleep(4)
