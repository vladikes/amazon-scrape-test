import pytest
from pathlib import Path
from selenium import webdriver

chrome_driver_path = str(Path.cwd() / "chromedriver")

pytest.fixture(scope="class")
def driver_init(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(chrome_driver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()
    driver.quit() 
