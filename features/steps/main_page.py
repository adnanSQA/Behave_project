from behave import given, when, then
from sample_data import sample_data
from selenium.webdriver.common.by import By
from locators import locators
from selenium.webdriver.common.action_chains import ActionChains
from loguru import logger
import time
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


@then(u'The banner text should be there')
def step_impl(context):
    banner_text = context.browser.find_element(*locators.main_page_banner_text).text 
    assert sample_data.main_page_banner_text == banner_text


@then(u'The bullet points should be exact')
def step_impl(context):
    bullets_area = context.browser.find_element(*locators.main_page_bullet_points)
    bullet_points = [item.text for item in bullets_area.find_elements(*locators.li_tag)]
    assert sample_data.main_page_bullet_points == bullet_points

@then(u'Verify the banner button background color')
def step_impl(context):
    banner_button = context.browser.find_element(*locators.banner_quote_button)
    logger.info(f"Banner button color is {banner_button.value_of_css_property('background-color')}")
    actions = ActionChains(context.browser)
    actions.move_to_element(banner_button).perform()
    time.sleep(3)
    logger.info(f"Banner button color after hover is {banner_button.value_of_css_property('background-color')}")
