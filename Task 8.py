from playwright.sync_api import sync_playwright

def test_hover_08():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/hovers")

        first_figure = page.locator(".figure").first

        first_figure.hover()

        user_info = first_figure.locator("h5")

        if user_info.is_visible():
            print(f"✅ Навели на изображение. Текст: {user_info.inner_text()}")
        else:
            print("❌ Текст не появился")

        browser.close()
