# environment.py

from selenium import webdriver
from features.pages import login_page
from features.pages import sidebar
from dotenv import load_dotenv
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



load_dotenv() 
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# executes common steps (open browser, login)
def before_scenario(context, scenario):
    # Check if the scenario has the "skip_before" tag
    if "skip_before" in scenario.tags:
        return  # Skip the rest of the hook logic for this scenario
    
    #open browser and define the driver
    context.driver1 = webdriver.Chrome()
    context.driver1.maximize_window()
    # perform user login
    login_page.getloginpage(context)
    login_page.loginbutton_welcome(context).click()
    email_field = login_page.emailfield(context)
    email_field.click()
    email_field.send_keys(email)
    password_field = login_page.passwordfield(context)
    password_field.click()
    password_field.send_keys(password)
    login_page.loginbutton_auth(context).click()
    WebDriverWait(context.driver1, 20).until(EC.visibility_of_element_located((By.XPATH,"//h2[contains(text(),'Dashboard')]")))

