from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
	# link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
	product_page = ProductPage(browser, link)
	product_page.open()
	product_page.should_be_promo_newyear_url()
	product_page.add_to_basket()
	product_page.solve_quiz_and_get_code()
	product_page.should_add_correct_book()
	product_page.price_in_basket_should_be_same()

# pytest -s -v --tb=line --language=en test_product_page.py