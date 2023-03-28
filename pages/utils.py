import datetime
import logging
import random
import string
from random import choice
from string import ascii_lowercase
from string import ascii_uppercase
from time import sleep


def random_upper():
    """Generate random string"""
    random_string = (''.join(choice(ascii_uppercase) for i in range(12)))
    return random_string


def random_low():
    """Generate random string"""
    random_string_low = (''.join(choice(ascii_lowercase) for i in range(12)))
    return random_string_low


def random_num():
    """Generate random number"""
    return str(random.randint(90001, 90001))


def random_str(length=5):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def wait_until_ok(timeout=8, period=1):
    """Reties until OK"""

    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        log.error(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_decorator(original_function):
    """Logging actions using doc stings"""

    log = logging.getLogger("[LogDecorator]")

    def wrapper(*args, **kwargs):
        result = original_function(*args, **kwargs)
        log.info(f"{original_function.__doc__}")
        return result

    return wrapper


class User:
    def __init__(self, firstname="", lastname="", email="", address="", city="", zip=""):
        self.firstname = firstname
        self.email = email
        self.lastname = lastname
        self.address = address
        self.city = city
        self.zip = zip

    def fill_data(self, firstname="", email="", lastname="", address="", city="", zip=""):
        """Fill fields with sample data"""
        user = random_str()
        self.firstname = f"{user}{random_str(7)}" if not firstname else firstname
        self.email = f"{user}{random_str(4)}@E2E.com" if not email else email
        self.lastname = f"{user}{random_str(6)}{random_num()}" if not lastname else lastname
        self.address = f"{random_str(6)}{random_num()}" if not address else address
        self.city = f"{random_str(6)}{random_num()}" if not city else city
        self.zip = f"{random_num()}" if not zip else zip
