import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
#In this browser is opened twice since setUp function is used
# Use the 2nd example if you want to open the browser once.
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search_kalimoh(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Kalimoh + YouTube")
        self.driver.find_element_by_name("btnK").click()
        x=self.driver.title
        print(x)
        self.assertEqual(x,"Kalimoh + YouTube - Google Search")

    def test_search_Satyank(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Satyank tiwari")
        self.driver.find_element_by_name("btnK").click()
        x=self.driver.title
        print(x)
        self.assertEqual(x,"Satyank tiwari - Google Search")
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
