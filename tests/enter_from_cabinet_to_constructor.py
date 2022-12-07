from selenium import webdriver
from locators.ForEnter import EnterCheckLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""В данном кейсе проверяем вход из Личного Кабинета в конструктор"""


def test_check_enter_to_constructor_from_cabinet_true():
    driver = webdriver.Chrome(executable_path='/Users/sergeibiryukov/yandex/Sprint_3/chromedriver')
    driver.get('https://stellarburgers.nomoreparties.site')  # переходим по ссылке
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        EnterCheckLocators.PERSONAL_CABINET_BUTTON))#ожидаем появление элемента
    driver.find_element(*EnterCheckLocators.PERSONAL_CABINET_BUTTON).click()  # нажимаем по кнопке личный кабинет
    driver.find_element(*EnterCheckLocators.EMAIL_LINE).send_keys('sergamer@ya.ru')# вводим логин
    driver.find_element(*EnterCheckLocators.PASSWORD_LINE).send_keys('1234567')# вводим пароль
    driver.find_element(*EnterCheckLocators.ENTER_BUTTON).click()# нажимаем на кнопку входа
    driver.find_element(*EnterCheckLocators.PERSONAL_CABINET_BUTTON).click()  # нажимаем на кнопку Личного кабинета
    driver.find_element(*EnterCheckLocators.STELLAR_BURGER_ELEMENT).click() # переходим в конструктор по клику на текст
    constructor_text = driver.find_element(*EnterCheckLocators.CONSTRUCT_BURGER_TEXT) # Находим заголовок на странице конструктора
    assert constructor_text.text == "Соберите бургер"

    driver.quit()
