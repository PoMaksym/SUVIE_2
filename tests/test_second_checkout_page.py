class TestSecondCheckout:

    def test_second_checkout(self, start_page):
        start_page.second_checkout()
        start_page.verify_checkout_complete()
