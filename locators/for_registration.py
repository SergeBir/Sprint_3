from pages.base_app import BasePage
from selenium.webdriver.common.by import By


class TestRegistrationCheckLocators(BasePage):
    """Создали класс, в котором будут храниться все локаторы , необходимые для проверки регистрации"""
    PERSONAL_CABINET_BUTTON = By.XPATH, './/a[@href="/account"]'  # кнопка Личный Кабинет
    REGISTRATION_BUTTON = By.XPATH, './/a[@href = "/register"]'  # кнопка регистрации
    NAME_LINE = By.XPATH, '//fieldset[contains(@class, "Auth_fieldset")]/div/div/label[text()="Имя"]/following-sibling::node()'  # строка имя
    EMAIL_LINE = By.XPATH, '//fieldset[contains(@class, "Auth_fieldset")]/div/div/label[text()="Email"]/following-sibling::node()'  # строла email
    PASSWORD_LINE = By.XPATH, "//input[@name='Пароль']"  # строка пароль
    BUTTON_REG = By.XPATH, './/button[text()="Зарегистрироваться"]'  # Кнопка зарегистрироваться
    ENTER_BUTTON = By.XPATH, './/button[text()="Войти"]'  # кнопка Войти
    ENTER_TEXT = By.XPATH, './/h2[text()="Вход"]'  # Надпись Вход
    ERROR_MESSAGE = By.XPATH, "//p[@class='input__error text_type_main-default']" # Ошибка пароля

    #нажать на кнопку Личного кабинета
    def click_to_personal_cabinet_button(self):
        p_button = self.find_element(TestRegistrationCheckLocators.PERSONAL_CABINET_BUTTON)
        self.driver.execute_script("arguments[0].click();", p_button)

    #нажать на кнопку Регистрация
    def click_to_reg_button(self):
        r_button = self.find_element(TestRegistrationCheckLocators.REGISTRATION_BUTTON)
        self.driver.execute_script("arguments[0].click();", r_button)

    #заполнить поле имя
    def send_data_to_name_field(self, name):
        name_field = self.find_element(TestRegistrationCheckLocators.NAME_LINE)
        name_field.send_keys(name)

    #заполнить поле email
    def send_data_to_email_field(self, email):
        email_field = self.find_element(TestRegistrationCheckLocators.EMAIL_LINE)
        email_field.send_keys(email)

    #заполнить поле пароль
    def send_data_to_password_field(self, password):
        password_field = self.find_element(TestRegistrationCheckLocators.PASSWORD_LINE)
        password_field.send_keys(password)

    #нажать на кнопку Зарегистрироваться
    def click_to_registration_button(self):
        button = self.find_element(TestRegistrationCheckLocators.BUTTON_REG)
        button.click()

    #найти текст
    def find_text(self, locator):
        line_text = self.find_element(locator, time=3)
        return line_text
