from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By

"""В этом классе будут описаны все локаторы"""


class RegistrationCheckLocators:
    """Создали класс, в котором будут храниться все локаторы , необходимые для проверки регистрации"""
    PERSONAL_CABINET_BUTTON = By.XPATH, './/a[@href="/account"]'  # кнопка Личный Кабинет
    REGISTRATION_BUTTON = By.XPATH, './/a[@href = "/register"]'  # кнопка регистрации
    NAME_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][1]//input"  # строка имя
    EMAIL_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][2]//input"  # строла email
    PASSWORD_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][3]//input"  # строка пароль
    BUTTON_REG = By.XPATH, './/button[text()="Зарегистрироваться"]'  # Кнопка зарегистрироваться
    FORM = By.XPATH, './/form[@class="Auth_form__3qKeq mb-20"]'  # форма авторизации
    ERROR_MESSAGE = By.XPATH, './/p[@class="input__error text_type_main-default"]'  # сообщение об ошибке(некорректный пароль)

"""В этом классе будут описаны все методы для управления тестами"""


class RegistrationHelper(BasePage):
    # нажатие на кнопку Личного кабинета
    def click_on_the_cabinet_button(self):
        return self.find_element(RegistrationCheckLocators.PERSONAL_CABINET_BUTTON, time=3).click()

    # регистрация
    def registration(self, name, email, password):
        reg_button = self.find_element(RegistrationCheckLocators.REGISTRATION_BUTTON)
        reg_button.click()
        name_field = self.find_element(RegistrationCheckLocators.NAME_LINE)
        name_field.send_keys(name)
        email_field = self.find_element(RegistrationCheckLocators.EMAIL_LINE)
        email_field.send_keys(email)
        password_field = self.find_element(RegistrationCheckLocators.PASSWORD_LINE)
        password_field.send_keys(password)
        registration_button = self.find_element(RegistrationCheckLocators.BUTTON_REG)
        registration_button.click()

    # проверка количества элементов после регистрации
    def check_len_form_after_registration(self):
        return self.find_element(RegistrationCheckLocators.FORM) == 2

    # негативная регистрация
    def negative_registration(self, name, email, falsePassword):
        reg_button = self.find_element(RegistrationCheckLocators.REGISTRATION_BUTTON)
        reg_button.click()
        name_field = self.find_element(RegistrationCheckLocators.NAME_LINE)
        name_field.send_keys(name)
        email_field = self.find_element(RegistrationCheckLocators.EMAIL_LINE)
        email_field.send_keys(email)
        password_field = self.find_element(RegistrationCheckLocators.PASSWORD_LINE)
        password_field.send_keys(falsePassword)
        registration_button = self.find_element(RegistrationCheckLocators.BUTTON_REG)
        registration_button.click()

    # проверка текста ошибки после регистрации с невалидным паролем
    def check_error_message(self):
        error_message_form = self.find_element(RegistrationCheckLocators.ERROR_MESSAGE, time=3)
        assert error_message_form.text == "Некорректный пароль"
