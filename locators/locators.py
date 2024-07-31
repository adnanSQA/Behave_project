from selenium.webdriver.common.by import By


navbar = (By.ID, 'myheader')
navbar_logo = (By.CLASS_NAME, 'main-logo')
navbar_phone_number = (By.CLASS_NAME, 'num_replace')
navbar_opening_hours = (By.CLASS_NAME, 'opening')
banner_review_below = (By.XPATH, '//*[@id="rating"]/div/div/div/div/div/p')
banner_inputfield = (By.ID, 'postalcode')
main_page_banner_text = (By.XPATH, '//*[@id="bgimage"]/div/div/div[1]/div/div/h1')
main_page_bullet_points = (By.CLASS_NAME, 'home-bullets')
banner_quote_button = (By.XPATH, '//*[@id="formid"]/button')
li_tag = (By.TAG_NAME, 'li')
