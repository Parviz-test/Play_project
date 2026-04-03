# Task 1
# def test_task_01():
#     with sync_playwright() as drv:
#         browser = drv.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         page.goto(BASE_URL)
#
#         assert_text_in_url(page.url, TEXT_TO_FIND)
#         loc_h1 = page.locator("h1.heading")
#         text_h1 = loc_h1.text_content()
#         assert TEXT_TO_FIND in text_h1, \
#             f"Не тот заголовок!\n" \
#             f"Ожидание: '{TEXT_TO_FIND}' в заголовке\n" \
#             f"Актуальный текст заголовка: '{text_h1}'"
#         print(f"T1: ✅ Сайт доступен. Заголовок: '{text_h1}'")

        # Task 2
# def test_task_02():
#     with sync_playwright() as drv:
#         browser = drv.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         page.goto(BASE_URL)
#
#         link_form = navigate_to_example(page, TITLE_FORM)
#         assert_text_in_url(link_form, LINK_LOGIN)
#         print(f"T2: ✅ Перешли в: Form Authentication | URL: {link_form}")

# Task 3
# def test_task_03():
#     with sync_playwright() as drv:
#         browser = drv.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         page.goto(BASE_URL)
#
#         field_username = page.locator("#username")
#         field_password = page.locator("#password")
#         env_username = os.getenv("USER")
#         env_password = os.getenv("PASS")
#         field_username.fill(env_username)
#         field_password.fill(env_password)
#
#         btn_login = page.locator("//button/i[contains(@class, 'sign-in')]")
#         btn_login.click()
#         assert_text_in_url(page.url, LINK_SECURE)
#         print(f"T3: ✅ Успешный вход! URL: {page.url}")

# Task 4

# def test_task_04():
#     with sync_playwright() as drv:
#         browser = drv.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         page.goto(BASE_URL)
#
#         btn_logout = page.locator(".button[href='/logout']")
#         btn_logout.click()
#         assert_text_in_url(page.url, LINK_LOGIN)
#         print(f"T4: ✅ Успешный выход! URL: {page.url}")

# Task 5
# def test_task_05():
#     with sync_playwright() as drv:
#         browser = drv.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         page.goto(BASE_URL)
#
#         link_form = navigate_to_example(page, TITLE_CHECKBOXES)
#         chkbox1 = page.locator("//form[@id='checkboxes']/input[1]")
#         chkbox2 = page.locator("//form[@id='checkboxes']/input[2]")
#
#         assert not chkbox1.is_checked(), "Чекбокс 1 ОТМЕЧЕН!"
#         assert chkbox2.is_checked(), "Чекбокс 2 НЕ отмечен!
#         chkbox1.check()
#         chkbox2.uncheck()
#         print(f"T5: ✅ Checkbox 1: checked={chkbox1.is_checked()}\n"
#               f"T5: ✅ Checkbox 2: checked={chkbox2.is_checked()}")

# Task 6
# def test_task_06():
#
#     with sync_playwright() as drv:
#         browser = drv.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         page.goto(BASE_URL)
#
#         link_form = navigate_to_example(page, TITLE_DROPDOWN)
#         assert_text_in_url(link_form, LINK_DROPDOWN)
#         selected_option = page.locator("[selected='selected']")
#         _assert_selected(OPTION_0, selected_option.inner_text())
#
#         drop_list = page.locator("#dropdown")
#         drop_list.select_option("1")
#         _assert_selected(OPTION_1, selected_option.inner_text())
#
#         drop_list.select_option("2")
#         _assert_selected(OPTION_2, selected_option.inner_text())
#
#         print(f"✅ Выбрано: {selected_option.inner_text()}")

# Task 7
def test_task_07():
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

  # Task 8
def test_task_08():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        link_form = navigate_to_example(page, TITLE_HOVERS)
        field = page.locator("input[type='number']")

        figures_xpath = page.locator("//div[@class='figure']")
        figures_css = page.locator(".figure")
        print(f"{figures_xpath.count()} {figures_css.count()}")
        # figure = page.locator(".figure:nth-child(3)")
        figure = page.locator("//div[@class='figure'][1]")
        # figure = figures_css.all()[0]
        figure = figures_css.first
        fig_caption = figure.locator(".figcaption h5")
        figure.hover()
        assert fig_caption.is_visible(), f"Текст '{TEXT_NAME_USER1}' не видим"
        _assert_selected(TEXT_NAME_USER1, fig_caption.inner_text())

        print(f"✅ Навели на изображение. Текст: '{fig_caption.inner_text()}'")
# Task 9
def test_task_09():

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

    # Task 10

    def test_task_10():
        with sync_playwright() as drv:
            browser = drv.chromium.launch(headless=False, slow_mo=1000)
            page = browser.new_page()
            page.goto(BASE_URL)

            link_form = navigate_to_example(page, TITLE_FILE_UPLOAD)

            # file_upload = Path(__file__).parent / FILE_NAME

            field_file_upload = page.locator("#file-upload")
            # field_file_upload.set_input_files(file_upload)
            field_file_upload.set_input_files(FILE_NAME)

            btn_upload = page.locator("#file-submit")
            btn_upload.click()

    # Task 11

    def test_task_11():
        with (sync_playwright() as drv):
            browser = drv.chromium.launch(headless=False, slow_mo=1000)
            page = browser.new_page()
        page.goto(f"{BASE_URL}{USR_DYN_LOAD2}")

        btn_start2 = page.get_by_role("button", name="Start")
        btn_start2.click()

        finish_text2 = page.locator("#finish")
        expect(finish_text2).to_be_visible()
        expect(finish_text2).to_contain_text("Worl")
        txt = finish_text2.inner_text()
        assert "Hello World" in txt
        print(txt, finish_text2.is_visible())



