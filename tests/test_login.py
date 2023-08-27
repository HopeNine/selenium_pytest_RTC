from time import sleep
from pages.main_page import MainPage

"""Позитивные тесты"""


def test_auth_by_mail_with_correct_data(driver):
    main_page = MainPage(driver)
    main_page.load()
    main_page.auth_by_mail('npdevyatka@gmail.com',
                           '&L!#32_#%T.2ubH')  # выполняется ввод корректного логина и корректного пароля
    assert main_page.check_user_page_url()  # на загруженной странице появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_phone_with_correct_data(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_phone('89224706660',
                            '&L!#32_#%T.2ubH')  # выполняется ввод корректного логина и корректного пароля
    assert main_page.check_user_page_url()  # на загруженной странице появляется данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_login_with_correct_data(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_login('npdevyatka@gmail.com',
                            '&L!#32_#%T.2ubH')  # выполняется ввод корректного логина и корректного пароля
    assert main_page.check_user_page_url()  # на загруженной странице появляется данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_ls_with_correct_data(driver):  # нет возможности проверить - нет ЛС в Компании
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_ls('5646856511685463',
                         '&L!#32_#%T.2ubH')  # выполняется ввод корректного логина и корректного пароля
    assert main_page.check_user_page_url()  # на загруженной странице появляются данные о пользователе

    sleep(2)
    driver.quit()


"""Негативные тесты"""


def test_auth_by_mail_with_uncorrect_login_1(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_mail('45344123456@',
                           '&L!#32_#%T.2ubH')  # выполняется ввод некорректного логина и корректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_mail_with_uncorrect_login_2(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_mail('SDfd', '&L!#32_#%T.2ubH')  # выполняется ввод некорректного логина и корректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_mail_with_uncorrect_login_3(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_mail('nlklnmn@fghj',
                           '&L!#32_#%T.2ubH')  # выполняется ввод некорректного логина и корректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_mail_with_uncorrect_password(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_mail('npdevyatka@gmail.com',
                           'TYрfhжjkl8$%')  # выполняется ввод корректного логина и некорректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_mail_with_uncorrect_data(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_mail('4856rty@yut.bj',
                           'tyuiolk%%')  # выполняется ввод некорректного логина и некорректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_phone_with_uncorrect_login_1(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_phone('+7345285956D',
                            '&L!#32_#%T.2ubH')  # выполняется ввод некорректного логина и корректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_phone_with_uncorrect_login_2(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_phone('+734528595684',
                            '&L!#32_#%T.2ubH')  # выполняется ввод некорректного логина и корректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_phone_with_uncorrect_login_3(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_phone('+73452684',
                            '&L!#32_#%T.2ubH')  # выполняется ввод некорректного логина и корректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_phone_with_uncorrect_password(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_phone('npdevyatka@gmail.com',
                            'Ztyu')  # выполняется ввод корректного логина и некорректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_phone_with_uncorrect_data(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_phone('4856rty@yut.bj',
                            'tyuiolk%%')  # выполняется ввод некорректного логина и некорректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_login_with_uncorrect_login_1(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_login('nlklnmn@fghj',
                            '&L!#32_#%T.2ubH')  # выполняется ввод некорректного логина и корректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_login_with_uncorrect_login_2(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_login('SDfd', '&L!#32_#%T.2ubH')  # выполняется ввод некорректного логина и корректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_login_with_uncorrect_login_3(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_login('45344123456@',
                            '&L!#32_#%T.2ubH')  # выполняется ввод некорректного логина и корректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_login_with_uncorrect_password(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_login('npdevyatka@gmail.com',
                            'TYрfhжjkl8$%')  # выполняется ввод корректного логина и некорректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_login_with_uncorrect_data(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_login('4856rty@yut.bj', 'Ztyu')  # выполняется ввод некорректного логина и некорректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_ls_with_uncorrect_login_1(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_ls('75685125452', '&L!#32_#%T.2ubH')  # выполняется ввод некорректного логина и корректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_ls_with_uncorrect_login_2(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_ls('asdfET45', '&L!#32_#%T.2ubH')  # выполняется ввод некорректного логина и корректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_ls_with_uncorrect_login_3(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_ls('$%^&*%', '&L!#32_#%T.2ubH')  # выполняется ввод некорректного логина и корректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_ls_with_uncorrect_password(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_ls('456789123', '75685125452')  # выполняется ввод корректного логина и некорректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


def test_auth_by_ls_with_uncorrect_data(driver):
    main_page = MainPage(driver)  # создается класс
    main_page.load()  # загружается страница
    main_page.auth_by_ls('4856rty@yut.bj',
                         '75685125452')  # выполняется ввод некорректного логина и некорректного пароля
    assert not main_page.check_user_page_url()  # на загруженной странице не появляются данные о пользователе

    sleep(2)
    driver.quit()


"""для запуска вводим в терминал: pytest test_login.py"""
