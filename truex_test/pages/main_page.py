import datetime
from truex_test.locators.main import *


class MainPage:

    def date_range_picker(self, last_days):
        current_date = datetime.datetime.today()
        for i in range(last_days):
            self.driver.find_element(*drop_down_date).click()
            input_date = current_date - datetime.timedelta(days=i)
            self.driver.find_element(*start_date).clear()
            self.driver.find_element(*start_date).send_keys(input_date.month)
            self.driver.find_element(*start_date).send_keys(input_date.day)
            self.driver.find_element(*end_date).clear()
            self.driver.find_element(*end_date).send_keys(input_date.month)
            self.driver.find_element(*end_date).send_keys(input_date.day)
            self.driver.find_element(*apply_button).click()
            elements = self.driver.find_elements(By.CSS_SELECTOR, data_xpath_selector)
            print("\n" + str(input_date))
            for element in elements:
                print(element.text)
