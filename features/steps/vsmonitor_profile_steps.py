from behave import *
from selenium import webdriver
from vsmonitor_login_steps import login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages import login_page,my_user_account_page,sidebar
from dotenv import load_dotenv
import os

#load environment variables from env file 
load_dotenv() 
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


@when('I click on Profile button')
def profile_click(context):
    sidebar.userbutton(context).click()


@when('I click on My User Account')
def my_user_account_click(context):
    sidebar.myuseraccountbutton(context).click()


@then('My User Account page appears')
def verify_user_account_page_url(context):
    WebDriverWait(context.driver1, 20).until(EC.visibility_of_element_located((By.XPATH,"//h2//span[contains(text(),'My user account')]")))
    currentURL = context.driver1.current_url
    expectedURL = "https://vsmonitor.com/user/profile"
    assert currentURL == expectedURL , "URL is not matching. User not on the correct page after clicking on My User Account"


@then('First/Last name fields matches')
def verify_first_last_name(context):
    first_name = my_user_account_page.firstnamefield(context).text
    last_name = my_user_account_page.lastnamefield(context).text
    fullname = sidebar.username(context).text
    assert first_name in fullname, "first name do not match the actual name"
    assert last_name in fullname, "last name do not match the actual name"


@then('email field matches')
def verify_email(context):
    email_field = my_user_account_page.emailfield(context)
    user_email = email_field.get_attribute('value')
    print(email)
    print (user_email)
    assert user_email == email , "email in user account page do not match the actual user email" 