from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = MainPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод страницы - переходим на страницу логина
    page.go_to_login_page()
    # инициализируем Page Object логина
    page_login = LoginPage(browser, browser.current_url)
    # проверяем что на странице отображаются элементы
    page_login.should_be_login_form()

# pytest -v --tb=line --language=en test_main_page.py