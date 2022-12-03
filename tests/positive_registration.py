from selenium import webdriver
from selenium.webdriver.common.by import By
from test_locators.for_registration import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def check_registration():

    locator = TestLocators()

    driver = webdriver.Chrome(executable_path='/Users/sergeibiryukov/yandex/Sprint_3/chromedriver')
    driver.get('https://stellarburgers.nomoreparties.site')
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        TestLocators.PERSONAL_CABINET_BUTTON))
    driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*TestLocators.AUTHORIZATION_BUTTON).click()
    driver.find_element(*TestLocators.NAME_LINE).send_keys("Sergei")
    login = TestLocators.get_login(locator)
    print(f"Login {login}")
    driver.find_element(*TestLocators.EMAIL_LINE).send_keys(login)
    password = TestLocators.get_password(locator)
    print(f"Password {password}")
    driver.find_element(*TestLocators.PASSWORD_LINE).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_REG).click()
    assert len(TestLocators.FORM) == 2

    driver.quit()


if __name__ == "__main__":
    check_registration()