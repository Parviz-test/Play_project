from playwright.sync_api import sync_playwright


def test_java_scripts_alerts_09():

    def accept_dialog(dialog):
        return dialog.accept()

    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        link_form = navigate_to_example(page, TITLE_JS_ALERTS)
        btn_js_alerts = page.get_by_role("button", name=BUTTON_JS_ALERTS)
        btn_js_alerts.click()
        time.sleep(3)
        page.on("dialog", accept_dialog)
        # page.on("dialog", lambda d: d.accept())
        result = page.locator("#result")
        _assert_selected(MSG_CLICK_JS_ALLERT, result.inner_text())

        print(f"✅ Alert принят. Сообщение: '{result.inner_text()}'")