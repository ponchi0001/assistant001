#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/pi/.local/lib/python3.5/site-packages/')
from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
browser.get('https://www.google.com/')

time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)
driver.quit()
