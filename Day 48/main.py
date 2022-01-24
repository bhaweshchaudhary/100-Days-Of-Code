from selenium import webdriver

chrome_driver_path = "/Users/bhawesh/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://facebook.com")

driver.quit()