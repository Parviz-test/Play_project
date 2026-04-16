from playwright.sync_api import sync_playwright


def test_java_scripts_alerts_09():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/javascript_alerts")
        page.on("dialog", lambda dialog: dialog.accept())
        btn_js_alerts = page.get_by_role("button", name = "Click for JS Alert")
        btn_js_alerts.click()
        result=page.locator("#result")
        txt_result=result.inner_text()
        expext_txt="You successfully clicked an alert"
        assert txt_result in expext_txt, "текст не найден"

        print(f"✅ Alert принят. Сообщение: '{txt_result}'")

test_java_scripts_alerts_09()