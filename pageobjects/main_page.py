import pytest
from selenium.common.exceptions import NoSuchElementException
from locators.main_page_locators import search_bar_locators


@pytest.mark.usefixtures("driver_init")
class AmazonSearchBar:
    """methods for the start page that has the amazon search bar"""
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        try:
            self.driver.find_element(*search_bar_locators["search_bar"])
            return True
        except NoSuchElementException:
            return False

    def search_for(self, search_value):
        search_bar = self.driver\
            .find_element(*search_bar_locators["search_bar"])
        search_bar.send_keys(search_value)
        search_bar.submit()
