# 26x06: Выпадающий список (Select)
from playwright.sync_api import sync_playwright

def dropdown_list():

    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        link_form = navigate_to_example(page, TITLE_DROPDOWN)
        assert_text_in_url(link_form, LINK_DROPDOWN)
        selected_option = page.locator("[selected='selected']")
        _assert_selected(OPTION_0, selected_option.inner_text())

        drop_list = page.locator("#dropdown")
        drop_list.select_option("1")
        _assert_selected(OPTION_1, selected_option.inner_text())

        drop_list.select_option("2")
        _assert_selected(OPTION_2, selected_option.inner_text())

        print(f"✅ Выбрано: {selected_option.inner_text()}")