import pytest
from helpers.results_helper import ResultHelper
from pageobjects.main_page import AmazonSearchBar
from pageobjects.results_page import ResultsPage


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

    def test_should_write_to_csv(self):
        num_of_pages = 4
        scraper = ResultHelper
        results_page = ResultsPage(self.driver)

        titles = results_page.get_item_titles()
        dates = results_page.get_item_dates()
        authors = results_page.get_item_authors()
        prices = results_page.get_item_prices()
        stars = results_page.get_item_stars()
        reviews = results_page.get_item_reviews()

        for i in range(0, num_of_pages):
            scraper.set_results(titles, dates, authors, prices, stars, reviews)
            scraper.write_to_csv()
            results_page.navigate_to_next_page()
