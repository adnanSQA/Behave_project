from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from loguru import logger
import sys

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

@given(u'the user is on the cbuk main page')
def step_impl(context):
    context.browser.get('https://www.carpetbright.uk.com/')


@when(u'the navbar is visible')
def step_impl(context):
    context.browser.find_element(By.ID, 'myheader').is_displayed()


@when(u'the Carpetbright logo should be present with the home page link')
def step_impl(context):
    context.browser.find_element(By.CLASS_NAME, 'main-logo').is_enabled()

@when('the phone number "{phone_number}" should be there on the page')
def step_impl(context, phone_number):
    phone_number_field = context.browser.find_element(By.CLASS_NAME, 'num_replace').text
    assert phone_number in phone_number_field
    logger.info(f'this is the phone number ==  {phone_number}')


@when(u'the "{opening_hours}" should be present on the page')
def step_impl(context, opening_hours):
    context.browser.find_element(By.CLASS_NAME, 'opening').is_displayed()
    logger.info(f"these are the opening hours {opening_hours}")


@then(u'it will close the browser')
def step_impl(context):
   pass