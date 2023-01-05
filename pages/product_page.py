from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart button is not presented"
    
    def add_product_to_basket(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_names_match(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_add_to_cart__message = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_MESSAGE)
        assert product_add_to_cart__message.text == product_name.text, "The product name did not match the product name in the cart"

    def should_be_prices_match(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_in_cart_price = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_CART_PRICE)
        assert product_price.text == product_in_cart_price.text, "The product price did not match the product price in the cart"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_success_message_is_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"