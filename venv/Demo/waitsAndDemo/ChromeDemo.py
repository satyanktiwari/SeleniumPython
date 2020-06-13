from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:/Satyank/Languages/python/SeleniumPython/venv/drivers/chromedriver.exe")
driver.set_page_load_timeout(10)
driver.maximize_window()
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("kalimoh+youtube")
time.sleep(1)
driver.find_element_by_name("btnK").click()
time.sleep(2)

driver.close()
driver.quit()

print("Test Completed")