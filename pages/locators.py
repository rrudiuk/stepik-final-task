from selenium.webdriver.common.by import By

class BasePageLocators():
    GO_TO_BASKET = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p:first-child")
    BASKET_ITEMS_CONTAINER = (By.CSS_SELECTOR, "#basket_formset")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRY_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRY_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRY_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRY_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRY_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-primary")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini")
