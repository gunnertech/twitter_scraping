from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
import json
import datetime

driver = webdriver.Safari()
# driver.implicitly_wait(10)

driver.get("https://twitter.com/gunnertech")
sleep(1)
# driver.set_window_size(1, 1)
driver.find_element_by_css_selector("div.LoginForm-username input").send_keys("gunnertech")
driver.find_element_by_css_selector("div.LoginForm-password input").send_keys("Twi2010!!")
driver.find_element_by_css_selector("form.js-front-signin input.js-submit").click()

while True:
    sleep(1)
    for button in driver.find_elements_by_css_selector("button.ProfileTweet-actionButton.js-dropdown-toggle"):
        button.click()
        sleep(1)
        driver.find_element_by_css_selector("li.js-actionDelete button").click()
        sleep(1)
        driver.find_element_by_css_selector("button.delete-action").click()
        sleep(1)
    driver.refresh()

print('all done here')
driver.close()
