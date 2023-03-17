import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.homepage import StartPage
from pages.utils import User


@pytest.fixture()
def start_page():
    # Pre-conditions
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    # Steps
    yield StartPage(driver)
    # Post-conditions
    driver.close()


@pytest.fixture()
def random_user():
    user = User()
    user.fill_data()
    return user

