from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Function to initialize WebDriver
def initialize_driver():
    options = Options()
    options.add_argument("--start-maximized")  # Maximize the browser window
    driver = webdriver.Chrome(options=options)
    return driver


# Function to perform scenario 1: Navigate to the HRS Website
@pytest.mark.order(1)
def test_navigate_to_hrs_website():
    # Initialize WebDriver
    driver = initialize_driver()
    driver.get("https://www.hrs.de/")
    assert "HRS" in driver.title  # Verify that the homepage is loaded
    driver.quit()


# Function to perform scenario 2: Search for Hotels in Barcelona
@pytest.mark.order(2)
def test_search_for_hotels():
    # Initialize WebDriver
    driver = initialize_driver()
    driver.get("https://www.hrs.de/")
    time.sleep(3)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ESCAPE).perform()
    time.sleep(3)
    driver.find_element_by_xpath("//div[@class='banner-actions-container']/button").click()
    time.sleep(3)
    # Accept Cookies
    # Find the search box using its class name
    search_box = driver.find_element_by_id("DestinationSearchInput")
    search_box.clear()
    search_box.send_keys("Barcelona")
    assert "Barcelona" in driver.title  # Verify search results page loaded
    driver.quit()


if __name__ == "__main__":
    pytest.main()
