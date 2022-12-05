from selenium import webdriver
from locators.for_registration import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from methods.methods_for_tests import Methods


def test_check_positive_registration_succes():
    method = Methods() #создаем объект класса

    driver = webdriver.Chrome(executable_path='/Users/sergeibiryukov/yandex/Sprint_3/chromedriver')
    driver.get('https://stellarburgers.nomoreparties.site')#переходим по ссылке
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        TestLocators.PERSONAL_CABINET_BUTTON))#ожидаем появление элемента
    driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()#нажимаем по кнопке кабинета
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()#ищем элемент кнопки Зарегистрироваться
    driver.find_element(*TestLocators.NAME_LINE).send_keys("Sergei")#вводим имя
    login = Methods.get_login(method)#передаем в переменную метод генерации Логина(email)
    print(f"Login {login}")#проверяем, что метод сработал, напечатав логин
    driver.find_element(*TestLocators.EMAIL_LINE).send_keys(login)#вводим в строку email наши данные
    password = Methods.get_password(method)#передаем в переменную метод генерации Пароля
    print(f"Password {password}")#проверяем, что метод сработал, напечатав пароль
    driver.find_element(*TestLocators.PASSWORD_LINE).send_keys(password)#вводим в строку пароля наши данные
    driver.find_element(*TestLocators.BUTTON_REG).click()#находим кнопку регистрации
    assert len(TestLocators.FORM) == 2#проверяем элемент

    driver.quit()#Закрываем
