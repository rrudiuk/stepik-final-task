from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def should_be_promo_newyear_url(self):
        # реализуйте проверку на корректный url адрес
        promo_parameter = "promo=newYear"
        assert promo_parameter in self.browser.current_url, "Incorrect url"

    def should_add_correct_book(self):
        expected_result = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        actual_result = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

        assert actual_result == expected_result, "Book title in the message doesn't correspond to title on the page"

    def price_in_basket_should_be_same(self):
        expected_result = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        actual_result = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

        assert expected_result in actual_result, "Price in basket doesn't correspond to book price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"

