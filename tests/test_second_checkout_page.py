class TestSecondCheckout:

    def test_checkout_with_random_data(self, start_page, random_user):
        start_page.second_checkout(random_user)
        start_page.verify_checkout_complete()

    def test_total_price_without_add(self, start_page, random_user):
        start_page.second_checkout(random_user)
        start_page.verify_total_checkout_without()
