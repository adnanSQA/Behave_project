from selenium.webdriver.common.by import By


banner_main_heading = (By.XPATH, '//*[@id="bgimage-loc"]/div/div/div/div[1]/div/h1')
banner_input_field = (By.ID, 'postalcode')
banner_get_a_quote_button = (By.XPATH, '//*[@id="formid"]/button')
banner_reviews_image = (By.XPATH, '//*[@id="bgimage-loc"]/div/div/div/div[4]/div/a/img')


content_main_heading = (By.XPATH, '//*[@id="main-content"]/div/div/div/div[1]/h2')
content_image = (By.XPATH, '//*[@id="main-content"]/div/div/div/div[2]/div/img')


view_gaurantee_section = (By.XPATH, '//*[@id="services-guarantee"]')
view_gaurantee_section_main_box = (By.XPATH, '//*[@id="services-guarantee"]/div/div/div[2]')
view_gaurantee_section_footer = (By.XPATH, '//*[@id="bluebg"]/div/div/h3')
view_gaurantee_section_boxes = (By.CSS_SELECTOR, '.col-md-2.col-sm-4.col-xs-12')

need_your_carpet_clean_section_main = (By.XPATH, '//*[@id="location-bg"]/div')
need_your_carpet_clean_input_title = (By.XPATH, '//*[@id="location-bg"]/div/div[2]/div[1]/h5')
need_your_carpet_clean_input_field = (By.XPATH, '//*[@id="postalcode"]')
need_your_carpet_clean_quote_button = (By.XPATH, '//*[@id="formid"]/input[4]')

additional_services_heading = (By.XPATH, '/html/body/section[2]/header/h3')
additional_services_call_us_text = (By.XPATH, '//*[@id="green-rect"]/div/div/div/h5')
additional_services_phone_number = (By.XPATH, '//*[@id="loc_number_k"]')
additional_services_footer_text = (By.XPATH, '//*[@id="green-rect"]/div/div/div/p[1]')