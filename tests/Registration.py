from locators.ForRegistration import RegistrationHelper
from pages.CreatingData import CreatingData

"""Тесты на проверку регситрации с валидными и невалидными данными"""


#регистрация с валидными данными
def test_positive_registration_true(browser):
    reg_main_page = RegistrationHelper(browser)
    data = CreatingData()
    reg_main_page.go_to_site()
    reg_main_page.click_on_the_cabinet_button()
    reg_main_page.registration("Sergei", CreatingData.get_login(data), CreatingData.get_password(data))
    reg_main_page.check_len_form_after_registration()
    assert True


#регистрация с невалидным паролем
def test_negative_registration_error_true(browser):
    reg_main_page = RegistrationHelper(browser)
    data = CreatingData()
    reg_main_page.go_to_site()
    reg_main_page.click_on_the_cabinet_button()
    reg_main_page.negative_registration("Sergei", CreatingData.get_login(data), CreatingData.get_password_false(data))
    reg_main_page.check_error_message()
    assert True



