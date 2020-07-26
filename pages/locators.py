from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRY_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
	BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
	SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
	BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
	BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini")
