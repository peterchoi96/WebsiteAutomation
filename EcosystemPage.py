from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class EcosystemPage(object):

    def __init__(self):
        driver = object

    def ecosystem_url_check(self, driver):
        ecoPageURL = driver.current_url
        try:
            assert ecoPageURL == 'https://www.neighborlysoftware.com/join-the-ecosystem/'
        except AssertionError:
            print("Wrong URL")
        return self

    def fill_out_input_fields(self, driver):
        # Must traverse through iFrame to access input fields
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, "//iframe[@id='hs-form-iframe-0']")))
        iframe = driver.find_element(By.XPATH, "//iframe[@id='hs-form-iframe-0']")
        driver.switch_to.frame(iframe)

        driver.find_element(By.NAME, "email").send_keys("Test.Email@gmail.com")
        time.sleep(1)
        driver.find_element(By.NAME, "firstname").send_keys("Test")
        time.sleep(1)
        driver.find_element(By.NAME, "lastname").send_keys("User")
        time.sleep(1)
        driver.find_element(By.NAME, "phone").send_keys("1234567890")
        time.sleep(1)
        driver.find_element(By.NAME, "state").send_keys("ga")
        time.sleep(1)
        driver.find_element(By.NAME, "city").send_keys("Atlanta")
        time.sleep(1)
        driver.find_element(By.NAME, "company").send_keys("Test Company")
        time.sleep(1)
        driver.find_element(By.NAME, "message").send_keys("I will not click submit because this is a test.")

        # Traversing out of iFrame
        driver.switch_to.default_content()
        return self

