from selenium import webdriver


caps = webdriver.DesiredCapabilities.INTERNETEXPLORER
caps['ignoreProtectedModeSettings']=True
path = "../drivers/IEDriverServer.exe"

driver = webdriver.Ie(executable_path=path, desired_capabilities=caps)
driver.get("https://google.com")
print("google opened now finding q")

driver.find_element_by_name('q').send_keys('Kalimoh + youtube')
time.sleep(2)
driver.find_element_by_name("btnK").click()
print(driver.title)
driver.quit()
print("Test completed")