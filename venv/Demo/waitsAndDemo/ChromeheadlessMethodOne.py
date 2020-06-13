from selenium import webdriver


# To run in headless mode
# add variable chrome_options and then instantiate
# then modify driver variable
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
#Below code will give warning and hence using options instead of chrome_options
#driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="../drivers/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options,executable_path="../drivers/chromedriver.exe")
driver.get("https://google.com")
print(driver.title)
driver.close()
driver.quit()
print('Test completed')