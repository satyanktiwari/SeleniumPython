from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://google.com")
time.sleep(3)
driver.close()
driver.quit()
print("Completed")


# Webdrivermanager for python
# https://github.com/SergeyPirogov/webdriver_manager