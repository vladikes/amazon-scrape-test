import pytest
from selenium.common.exceptions import NoSuchElementException
from locators.results_locators import results_locators


@pytest.mark.usefixtures("driver_init")
class AmazonSearchBar:
    """methods for the start page that has the amazon search bar"""
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        try:
            self.driver.find_element(*results_locators["first_item"])
            return True
        except NoSuchElementException:
            return False