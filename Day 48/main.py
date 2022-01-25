from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/bhawesh/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://google.com/")
assert 'Google' in driver.title

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Nest Nepal' + Keys.RETURN)