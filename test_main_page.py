from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page = MainPage(browser, link)
#     # открываем страницу
#     page.open()
#     # выполняем метод страницы - переходим на страницу логина
#     page.go_to_login_page()
#     # инициализируем Page Object логина
#     page_login = LoginPage(browser, browser.current_url)
#     # проверяем что на странице отображаются элементы
#     page_login.should_be_login_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = MainPage(browser, link)
    # открываем страницу
    page.open()
    page.go_to_basket_page()
    page_basket = BasketPage(browser, browser.current_url)
    # page_basket.should_be_empty_card_message()
    page_basket.test_guest_cant_see_product_in_basket_opened_from_product_page()


# pytest -v --tb=line --language=en test_main_page.py