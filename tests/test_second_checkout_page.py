class TestSecondCheckout:

    def test_checkout_with_random_data(self, start_page, random_user):
        second_checkout = start_page.navigate_to_second_checkout(random_user)
        second_checkout.fill_users_data_2(random_user)
        second_checkout.verify_checkout_complete()
        second_checkout.verify_total_checkout_without()
