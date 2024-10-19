from urllib import request
from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
from pages import login_page
from pages import sidebar


#load environment variables from env file 
load_dotenv() 
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")



@given('I launched chrome browser')
def launchBrowser(context):
    #define the driver
    context.driver1 = webdriver.Chrome()
    context.driver1.maximize_window()
    

@when('open VistaSoft Monitor webpage')
def clickLoginWelcome(context):
    login_page.getloginpage(context)
    login_page.loginbutton_welcome(context).click()

    

@when('input Email in Email field')
def enterEmail(context):
    email_field = login_page.emailfield(context)
    email_field.click()
    email_field.send_keys(email)
    
    

@when('input Password in Password field')
def enterPassword(context):
    password_field = login_page.passwordfield(context)
    password_field.click()
    password_field.send_keys(password)


@when('Click on Log-in button')
def clickLoginAuth(context):
    login_page.loginbutton_auth(context).click()


@then('I am able to login successfully')
def verifyURL_login(context):
    WebDriverWait(context.driver1, 20).until(EC.visibility_of_element_located((By.XPATH,"//h2[contains(text(),'Dashboard')]")))
    current_url = context.driver1.current_url
    expected_url = 'https://vsmonitor.com/dashboard'
    assert current_url == expected_url,"URL is not matching. User not on the correct page after login"
    print("assertion 1 : User is able to login successfully!")
    
@given('I successfully logged in VistaSoft Monitor')
def login(context):
    launchBrowser(context)
    clickLoginWelcome(context)
    enterEmail(context)
    enterPassword(context)
    clickLoginAuth(context)
    verifyURL_login(context)