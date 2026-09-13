from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # 1. Открываем сайт gitflic.ru
    driver.get("https://gitflic.ru/")

    # 2. Устанавливаем cookie пользователя 1
    cookie_user1 = {
        'name': 'user1_session',
        'value': 'token_user_1_value_12345'
    }
    driver.add_cookie(cookie_user1)

    # 3. Обновляем страницу для применения cookie
    driver.refresh()

    # 4. Переходим на страницу профиля пользователя 1
    driver.get("https://gitflic.ru/user/user1")

    # 5. Сохраняем текущий URL
    url_user1 = driver.current_url

    # 6. Разлогиниваемся (очищаем куки)
    driver.delete_all_cookies()

    # 7. Устанавливаем cookie пользователя 2
    driver.get("https://gitflic.ru/")
    cookie_user2 = {
        'name': 'user2_session',
        'value': 'token_user_2_value_67890'
    }
    driver.add_cookie(cookie_user2)

    # 8. Обновляем страницу
    driver.refresh()

    # 9. Переходим на страницу профиля пользователя 2
    driver.get("https://gitflic.ru/user/user2")

    # 10. Сохраняем текущий URL
    url_user2 = driver.current_url

    # 11. Проверяем, что URL профилей
    # первого и второго пользователей различаются
    assert url_user1 != url_user2

    # Завершаем работу браузера
    driver.quit()
