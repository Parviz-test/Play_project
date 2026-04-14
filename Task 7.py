from playwright.sync_api import sync_playwright


def test_input_clear_07():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        link_form = navigate_to_example(page, TITLE_INPUTS)
        field = page.locator("input[type='number']")
        field.fill(NUMBER_123)
        _assert_selected(NUMBER_123, field.input_value())

        field.clear()
        field.fill(NUMBER_456)
        _assert_selected(NUMBER_456, field.input_value())

        print(f"✅ Введено: {field.input_value()}")
