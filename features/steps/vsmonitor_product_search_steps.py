from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages import my_user_account_page,sidebar,product_search_page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




@given('I click on Product Search button')
def product_search_click(context):
    sidebar.productsearchbutton(context).click()


@when('I populate the search field with complete serial number')
def search_field_complete_SN(context):
    complete_SN_keyword = "2"
    product_search_page.searchbar(context).click()
    product_search_page.searchbar(context).send_keys(complete_SN_keyword)
    


@when('I proceed with the search')
def search_proceed(context):
    product_search_page.searchbar(context).click()
    action = ActionChains(context.driver1)
    action.send_keys(Keys.ENTER).perform()

@then('I am able to see relevant products in the search results')
def verify_first_last_name(context):
    keyword = product_search_page.getkeyword(context)
    assert product_search_page.searchresult(context,keyword).is_displayed,"not able to see relevant products in the search result"
    

