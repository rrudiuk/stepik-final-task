from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
	def should_be_empty_card_message(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
			"Empty card message is not presented, but should be"

	def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_CONTAINER), \
			"There is a shopping item in the basket, but shouldn't be one"