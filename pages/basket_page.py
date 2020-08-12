from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_card_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty card message is not presented, but should be"

    def should_be_no_added_to_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_CONTAINER), \
            "There is a shopping item in the basket, but shouldn't be one"
