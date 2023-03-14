class TestThirdCheckout:

    def test_third_checkout(self, start_page):
        start_page.third_checkout()
        start_page.verify_checkout_complete()
