from selenium.webdriver.common.by import By


class PartnerPage(object):

    def __init__(self):
        driver = object

    def partner_url_check(self, driver):
        partnerPageURL = driver.current_url
        try:
            assert partnerPageURL == 'https://www.neighborlysoftware.com/about-us/partners/'
        except AssertionError:
            print("Wrong URL")
        return self

    def click_join_ecosystem(self, driver):
        driver.find_element(By.XPATH, "//*[contains(text(), 'JOIN THE ECOSYSTEM')]").click()
        return self
