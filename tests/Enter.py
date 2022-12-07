from locators.ForEnter import EnterHelper
from locators.ForEnter import EnterCheckLocators
import time


"""Тесты на проверку авторизации в системе с разными точками входа"""


def test_check_enter_to_personal_cabinet_true(browser):
    enter_main_page = EnterHelper(browser)
    locator = EnterCheckLocators
    enter_main_page.go_to_site()
    enter_main_page.click_on_the_button(locator.PERSONAL_CABINET_BUTTON)
    enter_main_page.enter_to_personal_cabinet('sergamer@ya.ru', '1234567')
    enter_main_page.click_on_the_button(locator.PERSONAL_CABINET_BUTTON)
    enter_main_page.check_text_in_personal_cabinet()
    assert True


def test_exit_from_personal_cabinet_true(browser):
    enter_main_page = EnterHelper(browser)
    locator = EnterCheckLocators
    enter_main_page.go_to_site()
    enter_main_page.click_on_the_button(locator.PERSONAL_CABINET_BUTTON)
    enter_main_page.enter_to_personal_cabinet('sergamer@ya.ru', '1234567')
    enter_main_page.click_on_the_button(locator.PERSONAL_CABINET_BUTTON)
    enter_main_page.exit_from_personal_cabinet()
    enter_main_page.check_text_in_enter_page()
    assert True


def test_check_enter_to_account_true(browser):
    enter_main_page = EnterHelper(browser)
    locator = EnterCheckLocators
    enter_main_page.go_to_site()
    enter_main_page.click_on_the_button(locator.ENTER_TO_ACCOUNT_BUTTON)
    enter_main_page.enter_to_account('sergamer@ya.ru', '1234567')
    enter_main_page.click_on_the_button(locator.PERSONAL_CABINET_BUTTON)
    enter_main_page.check_text_in_personal_cabinet()
    assert True


def test_check_enter_from_registration_form_true(browser):
    enter_main_page = EnterHelper(browser)
    locator = EnterCheckLocators
    enter_main_page.go_to_site()
    enter_main_page.click_on_the_button(locator.PERSONAL_CABINET_BUTTON)
    enter_main_page.enter_from_registration_form()
    enter_main_page.enter_to_personal_cabinet('sergamer@ya.ru', '1234567')
    enter_main_page.click_on_the_button(locator.PERSONAL_CABINET_BUTTON)
    enter_main_page.check_text_in_personal_cabinet()
    assert True


def test_check_enter_from_recovering_password_true(browser):
    enter_main_page = EnterHelper(browser)
    locator = EnterCheckLocators
    enter_main_page.go_to_site()
    enter_main_page.click_on_the_button(locator.PERSONAL_CABINET_BUTTON)
    enter_main_page.enter_from_forgotten_password_form()
    enter_main_page.enter_to_personal_cabinet('sergamer@ya.ru', '1234567')
    enter_main_page.click_on_the_button(locator.PERSONAL_CABINET_BUTTON)
    enter_main_page.check_text_in_personal_cabinet()
    assert True
