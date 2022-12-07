import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path='/Users/sergeibiryukov/yandex/Sprint_3/chromedriver')
    yield driver
    driver.quit()
