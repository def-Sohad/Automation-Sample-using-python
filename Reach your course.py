from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import keyboard # pip install keyboard
from creds import *

driver = webdriver.Chrome(executable_path=r"C:\Users\Sohad\Desktop\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://learn.humber.ca/")
time.sleep(1)


#Find the username box and put my username and click next
username = driver.find_element(By.ID,"i0116")
username.send_keys("your-N-number@humber.ca")
element = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.ID,"idSIButton9")))
time.sleep(1)
element.click()
#Find the Password box and put my password and click sign in
password = driver.find_element(By.ID,"i0118")
password.send_keys("Password")
time.sleep(1)
element = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.ID,"idSIButton9")))
time.sleep(1)
element.click()
element = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.ID,"idSIButton9")))
time.sleep(1)
element.click()
time.sleep(1)
element = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.LINK_TEXT,"Courses")))
time.sleep(1)
element.click()
time.sleep(1)
element = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.LINK_TEXT,"Name of the Course")))
time.sleep(1)
element.click()







