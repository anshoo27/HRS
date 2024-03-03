#import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pytest


# Function to initialize WebDriver
def initialize_driver():
    options = Options()
    options.add_argument("--start-maximized")  # Maximize the browser window
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.mark.order(1)
# Function to perform scenario 1: Navigate to the HRS Website
def navigate_to_hrs_website(driver):
    driver.get("https://www.hrs.de/")
    assert "HRS" in driver.title  # Verify that the homepage is loaded


# Function to perform scenario 2: Search for Hotels in Barcelona
def search_for_hotels(driver):
    search_box = driver.find_element_by_class("DestinationSearchOpener_destinationFormat__hwuCN")
    search_box.clear()
    search_box.send_keys("Barcelona")
    assert "Barcelona" in driver.title  # Verify that the search results page loaded


# Function to perform the main test script
def main():
    # Initialize WebDriver
    driver = initialize_driver()
    navigate_to_hrs_website(driver)
    search_for_hotels(driver)
    #driver.quit()


if __name__ == "__main__":
    main()
