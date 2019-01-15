import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.main_page import AmazonSearchBar
from locators.item_locators import item_locators


@pytest.mark.usefixtures("driver_init")
class TestAmazonSearch:

    @pytest.mark.parametrize("url", ["https://www.amazon.com"])
    def test_should_load_search_bar(self, url):
        search_bar = AmazonSearchBar(self.driver)
        self.driver.get(url)
        assert search_bar.is_loaded() is True

    def test_should_search(self):
        search_bar = AmazonSearchBar(self.driver)
        search_bar.search_for("software testing")

    def test_should_select_item(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(item_locators["items"]))
        item_button = self.driver. \
            find_element(*item_locators["items"])
        item_button.click()

    def test_should_click_add_to_cart(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located
                   (item_locators["add_to_cart_button"]))
        add_button = self.driver. \
            find_element(*item_locators["add_to_cart_button"])
        add_button.click()

    def test_should_confirm_item_addition(self):
        confirmation_string = "Added to Cart"
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located
                   (item_locators["cart_confirmation"]))
        confirm_item_in_cart = self.driver. \
            find_element(*item_locators["cart_confirmation"])
        assert confirm_item_in_cart.get_attribute('innerText') == confirmation_string
