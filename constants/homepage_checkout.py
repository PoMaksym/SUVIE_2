class HomePage:
    SHOP_BUTTON_XPATH = './/a[@class="btn btn_primary ml-6 min-w-[7.8125rem] xl:ml-4"][@href="/shop/"]'
    SECOND_BUY_NOW_XPATH = './/a[@href="https://app.suvie.com/purchase/?product-sku=PKG_SS_SV3_A1&site-version=a"]'
    CONTINUE_WITHOUT_ADD_XPATH = './/button[@class="btn btn_primary btn_size_default btn_rounded_default btn_size_default btn_rounded_default w-full"]'
    CONTACT_EMAIL_PLACEHOLDER = './/input[@placeholder="Email"]'
    CONTACT_FIRSTNAME_PLACEHOLDER = './/input[@placeholder="First name"]'
    CONTACT_LASTNAME_PLACEHOLDER = './/input[@placeholder="Last name"]'
    CONTACT_NEXT_BUTTON_XPATH = './/button[@data-cy="checkout-form-contact-section-next-button"]'
    SHIPPING_ADDRESS_PLACEHOLDER = './/input[@placeholder="Address"]'
    SHIPPING_CITY_PLACEHOLDER = './/input[@placeholder="City"]'
    SHIPPING_ZIP_PLACEHOLDER = './/input[@placeholder="Zip Code"]'
    SHIPPING_NEXT_BUTTON_XPATH = './/button[@data-cy="checkout-form-shipping-section-next-button"]'
    VERIFY_PAYMENT_OPEN_XPATH = './/button[contains(text(), "Pay with Credit Card")]'
    VERIFY_PAYMENT_OPEN_TEXT = "Pay with Credit Card"
    SHIPPING_STATE_XPATH = './/select'
    SHIPPING_STATE_OPTION = './/option[@value=3438]'
    THIRD_BUY_NOW_XPATH = './/a[@href="https://app.suvie.com/purchase/?product-sku=PKG_CHEF_SV3_A1&site-version=a"]'
    FIRST_BUY_NOW_XPATH = './/a[@href="https://app.suvie.com/checkout/start/?product-sku=PKG_SV3_A1&site-version=a"]'

    SECOND_TOTAL_WITHOUT_XPATH = './/div[@data-cy="order-total-total-price"]'
    SECOND_TOTAL_VERIFY_TEXT = "$799.00"
