from behave import given, when, then
from sample_data import CC_london_data
from locators import CC_locators
from loguru import logger




@when(u'the user redirects to the page')
def step_impl(context):
    context.browser.get('https://www.carpetbright.uk.com/carpet-cleaning/abbey-wood/')


@then('the browser title should be Carpet Cleaning Abbey Wood, SE2 | 20 000+ Reviews')
def step_then_browser_title_should_be(context):
    actual_title = context.browser.title
    context.location_name = context.browser.find_element(*CC_locators.location_name).text
    logger.info(context.location_name)
    assert "Carpet Cleaning Abbey Wood, SE2 | 20 000+ Reviews" in actual_title
    pass

@then('the banner section heading should be Carpet Cleaning Abbey Wood')
def step_then_banner_section_heading_should_be(context):
    banner_heading_text = context.browser.find_element(*CC_locators.banner_main_heading).text
    assert CC_london_data.banner_heading_text == banner_heading_text, f"The text are not same"

@then('the banner input field should be present')
def step_then_banner_input_field_should_be_present(context):
    banner_input_field = context.browser.find_element(*CC_locators.banner_input_field)
    banner_input_field.is_displayed()

@then('there should be a button that takes the user to a new page on click')
def step_then_button_should_take_user_to_new_page(context):
    banner_get_a_quote_button = context.browser.find_element(*CC_locators.banner_get_a_quote_button)
    banner_get_a_quote_button.is_enabled()

@then('a banner reviews image should be present')
def step_then_banner_reviews_image_should_be_present(context):
    banner_google_reviews_image = context.browser.find_element(*CC_locators.banner_reviews_image)
    banner_google_reviews_image.is_displayed()

@then('the content heading should be CARPET CLEANING ABBEY WOOD')
def step_then_content_heading_should_be(context):
    main_content_heading = context.browser.find_element(*CC_locators.content_main_heading).text
    assert CC_london_data.content_heading_text in main_content_heading

@then('a content image should be present on the page')
def step_then_content_image_should_be_present(context):
    context.main_content_image = context.browser.find_element(*CC_locators.content_image)
    context.main_content_image.is_displayed()

@then('the content image should have an alt attribute with the value Carpet Cleaning Abbey Wood SE2')
def step_then_content_image_should_have_alt_attribute(context):
    context.main_content_image.get_attribute('alt')

@then('there should be a We Guarantee section')
def step_then_we_guarantee_section_should_be_present(context):
    context.we_gauretee_section = context.browser.find_element(*CC_locators.view_gaurantee_section_main_box)
    context.we_gauretee_section.is_displayed()

@then('it should display 5 boxes on the page')
def step_then_it_should_display_5_boxes_on_the_page(context):
    number_of_boxes = context.browser.find_elements(*CC_locators.view_gaurantee_section_boxes)
    total_boxes = len(number_of_boxes)
    assert 5 == total_boxes, f'this is the {total_boxes}'

@then('the footer of this section should have the heading Call Our Local Carpet Cleaning Branch On 020 3519 8926')
def step_then_footer_heading_should_be(context):
    view_gaurentee_footer = context.browser.find_element(*CC_locators.view_gaurantee_section_footer)
    assert "Call Our Local Carpet Cleaning Branch On 020 3519 8926" in view_gaurentee_footer.text

@then('there should be a Need Your Carpet Clean? section')
def step_then_need_your_carpet_clean_section_should_be_present(context):
    context.need_carpet_clean_section = context.browser.find_element(*CC_locators.need_your_carpet_clean_section_main)
    context.need_carpet_clean_section.is_displayed()

@then('it should have a title for the input field')
def step_then_it_should_have_a_title_for_the_input_field(context):
    need_your_carpet_cleaned_input = context.browser.find_element(*CC_locators.need_your_carpet_clean_input_title)
    need_your_carpet_cleaned_input.is_displayed()

@then('there should be an input field')
def step_then_input_field_should_be_present(context):
    need_your_carpet_cleaned_input = context.browser.find_element(*CC_locators.need_your_carpet_clean_input_field)
    need_your_carpet_cleaned_input.is_enabled()
   

@then('there should be a Get a Quote button')
def step_then_get_a_quote_button_should_be_present(context):
    need_your_carpet_cleaned_quote_button = context.browser.find_element(*CC_locators.need_your_carpet_clean_quote_button)
    need_your_carpet_cleaned_quote_button.is_enabled()

@then('there should be an Additional Services heading')
def step_then_additional_services_heading_should_be(context):
    additional_service_heading = context.browser.find_element(*CC_locators.additional_services_heading)
    assert "Additional Cleaning Services For Your Home" in additional_service_heading.text

@then('it should contain the text Call us for a Free Estimate')
def step_then_it_should_contain_text_call_us_for_a_free_estimate(context):
    additional_service_text = context.browser.find_element(*CC_locators.additional_services_call_us_text).text
    assert "Call us for a Free Estimate" in additional_service_text

@then('it should display the phone number')
def step_then_it_should_display_the_phone_number(context):
    additional_service_phone_number = context.browser.find_element(*CC_locators.additional_services_phone_number)
    assert CC_london_data.phone_number in additional_service_phone_number.text

@then('it should include the text Voted #1 carpet cleaner in London. Our customer service hours are 9.00am to 6.00pm 6 days a week.')
def step_then_it_should_include_text_voted_1_carpet_cleaner(context):
    additional_service_voted_text = context.browser.find_element(*CC_locators.additional_services_footer_text)
    assert "Voted #1 carpet cleaner in London. Our customer service hours are 9.00am to 6.00pm 6 days a week." in additional_service_voted_text.text
