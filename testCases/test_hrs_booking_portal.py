import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Initialize WebDriver with correct path to chromedriver executable
    driver = webdriver.Chrome("/Users/mac/Documents/Project/hrs_booking_automation/HRS/chromedriver/chromedriver")
    yield driver
    # Teardown - close the browser
    driver.quit()

def test_hrs_booking_portal(browser):
    # Navigate to the HRS Online Booking Portal
    browser.get("https://www.hrs.de/")
    # Example test: verify page title
    assert "HRS" in browser.title
