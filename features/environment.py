# environment.py

from selenium import webdriver
from features.pages import login_page
from features.pages import sidebar
from dotenv import load_dotenv
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

load_dotenv() 
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU (useful for headless mode)
chrome_options.add_argument("--no-sandbox")  # Required in some CI environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
# executes common steps (open browser, login)
def before_scenario(context, scenario):
    # Check if the scenario has the "skip_before" tag
    if "skip_before" in scenario.tags:
        return  # Skip the rest of the hook logic for this scenario
    
    #open browser and define the driver

    context.driver1 = webdriver.Chrome(options=chrome_options)
    context.driver1.maximize_window()
    