from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# To run in headless mode option 2

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
#Below code will give warning and hence using options instead of chrome_options
#driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="../drivers/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options,executable_path="../drivers/chromedriver.exe")
driver.get("https://google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Kalimoh + youtube")
driver.find_element_by_name('btnK').click()
print(driver.title)
driver.close()
driver.quit()
print('Test completed')