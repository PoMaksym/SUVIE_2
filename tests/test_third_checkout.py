class TestThirdCheckout:

    def test_third_checkout(self, start_page, random_user):
        start_page.third_checkout(random_user)
        start_page.verify_checkout_complete()
