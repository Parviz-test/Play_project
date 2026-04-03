def logout_from_system():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        btn_logout = page.locator(".button[href='/logout']")
        btn_logout.click()
        assert_text_in_url(page.url, LINK_LOGIN)
        print(f"T4: ✅ Успешный выход! URL: {page.url}")