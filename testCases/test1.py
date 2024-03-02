import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Function to initialize WebDriver
def initialize_driver():
    options = Options()
    options.add_argument("--start-maximized")  # Maximize the browser window
    driver = webdriver.Chrome(options=options)
    return driver

# Function to perform scenario 1: Navigate to the HRS Website
def navigate_to_hrs_website(driver):
    driver.get("https://www.hrs.de/")
    assert "HRS" in driver.title  # Verify that the homepage is loaded successfully

# Function to perform scenario 2: Search for Hotels in Barcelona
def search_for_hotels(driver):
    search_box = driver.find_element_by_id("destination")
    search_box.clear()
    search_box.send_keys("Barcelona")
    check_in_date = driver.find_element_by_id("checkin_date")
    check_in_date.clear()
    check_in_date.send_keys("21/06/2024")
    check_out_date = driver.find_element_by_id("checkout_date")
    check_out_date.clear()
    check_out_date.send_keys("28/06/2024")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for the search results page to load
    assert "Barcelona" in driver.title  # Verify that the search results page is loaded successfully

# Function to perform scenario 3: Filter Hotels by Availability
def filter_hotels_by_availability(driver):
    availability_filter = driver.find_element_by_xpath("//label[contains(text(),'High Availability')]/preceding-sibling::input[@type='checkbox']")
    availability_filter.click()
    time.sleep(2)  # Wait for the search results to be updated
    # Verify that only hotels with high availability are displayed

# Function to perform scenario 4: Select a Hotel
def select_hotel(driver):
    first_hotel = driver.find_element_by_xpath("//div[@class='hotel_list_item_wrapper']/a")
    first_hotel.click()
    time.sleep(2)  # Wait for the hotel details page to load
    assert "Hotel Details" in driver.title  # Verify that the hotel details page is loaded successfully

# Function to perform scenario 5: Book a Hotel
def book_hotel(driver):
    book_button = driver.find_element_by_xpath("//button[contains(text(),'Book Now')]")
    book_button.click()
    time.sleep(2)  # Wait for the booking form to load
    # Fill in the booking form with guest details and complete the booking process

# Function to perform scenario 6: Check Booking Details
def check_booking_details(driver):
    # Navigate to the user's booking history or confirmation email
    # Verify that the booked hotel and travel dates match the user's selections

# Function to perform scenario 7: View Hotel Details
def view_hotel_details(driver):
    driver.back()  # Navigate back to the hotel details page
    time.sleep(2)  # Wait for the page to load
    # Verify that all relevant information (amenities, room types, location, etc.) is displayed accurately

# Function to perform scenario 8: Navigate Home
def navigate_home(driver):
    home_button = driver.find_element_by_xpath("//a[@class='logo_link']")
    home_button.click()
    time.sleep(2)  # Wait for the homepage to load
    assert "HRS" in driver.title  # Verify that the homepage is loaded successfully

# Function to perform scenario 9: Logout (if applicable)
def logout(driver):
    # Navigate to the account settings or logout option
    # Verify that the user is logged out successfully

# Main function to execute the test script
def main():
    driver = initialize_driver()
    navigate_to_hrs_website(driver)
    search_for_hotels(driver)
    filter_hotels_by_availability(driver)
    select_hotel(driver)
    book_hotel(driver)
    check_booking_details(driver)
    view_hotel_details(driver)
    navigate_home(driver)
    logout(driver)
    driver.quit()

if __name__ == "__main__":
    main()
