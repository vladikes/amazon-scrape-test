import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.results_locators import results_locators
import re


@pytest.mark.usefixtures("driver_init")
class ResultsPage:
    """methods for the search results page """

    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        try:
            self.driver.find_element(*results_locators["results_page"])
            return True
        except NoSuchElementException:
            return False

    def get_item_titles(self):
        all_titles = self.driver.find_elements(*results_locators["titles"])
        title_results_list = [title.text for title in all_titles]

        return title_results_list

    def get_item_dates(self):
        pattern = r'[A-Za-z]{3} \d\d?, \d{4}'
        all_dates = self.driver.find_elements(*results_locators["dates"])
        date_results_list = [date.text for date in all_dates]
        clear_date_results = [d for d in date_results_list
                              if re.findall(pattern, d)]
        return clear_date_results

    def get_item_authors(self):
        all_authors = self.driver.find_elements(*results_locators["authors"])
        author_results_list = [author.text for author in all_authors
                               if author.text.startswith("by")]
        return author_results_list

    def get_item_prices(self):
        all_prices = self.driver.find_elements(*results_locators["prices"])
        price_results_list = [price.text for price in all_prices]
        return price_results_list

    def get_item_stars(self):
        pattern = r'(\d\.?\d?.out.of.\d.stars)'
        all_stars = self.driver.find_elements(*results_locators["stars"])
        star_results_list = [star.get_attribute('innerText').rstrip()
                             for star in all_stars]
        clear_star_results = [d for d in star_results_list
                              if re.findall(pattern, d)]

        return clear_star_results

    def get_item_reviews(self):
        all_reviews = self.driver.find_elements(*results_locators["reviews"])
        review_results_list = [review.text for review in all_reviews
                               if review.text.isdigit()]
        return review_results_list

    def get_current_page(self):
        cur = self.driver.find_elements(*results_locators["current_page"])
        current_page_result = [page.get_attribute('textContent')
                               for page in cur]

        return current_page_result[0]

    def navigate_to_next_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located
                   (results_locators["next_page"]))
        next_page_button = self.driver\
            .find_element(*results_locators["next_page"])
        next_page_button.click()