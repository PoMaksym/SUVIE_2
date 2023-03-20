class FirstCheckout:
    START_ZIPCODE_PLACEHOLDER = './/input[@placeholder="Zip Code"]'
    START_EMAIL_PLACEHOLDER = './/input[@placeholder="Email Address"]'
    START_CONTINUE_BTN_XPATH = './/button[@data-cy="checkout-start-form-submit-button"]'
    MEAL_PLAN_CONTINUE_XPATH = './/button[@data-cy="checkout-meal-plan-form-submit-button"]'
    CHECK_CONTINUE_WITHOUT_XPATH = './/button[@data-cy="checkout-form-addons-section-next-button"]'
    CONTACT_FIRSTNAME_PLACEHOLDER = './/input[@placeholder="First name"]'
    CONTACT_LASTNAME_PLACEHOLDER = './/input[@placeholder="Last name"]'
    SHIPPING_ADDRESS_PLACEHOLDER = './/input[@placeholder="Address"]'
    SHIPPING_CITY_PLACEHOLDER = './/input[@placeholder="City"]'
    SHIPPING_STATE_XPATH = './/select'
    SHIPPING_STATE_OPTION = './/option[@value=3438]'
    SHIPPING_ZIP_PLACEHOLDER = './/input[@placeholder="Zip Code"]'
    SHIPPING_NEXT_BUTTON_XPATH = './/button[@data-cy="checkout-form-shipping-section-next-button"]'
    VERIFY_PAYMENT_OPEN_XPATH = './/button[contains(text(), "Pay with Credit Card")]'
    VERIFY_PAYMENT_OPEN_TEXT = "Pay with Credit Card"
    TERMS_COND_XPATH = './/a[@href="https://www.suvie.com/terms-and-conditions/"]'
    VERIFY_TERMS_COND_XPATH = './/span[contains(text(), "Home Tech Innovation, Inc. Terms and Conditions")]'
    VERIFY_TERMS_COND_TEXT = "Home Tech Innovation, Inc. Terms and Conditions"
