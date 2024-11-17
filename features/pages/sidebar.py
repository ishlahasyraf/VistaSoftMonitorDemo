from urllib import request
from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def waituntil(context,locator):
    wait = WebDriverWait(context.driver1, 20)
    return wait.until(EC.element_to_be_clickable(locator))

def dashboardbutton(context):
    dashboard_button = waituntil(context,(By.XPATH,"//a[@href='/dashboard']"))
    return dashboard_button

def inboxbutton(context):
    inbox_button = context.driver1.find_element(By.XPATH,"//a[@href='/inbox']")
    return inbox_button

def productsearchbutton(context):
    productsearch_button = waituntil(context,(By.XPATH,"//div[@id='nav-desktop']//span//a[@href='/search/']"))
    return productsearch_button

def saveddocumentsbutton(context):
    saveddocuments_button = context.driver1.find_element(By.XPATH,"//a[@href='/favorites']")
    return saveddocuments_button

def productregistrationbutton(context):
    productregistration_button = context.driver1.find_element(By.XPATH,"//a[@href='/warranty/things/']")
    return productregistration_button

def settingsbutton(context):
    settings_button = context.driver1.find_element(By.XPATH,"//a[@href='/settings']")
    return settings_button

def userbutton(context):
    user_button = waituntil(context,(By.XPATH,"//div[@id='nav-desktop']//div[@aria-label='nav-user-button']"))
    return user_button

def myuseraccountbutton(context):
    myuseraccount_button = waituntil(context,(By.XPATH,"//div[@id='user-profile']"))
    return myuseraccount_button

def languagebutton(context):
    language_button = context.driver1.find_element(By.XPATH,"//span[@title='Language']")
    return language_button

def helpbutton(context):
    help_button = context.driver1.find_element(By.XPATH,"//span[@title='Help']")
    return helpbutton

def legalnoticesbutton(context):
    legalnotices_button = context.driver1.find_element(By.XPATH,"//span[@title='Legal notices']")
    return legalnotices_button

def username(context):
    username_ = context.driver1.find_element(By.XPATH,"//div[@aria-label='nav-user-button']//p[1]")
    return username_