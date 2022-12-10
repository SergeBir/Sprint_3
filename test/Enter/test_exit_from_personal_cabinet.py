from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.ForEnter import TestEnterCheckLocators


def test_exit_from_personal_cabinet_true(browser):
    reg = TestEnterCheckLocators(browser)
    reg.go_to_site()
    reg.click_to_personal_cabinet_button()
    reg.send_data_to_email_field("sergamer@ya.ru")
    reg.send_data_to_password_field("1234567")
    reg.click_to_enter_button()
    reg.click_to_personal_cabinet_button()
    reg.click_to_personal_cabinet_button()
    WebDriverWait(browser, 5).until(
              expected_conditions.element_to_be_clickable(TestEnterCheckLocators.PROFILE_BUTTON))
    reg.click_to_profile_button()
    WebDriverWait(browser, 5).until(
         expected_conditions.visibility_of_element_located(TestEnterCheckLocators.EXIT_BUTTON))
    reg.click_to_exit_button()
    enter_message = reg.find_text(TestEnterCheckLocators.ENTER_TEXT)
    assert enter_message.text == "Вход"
