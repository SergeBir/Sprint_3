import random

# Список символов и цифр для генерации логина и пароля
LIST_FOR_LOGIN_PASSWORD = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                           'w', 'x', 'y', 'z', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


class CreatingData:

    """Метод для генерации пароля"""
    def get_password(self):
        password_list = []
        for _ in range(10):
            password_list.append(str(random.choice(LIST_FOR_LOGIN_PASSWORD)))
        password = "".join(password_list)
        return password

    """Метод для генерации логина"""
    def get_login(self):
        symbols_count = random.randint(3,9)
        first_part_list = []
        for _ in range(symbols_count):
            first_part_list.append(str(random.choice(LIST_FOR_LOGIN_PASSWORD)))
        first_part = ''.join(first_part_list)
        return f"{first_part}@ya.ru"

    """Метод для генерации некорректного пароля"""
    def get_password_false(self):
        symbols_count = random.randint(1, 3)
        password_list = []
        for _ in range(symbols_count):
            password_list.append(str(random.choice(LIST_FOR_LOGIN_PASSWORD)))
        password = "".join(password_list)
        return password
