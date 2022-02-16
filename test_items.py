def test_find_btns_buy(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    btn = browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert btn, "3,14zdec"







