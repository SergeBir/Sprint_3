from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.ForEnter import TestEnterCheckLocators


def test_enter_to_constructor_true(browser):
    reg = TestEnterCheckLocators(browser)
    reg.go_to_site()
    reg.click_to_personal_cabinet_button()
    reg.send_data_to_email_field("sergamer@ya.ru")
    reg.send_data_to_password_field("1234567")
    reg.click_to_enter_button()
    reg.click_to_personal_cabinet_button()
    reg.click_to_personal_cabinet_button()
    WebDriverWait(browser, 5).until(
        expected_conditions.element_to_be_clickable(TestEnterCheckLocators.STELLAR_BURGER_ELEMENT))
    reg.click_to_constructor_form()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(TestEnterCheckLocators.CONSTRUCT_BURGER_TEXT))
    burger_text = reg.find_text(TestEnterCheckLocators.CONSTRUCT_BURGER_TEXT)
    assert burger_text.text == "Соберите бургер"
