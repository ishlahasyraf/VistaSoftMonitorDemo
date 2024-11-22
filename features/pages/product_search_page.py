from urllib import request
from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException


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

def clickproduct(context,searchresult):
    searchresult.click()
    
def search_result_product_name(context,keyword):
    search_result_product_name = waituntil(context,(By.XPATH,"(//nav[@aria-label='menu.nav_search']//span[contains(text(),'"+keyword+"')]) | (//nav[@aria-label='menu.nav_search']//p[contains(text(),'"+keyword+"')])")).text
    return search_result_product_name

def search_result_product_SN(context):
    try:
        search_result_product_SN = waituntil(context,(By.XPATH,"(//nav[@aria-label='menu.nav_search']//span[contains(text(),'Serial number:')]) | (//nav[@aria-label='menu.nav_search']//p[contains(text(),'Serial number:')])")).text
    except TimeoutException as e:
        search_result_product_SN = None
    return search_result_product_SN

def search_result_product_ref(context):
    try:
        search_result_product_ref1 = context.driver1.find_element(By.XPATH,"(//nav[@aria-label='menu.nav_search']//span[contains(text(),'REF:')]) |(//nav[@aria-label='menu.nav_search']//p[contains(text(),'REF:')])").text
        search_result_product_ref2 = context.driver1.find_element(By.XPATH,"//span[@class='text-gray-500' and normalize-space(text())]").text

        search_result_product_ref = search_result_product_ref1+" "+search_result_product_ref2
    except TimeoutException as e:
        search_result_product_ref = None
    return search_result_product_ref


def product_detail_page_name(context):
    detail_page_name = waituntil(context,(By.XPATH,"//div[@class='_tid_search-detail-page h-full flex']//span[@class='mx-2']")).text
    return detail_page_name

def product_detail_page_SN(context):
    try:
        detail_page_SN = waituntil(context,(By.XPATH,"//div[@class='_tid_search-detail-page h-full flex']//div[@id='things-header-details']//span[contains(text(),'SN')]")).text
    except TimeoutException as e:
        detail_page_SN = None
    return detail_page_SN

def product_detail_page_ref(context):
    try:
        detail_page_ref = waituntil(context,(By.XPATH,"//div[@class='_tid_search-detail-page h-full flex']//div[@id='things-header-details']//span[contains(text(),'REF:')]")).text
    except TimeoutException as e:
        detail_page_ref = None
    return detail_page_ref