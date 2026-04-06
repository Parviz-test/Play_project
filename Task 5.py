# 🌐26x05: Чекбоксы (Check/Uncheck)
def work_with_chekbox():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless =False,slow_mo=1000)
        page = browser.new_page()
        link_form = navigate_to_example(page, TITLE_CHECKBOXES)
        chkbox1 = page.locator("//form[@id='checkboxes']/input[1]")
        chkbox2 = page.locator("//form[@id='checkboxes']/input[2]")

        assert not chkbox1.is_checked(), "Чекбокс 1 ОТМЕЧЕН!"
        assert chkbox2.is_checked(), "Чекбокс 2 НЕ отмечен!"


        chkbox1.check()
        chkbox2.uncheck()

        print(f"T5: ✅ Checkbox 1: checked={chkbox1.is_checked()}\n"
              f"T5: ✅ Checkbox 2: checked={chkbox2.is_checked()}")
