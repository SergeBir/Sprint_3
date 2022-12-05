from selenium.webdriver.common.by import By


class TestLocators:

    """Создали класс, в котором будут храниться все локаторы , необходимые для проверки регистрации"""
    PERSONAL_CABINET_BUTTON = By.XPATH, './/a[@href="/account"]'  # кнопка Личный Кабинет
    REGISTRATION_BUTTON = By.XPATH, './/a[@href = "/register"]'  # кнопка регистрации
    NAME_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][1]//input"  # строка имя
    EMAIL_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][2]//input"  # строла email
    PASSWORD_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][3]//input"  # строка пароль
    BUTTON_REG = By.XPATH, './/button[text()="Зарегистрироваться"]' #Кнопка зарегистрироваться
    FORM = By.XPATH, './/form[@class="Auth_form__3qKeq mb-20"]' # форма авторизации
    ERROR_MESSAGE = By.XPATH, './/p[@class="input__error text_type_main-default"]' # сообщение об ошибке(некорректный пароль)







