from playwright.sync_api import sync_playwright


def test_dynamic_loading_11():
    with (sync_playwright() as drv):
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
    page.goto(f"{BASE_URL}{USR_DYN_LOAD2}")

    btn_start2 = page.get_by_role("button", name="Start")
    btn_start2.click()

    finish_text2 = page.locator("#finish")
    expect(finish_text2).to_be_visible()
    expect(finish_text2).to_contain_text("World")
    txt = finish_text2.inner_text()
    assert "Hello World" in txt
    print(txt, finish_text2.is_visible())