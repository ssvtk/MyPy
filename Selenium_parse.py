from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://31.220.42.115:3000/')
login_button = driver.find_element_by_id('link-to-login')
login_button.click()
login_form = driver.find_element_by_xpath('//*[@id="spree_user_email"]')
login_form.clear()
login_form.send_keys('vyzenef@mailinator.com')
password = driver.find_element_by_xpath('//*[@id="spree_user_password"]')
password.clear()
password.send_keys('qwe123')
password.send_keys(Keys.RETURN)
login_button.text

## vyzenef@mailinator.com
## qwe123