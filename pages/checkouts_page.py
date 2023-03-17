from time import sleep

from constants.homepage_checkout import HomePage
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_decorator


class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HomePage()

    def __scroll_down_page(self, speed=8):
        current_scroll_position, new_height = 2, 2
        while current_scroll_position <= new_height:
            current_scroll_position += speed
            self.driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
            new_height = self.driver.execute_script("return document.body.scrollHeight")

    @wait_until_ok(timeout=5, period=1)
    @log_decorator
    def second_checkout(self, user):
        """Go through checkout"""
        self.click(xpath=self.constants.SHOP_BUTTON_XPATH)
        """Click on Buy now"""
        self.find_element(xpath=self.constants.SECOND_BUY_NOW_XPATH)
        sleep(3)
        self.__scroll_down_page()
        self.click(xpath=self.constants.SECOND_BUY_NOW_XPATH)
        """Skip Add-ons and click on Continue"""
        self.click(xpath=self.constants.CONTINUE_WITHOUT_ADD_XPATH)
        """Fill Contact fields - email field"""
        self.fill_field(xpath=self.constants.CONTACT_EMAIL_PLACEHOLDER, value=user.email)
        """Fill first name fild"""
        self.fill_field(xpath=self.constants.CONTACT_FIRSTNAME_PLACEHOLDER, value=user.firstname)
        """Fill last name field"""
        self.fill_field(xpath=self.constants.CONTACT_LASTNAME_PLACEHOLDER, value=user.lastname)
        """Click on Next button"""
        self.click(xpath=self.constants.CONTACT_NEXT_BUTTON_XPATH)
        """Fill Shipping address"""
        self.fill_field(xpath=self.constants.SHIPPING_ADDRESS_PLACEHOLDER, value=user.address)
        """Fill Shipping city"""
        self.fill_field(xpath=self.constants.SHIPPING_CITY_PLACEHOLDER, value=user.city)
        """Fill State field"""
        self.click(xpath=self.constants.SHIPPING_STATE_XPATH)
        self.click(xpath=self.constants.SHIPPING_STATE_OPTION)
        """Fill Shipping Zip"""
        self.fill_field(xpath=self.constants.SHIPPING_ZIP_PLACEHOLDER, value=user.zip)
        """Click on Next button"""
        self.click(xpath=self.constants.SHIPPING_NEXT_BUTTON_XPATH)
        sleep(5)

    @wait_until_ok(timeout=5, period=0.5)
    @log_decorator
    def verify_total_checkout_without(self):
        assert self.get_element_text(
            xpath=self.constants.SECOND_TOTAL_WITHOUT_XPATH) == self.constants.SECOND_TOTAL_VERIFY_TEXT
        f"Actual: {self.get_element_text(xpath=self.constants.SECOND_TOTAL_WITHOUT_XPATH)}"

    @wait_until_ok(timeout=5, period=0.5)
    @log_decorator
    def verify_checkout_complete(self):
        assert self.get_element_text(
            self.constants.VERIFY_PAYMENT_OPEN_XPATH) == self.constants.VERIFY_PAYMENT_OPEN_TEXT
        f"Actual: {self.get_element_text(xpath=self.constants.VERIFY_PAYMENT_OPEN_XPATH)}"

    def find_element(self, xpath):
        pass

    @wait_until_ok(timeout=5, period=1)
    @log_decorator
    def third_checkout(self, user):
        """Click on Shop button in homepage"""
        self.click(xpath=self.constants.SHOP_BUTTON_XPATH)
        """Click on Buy now"""
        self.find_element(xpath=self.constants.THIRD_BUY_NOW_XPATH)
        sleep(3)
        self.__scroll_down_page()
        self.click(xpath=self.constants.THIRD_BUY_NOW_XPATH)
        """Skip Add-ons and click on Continue"""
        self.click(xpath=self.constants.CONTINUE_WITHOUT_ADD_XPATH)
        """Fill Contact fields - email field"""
        self.fill_field(xpath=self.constants.CONTACT_EMAIL_PLACEHOLDER, value=user.email)
        """Fill first name fild"""
        self.fill_field(xpath=self.constants.CONTACT_FIRSTNAME_PLACEHOLDER, value=user.firstname)
        """Fill last name field"""
        self.fill_field(xpath=self.constants.CONTACT_LASTNAME_PLACEHOLDER, value=user.lastname)
        """Click on Next button"""
        self.click(xpath=self.constants.CONTACT_NEXT_BUTTON_XPATH)
        """Fill Shipping address"""
        self.fill_field(xpath=self.constants.SHIPPING_ADDRESS_PLACEHOLDER, value=user.address)
        """Fill Shipping city"""
        self.fill_field(xpath=self.constants.SHIPPING_CITY_PLACEHOLDER, value=user.city)
        """Fill State field"""
        self.click(xpath=self.constants.SHIPPING_STATE_XPATH)
        self.click(xpath=self.constants.SHIPPING_STATE_OPTION)
        """Fill Shipping Zip"""
        self.fill_field(xpath=self.constants.SHIPPING_ZIP_PLACEHOLDER, value=user.zip)
        """Click on Next button"""
        self.click(xpath=self.constants.SHIPPING_NEXT_BUTTON_XPATH)
        sleep(5)

    @wait_until_ok(timeout=5, period=0.5)
    @log_decorator
    def verify_checkout_complete(self):
        assert self.get_element_text(
            self.constants.VERIFY_PAYMENT_OPEN_XPATH) == self.constants.VERIFY_PAYMENT_OPEN_TEXT
        f"Actual: {self.get_element_text(xpath=self.constants.VERIFY_PAYMENT_OPEN_XPATH)}"

    @wait_until_ok(timeout=5, period=1)
    @log_decorator
    def go_to_first_checkout(self, user):
        """Go through second checkout"""
        self.click(xpath=self.constants.SHOP_BUTTON_XPATH)
        """Click on Buy now"""
        self.find_element(xpath=self.constants.FIRST_BUY_NOW_XPATH)
        sleep(3)
        self.__scroll_down_page()
        self.click(xpath=self.constants.FIRST_BUY_NOW_XPATH)
        from pages.first_checkout import FirstCheckoutPage
        return FirstCheckoutPage(self.driver)
