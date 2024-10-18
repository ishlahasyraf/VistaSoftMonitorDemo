from urllib import request
from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def waituntil(context,locator):
    wait = WebDriverWait(context.driver1, 20)
    return wait.until(EC.visibility_of_element_located(locator))
    

def getloginpage(context):
    context.driver1.get("https://vsmonitor.com/")
    WebDriverWait(context.driver1, 20).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Login')]")))
    
def loginbutton_welcome(context):
    login_button = context.driver1.find_element(By.XPATH,"//span[contains(text(),'Login')]")
    return login_button

def emailfield(context):
    email_field = waituntil(context,(By.XPATH,"//input[@name='username']"))
    return email_field

def passwordfield(context):
    password_field = waituntil(context,(By.XPATH,"//input[@name='password']"))
    return password_field

def loginbutton_auth(context):
    login_auth = context.driver1.find_element(By.XPATH,"//button[@name='login']")
    return login_auth