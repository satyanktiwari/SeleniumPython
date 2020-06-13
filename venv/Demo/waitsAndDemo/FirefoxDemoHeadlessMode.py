from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
path="../drivers/geckodriver.exe"
driver = webdriver.Firefox(executable_path=path,firefox_options=firefox_options)
driver.get('https://google.com')

print(driver.title)
driver.find_element_by_name('q').send_keys('Kalimoh + youtube')
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(2)
print(driver.title)
driver.close()
driver.quit()
print('Test Completed')



# https://seleniumhq.github.io/selenium/docs/=pi/dotnet/html/
# T_OpenQA_Selenium_Firefox_FirefoxOptions.htm
# https://stackoverflow.com/questions/42529853/list-of-firefox-=nd-chrome-arguments-preferences