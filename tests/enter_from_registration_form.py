from selenium import webdriver
from locators.for_enter import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""В данном кейсе проверяем вход из раздела Регистрация"""


def test_check_enter_to_account_from_registration_form_true():

    driver = webdriver.Chrome(executable_path='/Users/sergeibiryukov/yandex/Sprint_3/chromedriver')
    driver.get('https://stellarburgers.nomoreparties.site')#переходим по ссылке
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        TestLocators.PERSONAL_CABINET_BUTTON))#ожидаем появление элемента
    driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()#нажимаем по кнопке кабинета
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()#ищем элемент кнопки Зарегистрироваться
    driver.find_element(*TestLocators.ENTER_FROM_REGISTRATION_BUTTON).click()  # нажимаем по кнопке Войти
    driver.find_element(*TestLocators.EMAIL_LINE).send_keys('sergamer@ya.ru')  # вводим логин
    driver.find_element(*TestLocators.PASSWORD_LINE).send_keys('1234567')  # вводим пароль
    driver.find_element(*TestLocators.ENTER_BUTTON).click()  # нажимаем на кнопку входа
    driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()  # нажимаем на кнопку Личного кабинета
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        TestLocators.PERSONAL_DATA_TEXT))  # ожидаем отображение элементы
    message = driver.find_element(*TestLocators.PERSONAL_DATA_TEXT)  # находим элемент с сообщением
    assert message.text == "В этом разделе вы можете изменить свои персональные данные"  # проверяем данные с текстом

    driver.quit()