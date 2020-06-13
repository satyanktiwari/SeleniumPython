import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import HtmlTestRunner

#In this browser is opened twice since setUp function is used
# Use the 2nd example if you want to open the browser once.
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_kalimoh(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Kalimoh + YouTube")
        self.driver.find_element_by_name("btnK").click()
        x=self.driver.title
        print(x)
        self.assertEqual(x,"Kalimoh + YouTube - Google Search")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main (testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\Satyank\\Languages\\python\\SeleniumPython\\venv\\reports'),verbosity=2)
