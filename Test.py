from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from HomePage import HomePage
from PartnerPage import PartnerPage
from EcosystemPage import EcosystemPage
import time


# THIS TEST WILL HAVE HARDCODED WAIT TIMES TO BETTER SHOW THE TEST STEPS.
# THESE WOULD USUALLY NOT EXIST IN A REGULAR TEST

# Set up the webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to Site
driver.get('https://www.neighborlysoftware.com/')
home = HomePage()
home.wait_for_loaded_homepage(driver)

# Accepting Cookies
time.sleep(2)
home.accept_cookies(driver)

# Navigating to Partners page through header menu
time.sleep(2)
home.click_partners(driver)

# Ensuring we are on Partner's page
partner = PartnerPage()
partner.partner_url_check(driver)

# Click Join the Ecosystem button
time.sleep(2)
partner.click_join_ecosystem(driver)

# Ensuring we are on Join The Ecosystem Page
ecosystem = EcosystemPage()
ecosystem.ecosystem_url_check(driver)

# Inputting data into the fields
ecosystem.fill_out_input_fields(driver)
time.sleep(5)

driver.quit()
