class TestThirdCheckout:

    def test_third_checkout(self, start_page, random_user):
        third_checkout = start_page.navigate_to_third_checkout(random_user)
        third_checkout.fill_users_data_3(random_user)
        third_checkout.verify_checkout_complete()
