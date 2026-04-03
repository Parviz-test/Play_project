def test_form_fill_click():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        field_username = page.locator("#username")
        field_password = page.locator("#password")
        env_username = os.getenv("USER")
        env_password = os.getenv("PASS")
        field_username.fill(env_username)
        field_password.fill(env_password)

        btn_login = page.locator("//button/i[contains(@class, 'sign-in')]")
        btn_login.click()
        assert_text_in_url(page.url, LINK_SECURE)
        print(f"T3: ✅ Успешный вход! URL: {page.url}")