from pages.main_page import MainPage
from pages.login_page import LoginPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    main = MainPage(browser, link)
    login = LoginPage(browser, link)
    # открываем страницу
    main.open()
    # выполняем метод страницы - переходим на страницу логина
    main.go_to_login_page()
    login.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main = MainPage(browser, link)
    main.open()
    main.should_be_login_link()