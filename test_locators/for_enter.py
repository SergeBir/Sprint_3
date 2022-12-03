from selenium.webdriver.common.by import By


class TestLocators:
    """Создали класс, в котором будут храниться все локаторы главной страницы, необходимые для проверки"""
    PERSONAL_CABINET_BUTTON = By.XPATH, './/a[@href="/account"]' #кнопка Личный Кабинет

    EMAIL_LINE = By.XPATH, './/input[@type="text" and @name = "name"]' # строка email
    PASSWORD_LINE = By.XPATH, './/input[@type="password"]' # строка password

    ENTER_BUTTON = By.XPATH, './/button[text()="Войти"]'  # кнопка Войти