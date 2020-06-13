import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GoogleSearchClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Kalimoh + YouTube")
        self.driver.find_element_by_name("btnK").click()
        x=self.driver.title
        print(x)
        print("Test Completed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        



if __name__ == '__main__':
    unittest.main()
