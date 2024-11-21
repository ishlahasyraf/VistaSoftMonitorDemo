from urllib import request
from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def waituntil(context,locator):
    wait = WebDriverWait(context.driver1, 10)
    return wait.until(EC.visibility_of_element_located(locator))

def searchbar(context):
    search_bar = waituntil(context,(By.XPATH,"//input[@id='search']"))
    return search_bar

def searchresult(context,keyword):
    searchresult = waituntil(context,(By.XPATH,"(//nav[@aria-label='menu.nav_search']//span[contains(text(),'"+keyword+"')]) | (//nav[@aria-label='menu.nav_search']//p[contains(text(),'"+keyword+"')])"))
    return searchresult

def getkeyword(context):
    current_url = context.driver1.current_url
    keyword = current_url.split("q=")[1]
    updatedkeyword = keyword.replace("%20", " ")
    print(updatedkeyword)
    return updatedkeyword
    