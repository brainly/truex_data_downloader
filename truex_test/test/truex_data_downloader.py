import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from truex_test.settings import truex_url
from truex_test.pages.login_page import LoginPage
from truex_test.pages.main_page import MainPage


class TruexHappyPath(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        self.driver.get(truex_url)
        self.main_page, self.login_page = MainPage, LoginPage

    def test_ads_pl(self):
        self.login_page.login_into_truex_interface(self)
        self.main_page.date_range_picker(self, last_days=1)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()