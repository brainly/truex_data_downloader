from selenium.webdriver.common.by import By

drop_down_date = (By.XPATH, "//h3[@class='date-range-display icon-carrot icon-after']")
start_date = (By.ID, "start_date_filter_input")
end_date = (By.ID, "end_date_filter_input")
apply_button = (By.ID, "apply_date_range_filter")
data_value_xpath_selector = (By.CSS_SELECTOR, ".clearfix h4")
data_label_xpath_selector = (By.CSS_SELECTOR, ".clearfix p")
