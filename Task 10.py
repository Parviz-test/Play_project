from playwright.sync_api import sync_playwright


def test_dowload_files_10():
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
