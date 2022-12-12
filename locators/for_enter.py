from pages.base_app import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""В этом классе будут описаны все локаторы"""


class TestEnterCheckLocators(BasePage):
    """Создали класс, в котором будут храниться все локаторы, необходимые для проверки входа"""
    ENTER_TO_ACCOUNT_BUTTON = By.XPATH, './/button[text()="Войти в аккаунт"]' #кнопка Войти в аккаунт
    PERSONAL_CABINET_BUTTON = By.XPATH, './/a[@href="/account"]' #кнопка Личный Кабинет
    CONTAINER = By.XPATH, './/main[@class="App_componentContainer__2JC2W"]' #контейнер Личного кабинета
    EMAIL_LINE = By.XPATH, '//fieldset[contains(@class, "Auth_fieldset")]/div/div/label[text()="Email"]/following-sibling::node()'  # строла email
    PASSWORD_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][2]//input"  # строка пароль
    ENTER_BUTTON = By.XPATH, './/button[text()="Войти"]'  # кнопка Войти
    MAKE_ORDER = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']" # Оформить заказ
    PROFILE_BUTTON = By.XPATH, './/a[@href="/account/profile"]'# Кнопка Профиль
    PERSONAL_DATA_TEXT = By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']" # текст в личном кабинете
    RECOVER_PASSWORD_BUTTON = By.XPATH, "//a[contains(text(),'Восстановить пароль')]" # Восстановление пароля
    REGISTRATION_BUTTON = By.XPATH, './/a[@href = "/register"]'  # кнопка регистрации
    ENTER_FROM_RECOVERING_BUTTON = By.XPATH, "//a[@class='Auth_link__1fOlj']"# Кнопка Войти из восстановления пароля
    ENTER_FROM_REGISTRATION_BUTTON = By.XPATH, './/a[@class="Auth_link__1fOlj"]'  # Кнопка Войти из регистрации
    STELLAR_BURGER_ELEMENT = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a//*[name()='svg']" # Текст кнопка для перехода в конструктор
    CONSTRUCT_BURGER_TEXT = By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]' # Текст в конструкторе
    EXIT_BUTTON = By.XPATH, '//button[@type="button" and text()="Выход"]'# кнопка Выход в кабинете
    ENTER_TEXT = By.XPATH, './/h2[text()="Вход"]' #Надпись Вход
    DISPLAY_BUTTON_BREAD = By.XPATH, "//span[contains(text(),'Булки')]"# кнопка Булки в конструкторе
    DISPLAY_BUTTON_SAUCE = By.XPATH, "//span[contains(text(),'Соусы')]"# кнопка Соусы в конструкторе
    DISPLAY_BUTTON_TOPPINGS = By.XPATH, "//span[contains(text(),'Начинки')]"# кнопка Начинки в конструкторе

    #нажатия на кнопку Личного кабинета
    def click_to_personal_cabinet_button(self):
        WebDriverWait(self, 3)
        p_button = self.find_element(TestEnterCheckLocators.PERSONAL_CABINET_BUTTON, time=10)
        p_button.click()

    # нажатие на кнопку входа в аккаунт
    def click_to_account_button(self):
        WebDriverWait(self, 3)
        a_button = self.find_element(TestEnterCheckLocators.ENTER_TO_ACCOUNT_BUTTON, time=10)
        a_button.click()

    # заполнение поля email
    def send_data_to_email_field(self, email):
        WebDriverWait(self, 3)
        email_field = self.find_element(TestEnterCheckLocators.EMAIL_LINE, time=10)
        email_field.send_keys(email)

    # заполнение поля пароль
    def send_data_to_password_field(self, password):
        password_field = self.find_element(TestEnterCheckLocators.PASSWORD_LINE)
        password_field.send_keys(password)

    # нажатие на кнопку Вход
    def click_to_enter_button(self):
        e_button = self.find_element(TestEnterCheckLocators.ENTER_BUTTON)
        self.driver.execute_script("arguments[0].click();", e_button)

    #нажатие на кнопку Профиля
    def click_to_profile_button(self):
        profile_button = self.find_element(TestEnterCheckLocators.PROFILE_BUTTON, time=10)
        profile_button.click()

    #найти надпись
    def find_text(self, locator):
        WebDriverWait(self, 3)
        line_text = self.find_element(locator, time=10)
        return line_text

    #нажать на кнопку Выход
    def click_to_exit_button(self):
        WebDriverWait(self, 3)
        e_button = self.find_element(TestEnterCheckLocators.EXIT_BUTTON, time=10)
        e_button.click()

    #нажать на кнопку Регистрация
    def click_to_registration_button(self):
        WebDriverWait(self, 3)
        r_button = self.find_element(TestEnterCheckLocators.REGISTRATION_BUTTON, time=10)
        r_button.click()

    #нажать на кнопку Войти из регистрации
    def click_to_enter_from_registration(self):
        WebDriverWait(self, 3)
        ent_button = self.find_element(TestEnterCheckLocators.ENTER_FROM_REGISTRATION_BUTTON, time=10)
        ent_button.click()

    #нажать на кнопку Восстановления пароля
    def click_to_recovering_password(self):
        WebDriverWait(self, 3)
        rec_button = self.find_element(TestEnterCheckLocators.RECOVER_PASSWORD_BUTTON, time=10)
        rec_button.click()

    #нажать на кнопку входа из восстановления пароля
    def click_to_enter_from_recover_password(self):
        WebDriverWait(self, 3)
        ent_rec_button = self.find_element(TestEnterCheckLocators.ENTER_FROM_RECOVERING_BUTTON,time=10)
        ent_rec_button.click()

    #нажать на форму конструктора
    def click_to_constructor_form(self):
        WebDriverWait(self, 3)
        construct = self.find_element(TestEnterCheckLocators.STELLAR_BURGER_ELEMENT,time=10)
        construct.click()

    #перемещение по конструктору
    def moving_in_constructor(self):
        WebDriverWait(self, 3)
        sauce = self.find_element(TestEnterCheckLocators.DISPLAY_BUTTON_SAUCE,time=10)
        sauce.click()
        bread = self.find_element(TestEnterCheckLocators.DISPLAY_BUTTON_BREAD,time=10)
        bread.click()
        toppings = self.find_element(TestEnterCheckLocators.DISPLAY_BUTTON_TOPPINGS,time=10)
        toppings.click()
