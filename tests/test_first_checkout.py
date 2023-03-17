class TestFirstCheckout:

    def test_first_checkout(self, start_page, random_user):
        first_checkout = start_page.navigate_to_first_checkout(random_user)

        first_checkout.fill_users_data(random_user)
