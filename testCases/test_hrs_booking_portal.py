import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    # Configure ChromeOptions
    chrome_options = Options()
    # Add any desired options here, e.g., headless mode
    # chrome_options.add_argument("--headless")

    # Initialize WebDriver with ChromeOptions
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    # Teardown - close the browser
    driver.quit()

def test_hrs_booking_portal(browser):
    # Navigate to the HRS Online Booking Portal
    browser.get("https://www.hrs.de/")
    # Example test: verify page title
    assert "HRS" in browser.title
