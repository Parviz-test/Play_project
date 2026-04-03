def test_main_page():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        assert_text_in_url(page.url, TEXT_TO_FIND)
        loc_h1 = page.locator("h1.heading")
        text_h1 = loc_h1.text_content()
        assert TEXT_TO_FIND in text_h1, \
            f"Не тот заголовок!\n" \
            f"Ожидание: '{TEXT_TO_FIND}' в заголовке\n" \
            f"Актуальный текст заголовка: '{text_h1}'"
        print(f"T1: ✅ Сайт доступен. Заголовок: '{text_h1}'")
