from tkinter import *
import tkinter
from email.quoprimime import body_check
from credential import credentials
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from twilio.rest import Client


def show_entry_fields():
    driver = webdriver.Chrome()
    driver.get('https://www.paygonline.com/')

    # parse in credentials
    driver.find_element(By.ID, 'login-phone-phone-number').send_keys(e1.get())
    driver.find_element(By.ID, 'login-pin-pin-number').send_keys(e2.get())
    driver.find_element(By.ID, 'login-form_0').click()
    # find data usage
    text = driver.find_element(By.XPATH, '//*[@id="usage-summary-css"]/div[3]/div/div[3]/div[2]/div[2]/div[2]/p/strong')
    toSend = text.text
    print("Remaining Data: %s" % (toSend))

top = Tk()
L1 = Label(top, text = "User Name").grid(row=0)
L2 = Label(top, text = "Password").grid(row=1)

e1 = Entry(top)
e2 = Entry(top)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(top,text='Quit', command=top.quit).grid(row=3,column=0, sticky=tkinter.W, pady=4)
Button(top,text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=tkinter.W, pady=4)
top.mainloop()