from time import sleep

import requests

from constants.first_checkout import FirstCheckout
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_decorator


class FirstCheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = FirstCheckout()

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

    @wait_until_ok(timeout=5, period=0.5)
    def verify_terms_opened(self):
        """Click on Terms and Conditions link"""
        self.click(self.constants.TERMS_COND_XPATH)
        """Verify page is opened"""
        response = requests.get("https://www.suvie.com/terms-and-conditions/")
        assert response.status_code == 200
        # assert self.get_element_text(self.constants.VERIFY_TERMS_COND_XPATH) == self.constants.VERIFY_TERMS_COND_TEXT
        # f"Actual: {self.get_element_text(xpath=self.constants.VERIFY_TERMS_COND_XPATH)}"

    def verify_privacy_opened(self):
        """Privacy page is opened"""
        self.click(self.constants.PRIVACY_POLICY_XPATH)
        response = requests.get("https://www.suvie.com/privacy-policy/")
        assert response.status_code == 200

    def verify_wrong_zip(self):
        self.fill_field(xpath=self.constants.START_ZIPCODE_PLACEHOLDER, value="093")
        self.fill_field(xpath=self.constants.START_EMAIL_PLACEHOLDER, value="test@test.com")
        assert self.get_element_text(self.constants.WRONG_ZIP_ALERT_XPATH) == self.constants.WRONG_ZIP_ALERT_TEXT
        f"Actual: {self.get_element_text(xpath=self.constants.WRONG_ZIP_ALERT_XPATH)}"

    def verify_invalid_zip(self):
        self.fill_field(xpath=self.constants.START_ZIPCODE_PLACEHOLDER, value="00000")
        self.fill_field(xpath=self.constants.START_EMAIL_PLACEHOLDER, value="mpolulffffffffffffffak@suvi.com")
        sleep(5)
        self.click(xpath=self.constants.START_CONTINUE_BTN_XPATH)
        assert self.get_element_text(self.constants.INVALID_ZIP_ALERT_XPATH) == self.constants.INVALID_ZIP_ALERT_TEXT
        f"Actual: {self.get_element_text(xpath=self.constants.INVALID_ZIP_ALERT_XPATH)}"
