class TestSecondCheckout:

    def test_second_checkout(self, start_page, random_user):
        start_page.second_checkout(random_user)
        start_page.verify_checkout_complete()
