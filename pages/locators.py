from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class RegisterPageLocators():
    EMAIL_FORM = (By.ID, "id_registration-email")
    PASSWORD_FORM = (By.ID, "id_registration-password1")
    REPEAT_PASSWORD_FORM = (By.ID, "id_registration-password2")
    REGISTRAION_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p.price_color")
    PRODUCT_IN_BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//header/div[1]/div/div[2]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
    PRODUCT_IN_BASKET = (By.CLASS_NAME, "basket_summary")


