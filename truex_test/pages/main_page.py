import datetime
from truex_test.locators.main import *
from typing import Dict, Any
from selenium.webdriver.common.keys import Keys


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def get_data_from_specific_day(self, input_date: datetime) -> Dict[str, Any]:
        self.driver.find_element(*drop_down_date).click()
        self.driver.find_element(*start_date).clear()
        self.driver.find_element(*start_date).send_keys(str(input_date.month) + Keys.SPACE)
        self.driver.find_element(*start_date).send_keys(input_date.day)
        self.driver.find_element(*end_date).clear()
        self.driver.find_element(*end_date).send_keys(str(input_date.month) + Keys.SPACE)
        self.driver.find_element(*end_date).send_keys(input_date.day)
        self.driver.find_element(*apply_button).click()
        return self.__extract_data_for_page()

    def get_data_from_last_days(self, last_days: int) -> Dict[str, Dict[str, Any]]:
        current_date = datetime.datetime.today()
        truex_data = {}
        for i in range(last_days):
            input_date = current_date - datetime.timedelta(days=i)
            truex_data[str(input_date).split()[0]] = self.get_data_from_specific_day(input_date)
        return truex_data

    def __extract_data_for_page(self) -> Dict[str, any]:
        data_dict = {}
        labels, values = self.driver.find_elements(*data_label_xpath_selector), self.driver.find_elements(*data_value_xpath_selector)
        for label, value in zip(labels, values):
            data_dict[label.text] = value.text
        return data_dict
