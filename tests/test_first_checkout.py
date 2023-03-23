from pages.utils import User


class TestFirstCheckout:

    def test_first_checkout(self, start_page, random_user):
        first_checkout = start_page.navigate_to_first_checkout(random_user)
        first_checkout.fill_users_data(random_user)

    def test_terms_cond_opened(self, start_page, random_user):
        terms_cond = start_page.navigate_to_first_checkout(random_user)
        terms_cond.verify_terms_opened()

    def test_privacy_opened(self, start_page, random_user):
        privacy = start_page.navigate_to_first_checkout(random_user)
        privacy.verify_privacy_opened()

    def test_wrong_zip(self, start_page, random_user):
        wrong_zip = start_page.navigate_to_first_checkout(random_user)
        wrong_zip.verify_wrong_zip()

    def test_invalid_zip(self, start_page, random_user):
        invalid_zip = start_page.navigate_to_first_checkout(random_user)
        invalid_zip.verify_invalid_zip(User(email="testzip2203@E2E.test", zip="00000"))

    def test_empty_zip(self, start_page, random_user):
        empty_zip = start_page.navigate_to_first_checkout(random_user)
        empty_zip.verify_empty_zip(User(email="mpoluliak@suvie.com"))

    def test_incorrect_email(self, start_page, random_user):
        incorrect_email = start_page.navigate_to_first_checkout(random_user)
        incorrect_email.verify_incorrect_email(User(zip="90001", email="usertest().test"))

    def test_empty_email(self, start_page, random_user):
        empty_email = start_page.navigate_to_first_checkout(random_user)
        empty_email.verify_empty_email(User(zip="90001"))

    # def test_total_price(self, start_page, random_user):
    #     t_price = start_page.navigate_to_first_checkout(random_user)
    #     t_price.fill_users_data(random_user)
    #     t_price.verify_total_price()

    def test_serve_click(self, start_page, random_user):
        serve = start_page.navigate_to_first_checkout(random_user)
        serve.verify_serve_clickable(random_user)
