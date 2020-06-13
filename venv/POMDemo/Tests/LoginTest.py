from selenium import webdriver
import time
import unittest
import HtmlTestRunner
# Below 3 imports to be made before the POM to ensure scripts can be run from cmd
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),"...",".."))
from POMDemo.Pages.loginPage import LoginPage
from POMDemo.Pages.homePage import HomePage



class loginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/Satyank/Languages/python/SeleniumPython/venv/drivers/chromedriver.exe")
        cls.driver.set_page_load_timeout(10)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        # Create object of loginPage
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('test completed')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Satyank/Languages/python/SeleniumPython/venv/reports'),verbosity=2)