def test_navigation():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        link_form = navigate_to_example(page, TITLE_FORM)
        assert_text_in_url(link_form, LINK_LOGIN)
        print(f"T2: ✅ Перешли в: Form Authentication | URL: {link_form}")