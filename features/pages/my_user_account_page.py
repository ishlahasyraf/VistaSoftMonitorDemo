from urllib import request
from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def waituntil(context,locator):
    wait = WebDriverWait(context.driver1, 20)
    return wait.until(EC.visibility_of_element_located(locator))
    