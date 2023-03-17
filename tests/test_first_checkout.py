class TestFirstCheckout:

    def test_first_checkout(self, start_page, random_user):
        first_checkout = start_page.go_to_first_checkout(random_user)
