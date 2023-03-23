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
    @log_decorator
    def fill_users_data(self, user):
        """Fill fields with random data"""
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
        """Verify payment card is opened"""
        assert self.get_element_text(
            self.constants.VERIFY_PAYMENT_OPEN_XPATH) == self.constants.VERIFY_PAYMENT_OPEN_TEXT
        f"Actual: {self.get_element_text(xpath=self.constants.VERIFY_PAYMENT_OPEN_XPATH)}"

    @log_decorator
    def verify_terms_opened(self):
        """Terms is opened"""
        self.click(self.constants.TERMS_COND_XPATH)
        """Verify page is opened"""
        response = requests.get("https://www.suvie.com/terms-and-conditions/")
        assert response.status_code == 200
        # assert self.get_element_text(self.constants.VERIFY_TERMS_COND_XPATH) == self.constants.VERIFY_TERMS_COND_TEXT
        # f"Actual: {self.get_element_text(xpath=self.constants.VERIFY_TERMS_COND_XPATH)}"

    @log_decorator
    def verify_privacy_opened(self):
        """Privacy page is opened"""
        self.click(self.constants.PRIVACY_POLICY_XPATH)
        response = requests.get("https://www.suvie.com/privacy-policy/")
        assert response.status_code == 200

    @log_decorator
    def verify_wrong_zip(self):
        """Verify wrong zip code"""
        self.fill_field(xpath=self.constants.START_ZIPCODE_PLACEHOLDER, value="093")
        self.fill_field(xpath=self.constants.START_EMAIL_PLACEHOLDER, value="test@test.com")
        assert self.get_element_text(self.constants.WRONG_ZIP_ALERT_XPATH) == self.constants.WRONG_ZIP_ALERT_TEXT
        f"Actual: {self.get_element_text(xpath=self.constants.WRONG_ZIP_ALERT_XPATH)}"

    @log_decorator
    def verify_invalid_zip(self, user):
        """Verify invalid zip code"""
        self.fill_field(xpath=self.constants.START_ZIPCODE_PLACEHOLDER, value=user.zip)
        self.fill_field(xpath=self.constants.START_EMAIL_PLACEHOLDER, value=user.email)
        sleep(5)
        self.click(xpath=self.constants.START_CONTINUE_BTN_XPATH)
        sleep(5)
        assert self.get_element_text(self.constants.INVALID_ZIP_ALERT_XPATH) == self.constants.INVALID_ZIP_ALERT_TEXT
        f"Actual: {self.get_element_text(xpath=self.constants.INVALID_ZIP_ALERT_XPATH)}"

    @log_decorator
    def verify_empty_zip(self, user):
        """Verify empty zip"""
        self.fill_field(xpath=self.constants.START_EMAIL_PLACEHOLDER, value=user.email)
        sleep(3)
        self.click(xpath=self.constants.START_CONTINUE_BTN_XPATH)
        sleep(3)
        assert self.get_element_text(self.constants.EMPTY_ZIP_CODE_XPATH) == self.constants.EMPTY_ZIP_CODE_TEXT
        f"Actual: {self.get_element_text(xpath=self.constants.EMPTY_ZIP_CODE_XPATH)}"

    @log_decorator
    def verify_empty_email(self, user):
        """Verify empty email"""
        self.fill_field(xpath=self.constants.START_ZIPCODE_PLACEHOLDER, value=user.zip)
        sleep(3)
        self.click(xpath=self.constants.START_CONTINUE_BTN_XPATH)
        assert self.get_element_text(self.constants.EMPTY_EMAIL_START_XPATH) == self.constants.EMPTY_EMAIL_START_TEXT
        f"Actual: {self.get_element_text(xpath=self.constants.EMPTY_EMAIL_START_XPATH)}"

    @log_decorator
    def verify_incorrect_email(self, user):
        """Verify incorrect email"""
        self.fill_field(xpath=self.constants.START_ZIPCODE_PLACEHOLDER, value=user.zip)
        self.fill_field(xpath=self.constants.START_EMAIL_PLACEHOLDER, value=user.email)
        sleep(3)
        self.click(xpath=self.constants.START_CONTINUE_BTN_XPATH)
        assert self.get_element_text(
            self.constants.INCORRECT_EMAIL_START_XPATH) == self.constants.INCORRECT_EMAIL_START_TEXT
        f"Actual: {self.get_element_text(xpath=self.constants.INCORRECT_EMAIL_START_XPATH)}"

    # def verify_total_price(self):
    #     s = self.get_element_text(self.constants.SUVIE_PRICE_XPATH)
    #     robot_price = int(s.replace('$', ''))
    #     print(robot_price)
    #     tax = self.get_element_text(self.constants.TAXE_PRICE_XPATH)
    #     tax_price = int(tax.replace('$', ''))
    #     print(tax_price)
    #     total = self.get_element_text(self.constants.TOTAL_PRICE_XPATH)
    #     total_price = int(total.replace('$', ''))

    @log_decorator
    @wait_until_ok(timeout=5, period=0.6)
    def verify_serve_clickable(self, user):
        """Verify radiobutton is clickable"""
        self.fill_field(xpath=self.constants.START_ZIPCODE_PLACEHOLDER, value=user.zip)
        self.fill_field(xpath=self.constants.START_EMAIL_PLACEHOLDER, value=user.email)
        sleep(5)
        """Click on Continue"""
        self.click(xpath=self.constants.START_CONTINUE_BTN_XPATH)
        sleep(5)
        self.click(xpath=self.constants.FOUR_SERVE_BUTTON_XPATH)
        self.click(xpath=self.constants.TWO_SERVE_BUTTON_XPATH)
