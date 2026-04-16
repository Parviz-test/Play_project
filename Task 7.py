from playwright.sync_api import sync_playwright


def test_input_clear_07():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=3000)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/inputs")



        field = page.locator("input[type='number']")
        page.fill("input[type='number']","123")
        txt = field.input_value()

        assert txt == "123"
        field.clear()
        page.fill("input[type='number']","456")
        assert field.input_value() == "456"

        print(f"✅ Введено: {field.input_value()}")

test_input_clear_07()
