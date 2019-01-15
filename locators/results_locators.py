from selenium.webdriver.common.by import By


results_locators = {
    "results_page": (By.ID, 'rightResultsATF'),
    "first_item": (By.ID, 'pdagDesktopSparkleHeadline'),
    "titles": (By.CSS_SELECTOR, '.s-color-twister-title-link.a-text-normal'),
    "dates": (By.CSS_SELECTOR, '.a-size-small.a-color-secondary'),
    "authors": (By.CSS_SELECTOR, '.a-row.a-spacing-none'),
    "prices": (By.CSS_SELECTOR, '.sx-price-whole'),
    "stars": (By.CSS_SELECTOR, '.a-column.a-span5.a-span-last'),
    "reviews": (By.CSS_SELECTOR, '.a-size-small.a-link-normal.a-text-normal'),
    "next_page": (By.ID, 'pagnNextString'),
    "current_page_nav": (By.ID, 'pagn'),
    "current_page": (By.CLASS_NAME, 'pagnCur')
}