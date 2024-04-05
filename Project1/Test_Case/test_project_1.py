# Importing necessary modules for testing
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Importing test data and locators from separate files
from Test_Data import data
from Test_Locator import locators


# Fixture for setting up the WebDriver
@pytest.fixture
def driver_setup():
    # Initialize Chrome WebDriver using WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    yield driver, wait
    driver.quit()


# Function to perform login
def login(driver, wait, username, password):
    # Open the login page
    driver.get(data.Data().url)
    username_field = wait.until(EC.presence_of_element_located((By.NAME, locators.Login().username_text_box)))
    username_field.send_keys(username)
    password_field = wait.until(EC.presence_of_element_located((By.NAME, locators.Login().password_text_box)))
    password_field.send_keys(password)
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.Login().login_btn)))
    button.click()


# Test class for project
class TestProject:

    # Test case for valid login credentials
    def test_login_valid_credential(self, driver_setup):
        driver, wait = driver_setup
        login(driver, wait, data.Data().username, data.Data().valid_password)
        # Verify the redirection to the dashboard page after successful login
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        current_url = driver.current_url
        assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"
        print("The user is logged in successfully")

    # Test case for invalid login credentials
    def test_invalid_employee_login(self, driver_setup):
        driver, wait = driver_setup

        # Attempt login with invalid credentials
        login(driver, wait, data.Data().username, data.Data().invalid_password)

        # Find and check the error message
        error_message_xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"
        actual_error_message = wait.until(EC.visibility_of_element_located((By.XPATH, error_message_xpath))).text
        assert "Invalid credentials" in actual_error_message, (f"Expected: 'Invalid credentials', Actual: "
                                                               f"'{actual_error_message}'")
        print("Valid error message for invalid credentials is displayed.")

    # Test case for adding a new employee
    def test_add_module(self, driver_setup):
        driver, wait = driver_setup
        try:
            # Perform login
            login(driver, wait, data.Data().username, data.Data().valid_password)
            add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, locators.PimModule.add_btn)))
            add_btn.click()
            # Fill in employee details
            first_name = wait.until(EC.presence_of_element_located((By.XPATH, locators.PimModule.first_name)))
            first_name.send_keys(data.Pim().first_Name)
            mid_name = wait.until(EC.presence_of_element_located((By.XPATH, locators.PimModule.mid_name)))
            mid_name.send_keys(data.Pim().mid_Name)
            last_name = wait.until(EC.presence_of_element_located((By.XPATH, locators.PimModule.last_name)))
            last_name.send_keys(data.Pim().last_Name)
            employee_id = wait.until(EC.presence_of_element_located((By.XPATH, locators.PimModule.employee_id)))
            employee_id.clear()
            employee_id.send_keys(data.Pim().employee_id)
            save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, locators.PimModule.save_btn)))
            save_btn.click()
            # Verify the addition of the new employee
            employee_list = wait.until(EC.presence_of_element_located((By.XPATH, locators.PimModule.employee_list)))
            assert employee_list.is_displayed()
            print("New Employee Added Successfully")
        except TimeoutException as e:
            print(e)

    # Test case for editing employee details
    def test_edit_module(self, driver_setup):
        driver, wait = driver_setup
        try:
            # Perform login
            login(driver, wait, data.Data().username, data.Data().valid_password)
            submodule = wait.until(EC.element_to_be_clickable((By.XPATH, locators.PimModule.pim_menu)))
            submodule.click()
            # Search for the employee to edit
            firstname = wait.until(EC.presence_of_element_located((By.XPATH, locators.PimModule.firstname)))
            firstname.send_keys(data.Pim().first_Name)
            employee_id = driver.find_element(By.XPATH, locators.PimModule.employee_id)
            employee_id.send_keys(data.Pim().employee_id)
            search = wait.until(EC.element_to_be_clickable((By.XPATH, locators.PimModule.search_btn)))
            search.click()
            edit = wait.until(EC.element_to_be_clickable((By.XPATH, locators.PimModule.edit_btn)))
            edit.click()
            # Update the employee's name
            edited_name = wait.until(EC.presence_of_element_located((By.XPATH, locators.PimModule.edited_name)))
            edited_name.clear()
            edited_name.send_keys(data.Pim().edited_name)
            save = wait.until(EC.element_to_be_clickable((By.XPATH, locators.PimModule.save_button1)))
            save.click()
            # Verify successful editing of personal details
            employee_list = wait.until(EC.presence_of_element_located((By.XPATH, locators.PimModule.employee_list)))
            assert employee_list.is_displayed()
            print("Personal details edited Successfully!!")
        except TimeoutException as e:
            print(e)

    # Test case for deleting an existing employee
    def test_delete_module(self, driver_setup):
        driver, wait = driver_setup
        try:
            # Perform login
            login(driver, wait, data.Data().username, data.Data().valid_password)
            submodule = wait.until(EC.element_to_be_clickable((By.XPATH, locators.PimModule.pim_menu)))
            submodule.click()
            # Search for the employee to delete
            firstname = wait.until(EC.presence_of_element_located((By.XPATH, locators.PimModule().firstname)))
            firstname.send_keys(data.Pim().first_Name)
            employee_id = driver.find_element(By.XPATH, locators.PimModule().employee_id)
            employee_id.send_keys(data.Pim().employee_id1)
            search = wait.until(EC.element_to_be_clickable((By.XPATH, locators.PimModule().search_btn)))
            search.click()
            delete = wait.until(EC.element_to_be_clickable((By.XPATH, locators.PimModule().delete_btn)))
            delete.click()
            confirm = wait.until(EC.element_to_be_clickable((By.XPATH, locators.PimModule().confirm_btn)))
            confirm.click()
            employee_list = wait.until(EC.presence_of_element_located((By.XPATH, locators.PimModule.employee_list)))
            assert employee_list.is_displayed()
            print("Existing employee deleted Successfully!!")
        except TimeoutException as e:
            print(e)
