from constants.homepage_checkout import HomePage
from time import sleep

from constants.homepage_checkout import HomePage
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_decorator, random_str


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
    def second_checkout(self):
        """Click on Shop button in homepage"""
        self.click(xpath=self.constants.SHOP_BUTTON_XPATH)
        """Click on Buy now"""
        self.find_element(xpath=self.constants.SECOND_BUY_NOW_XPATH)
        sleep(3)
        self.__scroll_down_page()
        self.click(xpath=self.constants.SECOND_BUY_NOW_XPATH)
        """Skip Add-ons and click on Continue"""
        self.click(xpath=self.constants.CONTINUE_WITHOUT_ADD_XPATH)
        """Fill Contact fields - email field"""
        self.fill_field(xpath=self.constants.CONTACT_EMAIL_PLACEHOLDER, value=random_str(6) + "@test.com")
        """Fill first name fild"""
        self.fill_field(xpath=self.constants.CONTACT_FIRSTNAME_PLACEHOLDER, value=random_str(7))
        """Fill last name field"""
        self.fill_field(xpath=self.constants.CONTACT_LASTNAME_PLACEHOLDER, value=random_str(7))
        """Click on Next button"""
        self.click(xpath=self.constants.CONTACT_NEXT_BUTTON_XPATH)
        """Fill Shipping address"""
        self.fill_field(xpath=self.constants.SHIPPING_ADDRESS_PLACEHOLDER, value=random_str(6))
        """Fill Shipping city"""
        self.fill_field(xpath=self.constants.SHIPPING_CITY_PLACEHOLDER, value=random_str(9))
        """Fill State field"""
        self.click(xpath=self.constants.SHIPPING_STATE_XPATH)
        self.click(xpath=self.constants.SHIPPING_STATE_OPTION)
        """Fill Shipping Zip"""
        self.fill_field(xpath=self.constants.SHIPPING_ZIP_PLACEHOLDER, value=90210)
        """Click on Next button"""
        self.click(xpath=self.constants.SHIPPING_NEXT_BUTTON_XPATH)
        sleep(5)

    @wait_until_ok(timeout=5, period=0.5)
    @log_decorator
    def verify_checkout_complete(self):
        assert self.get_element_text(
            self.constants.VERIFY_PAYMENT_OPEN_XPATH) == self.constants.VERIFY_PAYMENT_OPEN_TEXT
        f"Actual: {self.get_element_text(xpath=self.constants.VERIFY_PAYMENT_OPEN_XPATH)}"

    def find_element(self, xpath):
        pass
