import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
driver.maximize_window()


driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Kalimoh + YouTube")
wait = WebDriverWait(driver,10 )
try:
    element = wait.until(EC.element_to_be_clickable((By.NAME,"btnK1")))
    print("element is clickable")
except:
    print("element not clickable")
    driver.close()
    exit(1)
element.click()
# driver.find_element_by_name("btnK").click()
x=driver.title
print(x)
print("Test Completed")
driver.close()
driver.quit()

