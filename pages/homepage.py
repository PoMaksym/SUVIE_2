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
    def navigate_to_second_checkout(self, user):
        """Go through checkout"""
        self.click(xpath=self.constants.SHOP_BUTTON_XPATH)
        """Click on Buy now"""
        self.find_element(xpath=self.constants.SECOND_BUY_NOW_XPATH)
        sleep(3)
        self.__scroll_down_page()
        self.click(xpath=self.constants.SECOND_BUY_NOW_XPATH)
        from pages.second_checkout import SecondCheckoutPage
        return SecondCheckoutPage(self.driver)

    def find_element(self, xpath):
        pass

    @wait_until_ok(timeout=5, period=1)
    @log_decorator
    def navigate_to_third_checkout(self, user):
        """Click on Shop button in homepage"""
        self.click(xpath=self.constants.SHOP_BUTTON_XPATH)
        """Click on Buy now"""
        self.find_element(xpath=self.constants.THIRD_BUY_NOW_XPATH)
        sleep(3)
        self.__scroll_down_page()
        self.click(xpath=self.constants.THIRD_BUY_NOW_XPATH)
        from pages.third_checkout import ThirdCheckoutPage
        return ThirdCheckoutPage(self.driver)

    @wait_until_ok(timeout=5, period=1)
    @log_decorator
    def navigate_to_first_checkout(self, user):
        """Navigate to first checkout"""
        self.click(xpath=self.constants.SHOP_BUTTON_XPATH)
        """Click on Buy now"""
        self.find_element(xpath=self.constants.FIRST_BUY_NOW_XPATH)
        sleep(3)
        self.__scroll_down_page()
        self.click(xpath=self.constants.FIRST_BUY_NOW_XPATH)
        from pages.first_checkout import FirstCheckoutPage
        return FirstCheckoutPage(self.driver)
