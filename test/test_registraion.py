from locators.for_registration import TestRegistrationCheckLocators
from pages.creating_data import CreatingData


#проверка регистрации с валидными данными
def test_positive_registration_true(browser):
    reg = TestRegistrationCheckLocators(browser)
    data = CreatingData
    reg.go_to_site()
    reg.click_to_personal_cabinet_button()
    reg.click_to_reg_button()
    reg.send_data_to_name_field("Sergei")
    reg.send_data_to_email_field(data.get_login(browser))
    reg.send_data_to_password_field(data.get_password(browser))
    reg.click_to_registration_button()
    message = reg.find_text(TestRegistrationCheckLocators.ENTER_TEXT)
    assert message.text == "Вход"


#проверка регистрация с невалидным паролем
def test_negative_registration_get_error_true(browser):
    reg = TestRegistrationCheckLocators(browser)
    data = CreatingData
    reg.go_to_site()
    reg.click_to_personal_cabinet_button()
    reg.click_to_reg_button()
    reg.send_data_to_name_field("Sergei")
    reg.send_data_to_email_field(data.get_login(browser))
    reg.send_data_to_password_field(data.get_password_false(browser))
    button = reg.find_element(TestRegistrationCheckLocators.BUTTON_REG, time=10)
    browser.execute_script("return arguments[0].scrollIntoView();", button)
    reg.click_to_registration_button()
    error_message_form = reg.find_element(TestRegistrationCheckLocators.ERROR_MESSAGE, time=3)
    assert error_message_form.text == "Некорректный пароль"