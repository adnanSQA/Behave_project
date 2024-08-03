from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def before_all(context):
    # This function runs once before all tests
    context.browser = webdriver.Chrome()
    context.action = ActionChains(context.browser)

def after_all(context):
    # This function runs once after all tests
    context.browser.quit()

