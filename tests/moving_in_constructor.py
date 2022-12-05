from selenium import webdriver
from locators.for_enter import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""В данном кейсе проверяем вход из Личного Кабинета в конструктор и перемещение между разделами"""


def test_check_enter_to_constructor_from_cabinet_true():
    driver = webdriver.Chrome(executable_path='/Users/sergeibiryukov/yandex/Sprint_3/chromedriver')
    driver.get('https://stellarburgers.nomoreparties.site')  # переходим по ссылке
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        TestLocators.PERSONAL_CABINET_BUTTON))#ожидаем появление элемента
    driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()  # нажимаем по кнопке личный кабинет
    driver.find_element(*TestLocators.EMAIL_LINE).send_keys('sergamer@ya.ru')# вводим логин
    driver.find_element(*TestLocators.PASSWORD_LINE).send_keys('1234567')# вводим пароль
    driver.find_element(*TestLocators.ENTER_BUTTON).click()# нажимаем на кнопку входа
    driver.find_element(*TestLocators.PERSONAL_CABINET_BUTTON).click()  # нажимаем на кнопку Личного кабинета
    driver.find_element(*TestLocators.STELLAR_BURGER_ELEMENT).click() # переходим в конструктор по клику на текст
    sauce = driver.find_element(*TestLocators.DISPLAY_BUTTON_SAUCE) #находим конструкторе кнопку раздел Соусы
    sauce.click()#нажимаем в конструкторе кнопку раздел Соусы
    bread = driver.find_element(*TestLocators.DISPLAY_BUTTON_BREAD) #находим в конструкторе кнопку раздел Булки
    bread.click()#нажимаем в конструкторе кнопку раздел Булки
    toppings = driver.find_element(*TestLocators.DISPLAY_BUTTON_TOPPINGS) #находим в конструкторе кнопку раздел Начинки
    toppings.click()#нажимаем в конструкторе кнопку раздел Начинки

    assert (sauce.text == "Соусы" and bread.text == "Булки" and toppings.text == "Начинки")

    driver.quit()

