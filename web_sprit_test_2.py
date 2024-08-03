from selenium import webdriver
from selenium.webdriver.firefox.service import Service  # Import Service for geckodriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options  # Import Options if needed
import traceback
import time

# Path to geckodriver
geckodriver_path =  '<path-to-selenium-geckodriver-firefox>' #'/home/Archit/Software/selenium/geckodriver'

# Initialize the Firefox WebDriver with Service
service = Service(executable_path=geckodriver_path)
options = Options()  # Optional: Configure Firefox options if needed
driver = webdriver.Firefox(service=service, options=options)

try:
    # Navigate to the FitPeo Homepage
    driver.get("https://fitpeo.com/revenue-calculator")

  
    # Scroll down to the slider section
    input_element = driver.find_element(By.CSS_SELECTOR,
                                        'input.MuiInputBase-input.MuiOutlinedInput-input.css-1o6z5ng')

    value = input_element.get_attribute('value')
    print(f"The value of the input field is: {value}")

    # Clear the input field
    input_element.click()
    input_element.clear()

    value1 = input_element.get_attribute('value')
    print(f"Second of the input field is: {value1}")

    # Set the new value in the input field
    input_element.send_keys('820')

    value2 = input_element.get_attribute('value')
    print(f"Third is: {value2}")


    # Select CPT codes
    cpt_codes = [
        "CPT-99091",
        "CPT-99453",
        "CPT-99454",
        "CPT-99474"
    ]

    for cpt_code in cpt_codes:
        try:
            # Find the element containing the CPT code
            element = driver.find_element(By.XPATH, f"//p[text()='{cpt_code}']")
            # Print the text of the found element
            print(f"Data for {cpt_code}: {element.text}")

            # Use a relative XPath to find the label and checkbox within the element
            label_element = element.find_element(By.XPATH, ".//following-sibling::label[contains(@class, 'MuiFormControlLabel-root')]")
            checkbox_element = label_element.find_element(By.XPATH, ".//input[@type='checkbox']")

            # Check if the checkbox is selected
            is_checked = checkbox_element.is_selected()
            print(f"Checkbox is {'checked' if is_checked else 'unchecked'}")

            # Optionally, interact with the checkbox (e.g., check it if it's not already checked)
            checkbox_element.click()

            is_checked1 = checkbox_element.is_selected()
            print(f"Second {'checked' if is_checked1 else 'unchecked'}")

        except Exception as e:
            print(f"Error retrieving data for {cpt_code}: {e}")


    time.sleep(10)

    print("All tests passed!-- Value is $110700")



except Exception as e:
    print("An error occurred:", e)
    traceback.print_exc()
finally:
    driver.quit()
