from time import sleep

from constants.homepage_checkout import HomePage
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_decorator


class FirstCheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HomePage()

    @wait_until_ok(timeout=5, period=1)
    # @log_decorator
    def fill_users_data(self, user):
        """Fill ZipCode and Email"""
        self.fill_field(xpath=self.constants.START_ZIPCODE_PLACEHOLDER, value=user.zip)
        self.fill_field(xpath=self.constants.START_EMAIL_PLACEHOLDER, value=user.email)
        sleep(5)
        """Click on Continue"""
        self.click(xpath=self.constants.START_CONTINUE_BTN_XPATH)
        sleep(5)
        """Click on Continue in MealPlan"""
        self.click(xpath=self.constants.MEAL_PLAN_CONTINUE_XPATH)
        """Skip Add-ons and click on Continue"""
        self.click(xpath=self.constants.CHECK_CONTINUE_WITHOUT_XPATH)
        """Fill first name fild"""
        self.fill_field(xpath=self.constants.CONTACT_FIRSTNAME_PLACEHOLDER, value=user.firstname)
        """Fill last name field"""
        self.fill_field(xpath=self.constants.CONTACT_LASTNAME_PLACEHOLDER, value=user.lastname)
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
