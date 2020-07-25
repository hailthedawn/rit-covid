from datetime import datetime
import smtplib
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

load_dotenv()


def sendMessage():
    # If you're using Gmail to send the message, you might need to
    # go into the security settings of your email account and
    # enable the "Allow less secure apps" option
    username = os.getenv("EMAIL")
    password = os.getenv("EMAIL_PASSWORD")

    vtext = os.getenv("PHONE_NUMBER") + "@vtext.com"
    message = "\nSuccessfully filled out RIT COVID Assessment on " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print(message)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, vtext, message)
    server.quit()

    print('Completed and Sent')

driver = webdriver.Chrome('./chromedriver')
url = "https://dailyhealth.rit.edu/assessment"
driver.get(url)

delay = 3  # seconds
try:
    myElem = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div[2]/form/div[1]/div/input')))
    # Logging in to RIT shibboleth
    driver.find_element_by_xpath(
        "/html/body/div[2]/div/div[2]/form/div[1]/div/input").send_keys(
            os.getenv("RIT_USERNAME"))
    driver.find_element_by_xpath(
        "/html/body/div[2]/div/div[2]/form/div[2]/div/input").send_keys(
            os.getenv("RIT_PASSWORD"))
    driver.find_element_by_xpath(
        "/html/body/div[2]/div/div[2]/form/button").click()
    try:
        myElem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div[1]/div/div/div[1]/div[2]/div/div/a')))
        driver.find_element_by_xpath(
            "/html/body/div/div[1]/div/div/div[1]/div[2]/div/div/a").click()
        try:
            myElem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div/div[2]')))
            driver.find_element_by_xpath(
                "/html/body/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div/div[2]").click()
            sendMessage()
        except TimeoutException:
            print("Page TimeoutException")
    except TimeoutException:
        print("Page TimeoutException")
except TimeoutException:
    print("Page TimeoutException")
