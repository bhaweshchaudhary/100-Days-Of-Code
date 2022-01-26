from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/bhawesh/Development/chromedriver"
browser = webdriver.Chrome(executable_path=chrome_driver_path)
browser.get("https://instagram.com")

assert 'Instagram' in browser.title

username = browser.find_element(By.NAME, '')

#  TODO: instagram auto login