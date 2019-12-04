from selenium import *
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import request
import time
import pyperclip

user_name="b.onas.41.50@gmail.com"
password="Zayanto@2018"


driver=webdriver.Chrome()
z=driver.get("https://www.presearch.org/login")
print(z)

user=driver.find_element_by_name('email')
pass_word=driver.find_element_by_name('password')

user.send_keys(user_name)
pass_word.send_keys(password)

login = driver.find_element_by_xpath('//*[@id="login-form"]/form/div[3]/div[2]/button')
login.click()
time.sleep(5)

#balance = driver.find_element_by_class_name('tour-balance')
#balance.click()
zz=driver.get("https://www.presearch.org/account/2fa/confirm")
code=driver.find_element_by_tag_name('code')

pyperclip.copy(code.text)
paste=pyperclip.paste()
print(paste)
otp=driver.find_element_by_name('totp')
confirm=driver.find_element_by_xpath('//*[@id="main"]/form/button')   