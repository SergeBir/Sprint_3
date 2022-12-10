from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.ForEnter import TestEnterCheckLocators


#проверка входа из формы восстановления пароля
def test_enter_from_forgotten_password_true(browser):
    reg = TestEnterCheckLocators(browser)
    reg.go_to_site()
    reg.click_to_personal_cabinet_button()
    reg.click_to_recovering_password()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located(TestEnterCheckLocators.ENTER_FROM_RECOVERING_BUTTON))
    reg.click_to_enter_from_recover_password()
    reg.send_data_to_email_field("sergamer@ya.ru")
    reg.send_data_to_password_field("1234567")
    reg.click_to_enter_button()
    WebDriverWait(browser, 3).until(
        expected_conditions.presence_of_element_located(TestEnterCheckLocators.MAKE_ORDER))
    button = reg.find_text(TestEnterCheckLocators.MAKE_ORDER)
    assert button.text == "Оформить заказ"
