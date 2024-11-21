from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages import my_user_account_page,sidebar,product_search_page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

complete_SN_keyword = "2"
complete_ref_keyword = "7117-100-50"
complete_name_keyword ="V 6000 Suction System"
partial_SN_keyword = ""
partial_ref_keyword = "7117"
partial_name_keyword = "V 6000"



@given('I click on Product Search button')
def product_search_click(context):
    sidebar.productsearchbutton(context).click()


@when('I populate the search field with complete serial number')
def search_field_complete_SN(context):
    product_search_page.searchbar(context).click()
    product_search_page.searchbar(context).send_keys(complete_SN_keyword)

@when('I populate the search field with complete reference number')
def search_field_complete_SN(context):
    product_search_page.searchbar(context).click()
    product_search_page.searchbar(context).send_keys(complete_ref_keyword)

@when('I populate the search field with complete product name')
def search_field_complete_SN(context):
    product_search_page.searchbar(context).click()
    product_search_page.searchbar(context).send_keys(complete_name_keyword)

# @when('I populate the search field with partial serial number')
# def search_field_complete_SN(context):
#     product_search_page.searchbar(context).click()
#     product_search_page.searchbar(context).send_keys(partial_SN_keyword)

@when('I populate the search field with partial reference number')
def search_field_complete_SN(context):
    product_search_page.searchbar(context).click()
    product_search_page.searchbar(context).send_keys(partial_ref_keyword)

@when('I populate the search field with partial product name')
def search_field_complete_SN(context):
    product_search_page.searchbar(context).click()
    product_search_page.searchbar(context).send_keys(partial_name_keyword)

@when('I populate the search field with non-existent product')
def search_field_complete_SN(context):
    product_search_page.searchbar(context).click()
    product_search_page.searchbar(context).send_keys("sample")
    


@when('I proceed with the search')
def search_proceed(context):
    product_search_page.searchbar(context).click()
    action = ActionChains(context.driver1)
    action.send_keys(Keys.ENTER).perform()

@then('I am able to see relevant products in the search results')
def verify_first_last_name(context):
    keyword = product_search_page.getkeyword(context)
    assert product_search_page.searchresult(context,keyword).is_displayed,"not able to see relevant products in the search result"
    

@then('I am not able to see any search results')
def verify_no_search_results(context):
    keyword = product_search_page.getkeyword(context)
    try:
        product_search_page.searchresult(context,keyword)

    except TimeoutException as e:
        context.timeout_expected = True

    if hasattr(context,"timeout_expected") and context.timeout_expected:
        print("Timeout was expected. Marking test as passed")
    else:
        assert False,"Timeout did not occur as expected"

