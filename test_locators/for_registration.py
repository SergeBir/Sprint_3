from selenium import webdriver
from selenium.webdriver.common.by import By
import random

#Список символов и цифр для генерации логина и пароля
LIST_FOR_LOGIN = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                  'w', 'x', 'y', 'z', 1, 2, 3, 4, 5, 6, 7, 8, 9]


class TestLocators:

    """Создали класс, в котором будут храниться все локаторы главной страницы, необходимые для проверки"""
    PERSONAL_CABINET_BUTTON = By.XPATH, './/a[@href="/account"]'  # кнопка Личный Кабинет
    AUTHORIZATION_BUTTON = By.XPATH, './/a[@href = "/register"]'  # кнопка регистрации
    NAME_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][1]//input"  # строка имя
    EMAIL_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][2]//input"  # строла email
    PASSWORD_LINE = By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6'][3]//input"  # строка пароль
    BUTTON_REG = By.XPATH, './/button[text()="Зарегистрироваться"]' #Кнопка зарегистрироваться
    FORM = By.XPATH, './/form[@class="Auth_form__3qKeq mb-20"]' # форма авторизации

    """Метод для генерации пароля"""
    def get_password(self):
        password_list = []
        for _ in range(10):
            password_list.append(str(random.choice(LIST_FOR_LOGIN)))
        password = "".join(password_list)
        return password

    """Метод для генерации логина"""
    def get_login(self):
        symbols_count = random.randint(3,9)
        first_part_list = []
        for _ in range(symbols_count):
            first_part_list.append(str(random.choice(LIST_FOR_LOGIN)))
        first_part = ''.join(first_part_list)
        return f"{first_part}@ya.ru"







