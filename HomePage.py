from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class HomePage(object):

    def __init__(self):
        driver = object

    def click_partners(self, driver):
        driver.find_element(By.ID, "menu-item-1828").click()
        time.sleep(2)
        driver.find_element(By.ID, "menu-item-624").click()
        return self

    def wait_for_loaded_homepage(self, driver):
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "body > div.fl-page > header")))
        return self

    def accept_cookies(self, driver):
        driver.find_element(By.ID, "cookie_action_close_header").click()
        return self
