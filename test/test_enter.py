from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.for_enter import TestEnterCheckLocators


#проверка входа в личный кабинет
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


#проверка входа в аккаунт
def test_enter_to_account_true(browser):
    reg = TestEnterCheckLocators(browser)
    reg.go_to_site()
    reg.click_to_account_button()
    reg.send_data_to_email_field("sergamer@ya.ru")
    reg.send_data_to_password_field("1234567")
    reg.click_to_enter_button()
    WebDriverWait(browser, 3).until(
        expected_conditions.presence_of_element_located(TestEnterCheckLocators.MAKE_ORDER))
    button = reg.find_text(TestEnterCheckLocators.MAKE_ORDER)
    assert button.text == "Оформить заказ"


#проверка выхода из личного кабинета
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


#проверка входа из формы регистрации
def test_enter_from_registration_true(browser):
    reg = TestEnterCheckLocators(browser)
    reg.go_to_site()
    reg.click_to_personal_cabinet_button()
    reg.click_to_registration_button()
    WebDriverWait(browser, 3).until(
         expected_conditions.visibility_of_element_located(TestEnterCheckLocators.ENTER_FROM_REGISTRATION_BUTTON))
    reg.click_to_enter_from_registration()
    reg.send_data_to_email_field("sergamer@ya.ru")
    reg.send_data_to_password_field("1234567")
    reg.click_to_enter_button()
    WebDriverWait(browser, 3).until(
        expected_conditions.presence_of_element_located(TestEnterCheckLocators.MAKE_ORDER))
    button = reg.find_text(TestEnterCheckLocators.MAKE_ORDER)
    assert button.text == "Оформить заказ"


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


#проверка входа в конструктор
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


#проверка перемещения из конструктора
def test_moving_in_constructor_true(browser):
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
    reg.moving_in_constructor()
    sauce = reg.find_text(TestEnterCheckLocators.DISPLAY_BUTTON_SAUCE)
    bread = reg.find_text(TestEnterCheckLocators.DISPLAY_BUTTON_BREAD)
    toppings = reg.find_text(TestEnterCheckLocators.DISPLAY_BUTTON_TOPPINGS)
    assert (sauce.text == "Соусы" and bread.text == "Булки" and toppings.text == "Начинки")


