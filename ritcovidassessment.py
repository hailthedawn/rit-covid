from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"

driver = webdriver.Chrome('./chromedriver.exe') # or wherever the path to the chromedriver file is
url = "https://dailyhealth.rit.edu/assessment"
driver.get(url)

delay = 3  # seconds
try:
    myElem = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div[2]/form/div[1]/div/input')))
    # Logging in to RIT shibboleth
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[1]/div/input").send_keys(username)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[2]/div/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/button").click()
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div/div/div[1]/div[2]/div/div/a')))
			driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[1]/div[2]/div/div/a").click()
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div/div[2]')))
			driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div/div[2]").click()
            driver.close()
        except TimeoutException:
            print("Page TimeoutException")
    except TimeoutException:
        print("Page TimeoutException")
except TimeoutException:
    print("Page TimeoutException")
