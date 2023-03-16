class TestFirstCheckout:

    def test_first_checkout(self, start_page, random_user):
        start_page.first_checkout(random_user)
        start_page.verify_checkout_complete()
