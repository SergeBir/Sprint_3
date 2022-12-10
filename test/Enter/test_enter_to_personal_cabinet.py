from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.ForEnter import TestEnterCheckLocators


def test_enter_to_personal_cabinet_true(browser):
    reg = TestEnterCheckLocators(browser)
    reg.go_to_site()
    reg.click_to_personal_cabinet_button()
    reg.send_data_to_email_field("sergamer@ya.ru")
    reg.send_data_to_password_field("1234567")
    reg.click_to_enter_button()
    WebDriverWait(browser, 3).until(
        expected_conditions.presence_of_element_located(TestEnterCheckLocators.MAKE_ORDER))
    button = reg.find_text(TestEnterCheckLocators.MAKE_ORDER)
    assert button.text == "Оформить заказ"






    # reg.click_to_personal_cabinet_button()
    # reg.click_to_personal_cabinet_button()
    # WebDriverWait(browser, 3).until(
    #     expected_conditions.visibility_of_element_located(TestEnterCheckLocators.PROFILE_BUTTON))
    # reg.click_to_profile_button()
    # WebDriverWait(browser, 3).until(
    #     expected_conditions.presence_of_element_located(TestEnterCheckLocators.PERSONAL_DATA_TEXT))
    # message = reg.find_element(TestEnterCheckLocators.PERSONAL_DATA_TEXT, time=10)
    # assert message.text == "В этом разделе вы можете изменить свои персональные данные"


