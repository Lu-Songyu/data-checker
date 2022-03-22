import smtpd
import smtplib
from credential import credentials
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import sys


driver = webdriver.Chrome()
driver.get('https://www.paygonline.com/')

# parse in credentials
driver.find_element(By.ID, 'login-phone-phone-number').send_keys(credentials.get('att_userID'))
driver.find_element(By.ID, 'login-pin-pin-number').send_keys(credentials.get('att_password'))
driver.find_element(By.ID, 'login-form_0').click()
# find data usage
text = driver.find_element(By.XPATH, '//*[@id="usage-summary-css"]/div[3]/div/div[3]/div[2]/div[2]/div[2]/p/strong')
toSend = text.text
# login gmail
driver.get('https://www.gmail.com/')
river.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('songyulu99@gmail.com')
driver.find_element(By.XPATH, 'login-pin-pin-number').send_keys('LsyATT990914')
