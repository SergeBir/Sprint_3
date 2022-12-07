from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By

"""В этом классе будут описаны все локаторы"""


class EnterCheckLocators:
    """Создали класс, в котором будут храниться все локаторы, необходимые для проверки входа"""
    ENTER_TO_ACCOUNT_BUTTON = By.XPATH, './/button[text()="Войти в аккаунт"]' #кнопка Войти в аккаунт
    PERSONAL_CABINET_BUTTON = By.XPATH, './/a[@href="/account"]' #кнопка Личный Кабинет
    EMAIL_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][1]//input"  # строла email
    PASSWORD_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][2]//input"  # строка пароль
    ENTER_BUTTON = By.XPATH, './/button[text()="Войти"]'  # кнопка Войти
    PROFILE_BUTTON = By.XPATH, './/a[@href="/account/profile"]'# Кнопка Профиль
    PERSONAL_DATA_TEXT = By.XPATH, '//p[@class="Account_text__fZAIn text text_type_main-default"]' # текст в личном кабинете
    RECOVER_PASSWORD_BUTTON = By.XPATH, "//a[contains(text(),'Восстановить пароль')]" # Восстановление пароля
    REGISTRATION_BUTTON = By.XPATH, './/a[@href = "/register"]'  # кнопка регистрации
    ENTER_FROM_RECOVERING_BUTTON = By.XPATH, './/a[@class="Auth_link__1fOlj"]'# Кнопка Войти из восстановления пароля
    ENTER_FROM_REGISTRATION_BUTTON = By.XPATH, './/a[@class="Auth_link__1fOlj"]'  # Кнопка Войти из регистрации
    STELLAR_BURGER_ELEMENT = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a//*[name()='svg']" # Текст кнопка для перехода в конструктор
    CONSTRUCT_BURGER_TEXT = By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]' # Текст в конструкторе
    EXIT_BUTTON = By.XPATH, '//button[@type="button" and text()="Выход"]'# кнопка Выход в кабинете
    ENTER_TEXT = By.XPATH, './/h2[text()="Вход"]' #Надпись Вход
    DISPLAY_BUTTON_BREAD = By.XPATH, "//span[contains(text(),'Булки')]"# кнопка Булки в конструкторе
    DISPLAY_BUTTON_SAUCE = By.XPATH, "//span[contains(text(),'Соусы')]"# кнопка Соусы в конструкторе
    DISPLAY_BUTTON_TOPPINGS = By.XPATH, "//span[contains(text(),'Начинки')]"# кнопка Начинки в конструкторе


"""В этом классе будут описаны все методы для управления тестами"""


class EnterHelper(BasePage):
    #нажатие на любую кнопку
    def click_on_the_button(self, button):
        return self.find_element(button, time=10).click()

    # вход в личный кабинет
    def enter_to_personal_cabinet(self, name, password):
        name_field = self.find_element(EnterCheckLocators.EMAIL_LINE)
        name_field.send_keys(name)
        password_field = self.find_element(EnterCheckLocators.PASSWORD_LINE)
        password_field.send_keys(password)
        enter_button = self.find_element(EnterCheckLocators.ENTER_BUTTON)
        enter_button.click()

    # выход из личного кабинета
    def exit_from_personal_cabinet(self):
        exit_button = self.find_element(EnterCheckLocators.EXIT_BUTTON)
        exit_button.click()

    # проверка текста в личном кабинете
    def check_text_in_personal_cabinet(self):
        profile_button = self.find_element(EnterCheckLocators.PROFILE_BUTTON, time=10)
        profile_button.click()
        message = self.find_element(EnterCheckLocators.PERSONAL_DATA_TEXT, time=10)
        assert message.text == "В этом разделе вы можете изменить свои персональные данные"

    # проверка текста на вкладке входа
    def check_text_in_enter_page(self):
        self.find_element(EnterCheckLocators.ENTER_BUTTON, time=10)
        text_enter = self.find_element(EnterCheckLocators.ENTER_TEXT)
        assert text_enter.text == "Вход"

    # вход в аккаунт
    def enter_to_account(self, name, password):
        name_field = self.find_element(EnterCheckLocators.EMAIL_LINE)
        name_field.send_keys(name)
        password_field = self.find_element(EnterCheckLocators.PASSWORD_LINE)
        password_field.send_keys(password)
        enter_button = self.find_element(EnterCheckLocators.ENTER_BUTTON)
        enter_button.click()

    # вход в личный кабинет из формы регистрации
    def enter_from_registration_form(self):
        registration_button = self.find_element(EnterCheckLocators.REGISTRATION_BUTTON)
        registration_button.click()
        reg_enter_button = self.find_element(EnterCheckLocators.ENTER_FROM_REGISTRATION_BUTTON)
        reg_enter_button.click()

    # вход в личный кабинет из формы восстановления пароля
    def enter_from_forgotten_password_form(self):
        forgotten_password = self.find_element(EnterCheckLocators.RECOVER_PASSWORD_BUTTON)
        forgotten_password.click()
        recover_enter_button = self.find_element(EnterCheckLocators.ENTER_FROM_RECOVERING_BUTTON)
        recover_enter_button.click()

    # вход в конструктор из личного кабинета
    def enter_from_cabinet_to_constructor(self):
        burger_element = self.find_element(EnterCheckLocators.STELLAR_BURGER_ELEMENT)
        burger_element.click()

    # проверка текста в конструкторе
    def check_text_in_constructor(self):
        burger_text = self.find_element(EnterCheckLocators.CONSTRUCT_BURGER_TEXT, time=10)
        assert burger_text.text == "Соберите бургер"

    # перемещение по конструктору
    def moving_in_constructor(self):
        sauce = self.find_element(EnterCheckLocators.DISPLAY_BUTTON_SAUCE)
        sauce.click()
        bread = self.find_element(EnterCheckLocators.DISPLAY_BUTTON_BREAD)
        bread.click()
        toppings = self.find_element(EnterCheckLocators.DISPLAY_BUTTON_TOPPINGS)
        toppings.click()
        assert (sauce.text == "Соусы" and bread.text == "Булки" and toppings.text == "Начинки")
