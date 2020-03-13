from selenium import webdriver

username = "username"
password = "password"

url = 'https://web.facebook.com/?_rdc=1&_rdr/'

driver = webdriver.Chrome("C:\chrome driver/chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()

