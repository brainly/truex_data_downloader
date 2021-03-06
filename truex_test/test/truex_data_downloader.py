import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from truex_test.settings import TRUEX_URL
from truex_test.pages.login_page import LoginPage
from truex_test.pages.main_page import MainPage
from truex_test.helpers import print_json_data


class TruexHappyPath(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        self.driver.get(TRUEX_URL)
        self.main_page, self.login_page = MainPage(self.driver), LoginPage(self.driver)

    def test_ads_pl(self):
        self.login_page.login_into_truex_interface()
        truex_data = self.main_page.get_data_from_last_days(last_days=3)
        print_json_data(truex_data)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
