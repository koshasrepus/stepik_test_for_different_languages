def test_button_availability(browser):
    browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    add_to_cart_button = browser.find_element_by_class_name("btn-add-to-basket")
    assert add_to_cart_button.text is not None



