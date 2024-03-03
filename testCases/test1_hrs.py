from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")  # Maximize the browser window
driver = webdriver.Chrome(options=options)
driver.get("https://www.hrs.de/")
time.sleep(3)
driver.find_element_by_xpath("//button[text()='Accept All Cookies']").click()
driver.find_element_by_xpath("//span[@data-test='SearchHotelsButton_span']").click()
driver.find_element(xpath = "//div[@class='DestinationSearchOpener_errorText__z85WF']").click()
driver.find_element(xpath = "//input[@id='DestinationSearchInput']").click()
driver.find_element(xpath = "(//div[text()='Barcelona'])[4]").click()
driver.find_element(xpath = "//div[@class='FramedDatePickerOpener_date__z9igp']").click()
driver.find_element(xpath = "(//div[text()='21'])[2]").click()
driver.find_element(xpath = "(//div[text()='28'])[2]").click()
driver.find_element(xpath = "(//div[@class=\"Month_right__nAPB6\"])[2]/img").click()


