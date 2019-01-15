from selenium.webdriver.common.by import By


item_locators = {
    "items": (By.CSS_SELECTOR, '.s-color-twister-title-link.a-text-normal'),
    "loaded_item": (By.ID, 'buybox'),
    "add_to_cart_button": (By.ID, 'add-to-cart-button'),
    "cart_confirmation": (By.CSS_SELECTOR, '.a-size-medium.a-text-bold')
}