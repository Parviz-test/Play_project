from playwright.sync_api import sync_playwright, expect


def test_dynamic_loading_11():
    with (sync_playwright() as drv):
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading")
        page_go_to=page.locator("//*[@id='content']/div/a[1]")
        page_go_to.click()

        btn_start2 = page.get_by_role("button", name="Start")
        btn_start2.click()
        page.wait_for_selector("#finish")
        # finish_text2 = page.locator("#finish")
        expect(page.locator("#finish")).to_have_text("Hello World!")
        print("✅ Элемент появился: Hello World!")

test_dynamic_loading_11()