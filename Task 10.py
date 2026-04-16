from playwright.sync_api import sync_playwright


def test_dowload_files_10():
    with open("test_upload.txt", "w") as file:
        file.write("Hello Playwright")

    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/upload")

        page.set_input_files("#file-upload", "test_upload.txt")
        button_upload = page.locator("#file-submit").click()
        upload_file=page.locator("#uploaded-files")
        txt_upload_file=upload_file.inner_text()
        assert txt_upload_file== "test_upload.txt", "файл не найден"
        print("✅ Файл загружен: test_upload.txt")

test_dowload_files_10()