# Step 1: Open browser
# Step 2: Open Instagram.com
# Step 3: Open another tab
# Step 4: Open temp-mail.org and copy the mail
# Step 5: Go back to instagram tab
# Step 6: Click on signup button
# Step 7: Fill in the details along with the copied mail
# Step 8: go back to temp-mail tab and click on newly arrived mail then copy the code
# Step 9: go back to insta tab and paste the code
# to be continue...

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

INSTAURL = 'https://instagram.com'
s = Service('/Users/bhawesh/Desktop/geckodriver')
driver = webdriver.Firefox(service=s)
driver.get(INSTAURL)
signup = driver.find_element(By.XPATH('//a[@data-testid="sign-up-link"]'))
signup.click()
