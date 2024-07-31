from Helpers import project_helpers
import time
from behave import given, when, then
from locators import locators
from sample_data import sample_data

@given(u'the user is on the cbuk main page')
def step_impl(context):
    context.browser.get('https://www.carpetbright.uk.com')


@when(u'the navbar is visible')
def step_impl(context):
    context.browser.find_element(*locators.navbar).is_displayed()


@when(u'the Carpetbright logo should be present with the home page link')
def step_impl(context):
    navbar_log = context.browser.find_element(*locators.navbar_logo)
    navbar_log.is_displayed()
    navbar_log.is_enabled()


@when('the phone number "{phone_number}" should be there on the page')
def step_impl(context, phone_number):
    phone_number_element = context.browser.find_element(*locators.navbar_phone_number).text
    assert phone_number in phone_number_element, f"Expected phone number '{phone_number}' not found in '{phone_number_element}'"




@when('the opening hours "{opening_hours}" should be present on the page')
def step_impl(context, opening_hours):
    open_hours = context.browser.find_element(*locators.navbar_opening_hours).text
    assert opening_hours in open_hours, f"Expected opening hours '{opening_hours}' not found in '{open_hours}'"



@then(u'The banner text should be there')
def step_impl(context):
    banner_text = context.browser.find_element(*locators.main_page_banner_text)
    assert sample_data.main_page_banner_text == banner_text.text



@then(u'The bullet points should be exact')
def step_impl(context):
    bullet_points = context.browser.find_element(*locators.main_page_bullet_points)
    all_bullet_points = [item.text for item in bullet_points.find_elements(*locators.li_tag)]
    assert sample_data.main_page_bullet_points == all_bullet_points



@then(u'Verify the banner button background color')
def step_impl(context):
    bannet_quote_btn = context.browser.find_element(*locators.banner_quote_button)
    bannet_quote_btn.is_displayed()
    current_color = bannet_quote_btn.value_of_css_property('background-color')
    # assert "#82c12d" in project_helpers(current_color), f"Expected opening hours '{project_helpers(current_color)}' "
    pass



@when(u'the reviews text is visible it should have reviews on the page')
def step_impl(context):
    banner_reviews_blow = context.browser.find_element(*locators.banner_review_below)
    time.sleep(10)
    assert sample_data.banner_reviews_text == banner_reviews_blow.text, f"Actual text is'{banner_reviews_blow.text}' Expected text was '{sample_data.banner_reviews_text}'"




@when(u'There shuold be an input field for putting the postcode')
def step_impl(context):
    input_field = context.browser.find_element(*locators.banner_inputfield)
    input_field.is_displayed()


@when(u'the input field will accept the zipcode')
def step_impl(context):
    input_field = context.browser.find_element(*locators.banner_inputfield)
    input_field.send_keys(sample_data.post_code)


@when(u'there should be a get a quote button')
def step_impl(context):
    quote_btn = context.browser.find_element(*locators.banner_quote_button)
    context.action.click(quote_btn).perform()
    context.browser.switch_to.window(context.browser.window_handles[-1])

@when(u'on pressing the button it will redirect to this page https://www.carpetbright.uk.com/free-quote/?PostCode=')
def step_impl(context):
    time.sleep(4)
    assert "https://www.carpetbright.uk.com/free-quote/?PostCode=" in context.browser.current_url, f"the url of the page is {context.browser.current_url}"