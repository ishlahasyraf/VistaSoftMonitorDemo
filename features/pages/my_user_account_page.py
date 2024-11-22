from urllib import request
from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def waituntil(context,locator):
    wait = WebDriverWait(context.driver1, 30)
    return wait.until(EC.visibility_of_element_located(locator))

def firstnamefield(context):
    firstname_field = waituntil(context,(By.XPATH,"//input[@id='firstName']"))
    return firstname_field

def lastnamefield(context):
    lastname_field = context.driver1.find_element(By.XPATH,"//input[@id='lastName']")
    return lastname_field

def emailfield(context):
    email_field = context.driver1.find_element(By.XPATH,"//input[@id='email']")
    return email_field
    