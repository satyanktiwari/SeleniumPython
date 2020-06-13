from selenium import webdriver
import time
import pytest

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path='D:/Satyank/Languages/python/SeleniumPython/venv/drivers/chromedriver.exe')
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_login(self,test_setup):
        driver.get('https://opensource-demo.orangehrmlive.com/')
        driver.find_element_by_id("txtUsername").send_keys('Admin')
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        x = driver.title
        assert x== 'OrangeHRM'
        driver.find_element_by_id("welcome").click()
        driver.find_element_by_link_text("Logout").click()
        time.sleep(2)


    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test completed")