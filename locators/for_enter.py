from selenium.webdriver.common.by import By


class TestLocators:
    """Создали класс, в котором будут храниться все локаторы, необходимые для проверки входа"""
    ENTER_TO_ACCOUNT_BUTTON = By.XPATH, './/button[text()="Войти в аккаунт"]' #кнопка Войти в аккаунт
    PERSONAL_CABINET_BUTTON = By.XPATH, './/a[@href="/account"]' #кнопка Личный Кабинет
    EMAIL_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][1]//input"  # строла email
    PASSWORD_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][2]//input"  # строка пароль
    ENTER_BUTTON = By.XPATH, './/button[text()="Войти"]'  # кнопка Войти
    PERSONAL_DATA_TEXT = By.XPATH, '//p[@class="Account_text__fZAIn text text_type_main-default"]' # текст в личном кабинете
    RECOVER_PASSWORD_BUTTON = By.XPATH, "//a[contains(text(),'Восстановить пароль')]" # Восстановление пароля
    REGISTRATION_BUTTON = By.XPATH, './/a[@href = "/register"]'  # кнопка регистрации
    ENTER_FROM_RECOVERING_BUTTON = By.XPATH, './/a[@class="Auth_link__1fOlj"]'# Кнопка Войти из восстановления пароля
    ENTER_FROM_REGISTRATION_BUTTON = By.XPATH, './/a[@class="Auth_link__1fOlj"]'  # Кнопка Войти из восстановления пароля
    STELLAR_BURGER_ELEMENT = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a//*[name()='svg']" # Текст кнопка для перехода в конструктор
    CONSTRUCT_BURGER_TEXT = By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]' # Текст в конструкторе
    EXIT_BUTTON = By.XPATH, '//button[@type="button" and text()="Выход"]'# кнопка Выход в кабинете
    ENTER_TEXT = By.XPATH, './/h2[text()="Вход"]' #Надпись Вход
    DISPLAY_BUTTON_BREAD = By.XPATH, "//span[contains(text(),'Булки')]"# кнопка Булки в конструкторе
    DISPLAY_BUTTON_SAUCE = By.XPATH, "//span[contains(text(),'Соусы')]"# кнопка Соусы в конструкторе
    DISPLAY_BUTTON_TOPPINGS = By.XPATH, "//span[contains(text(),'Начинки')]"# кнопка Начинки в конструкторе
