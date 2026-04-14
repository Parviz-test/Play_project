from playwright.sync_api import sync_playwright


def run_full_test():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        base_url = "https://herokuapp.com"
        results = {}

        # 1. Form Authentication
        page.goto(f"{base_url}/login")
        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        page.click("button[type='submit']")
        if page.locator(".flash.success").is_visible():
            page.screenshot(path="auth.png")
            results["Form Authentication"] = "✅"

        # 2. Checkboxes
        page.goto(f"{base_url}/checkboxes")
        page.locator("input").first.check()
        page.locator("input").last.uncheck()
        page.screenshot(path="checkboxes.png")
        results["Checkboxes"] = "✅"

        # 3. Dropdown
        page.goto(f"{base_url}/dropdown")
        page.select_option("#dropdown", label="Option 2")
        page.screenshot(path="dropdown.png")
        results["Dropdown"] = "✅"

        # 4. Inputs
        page.goto(f"{base_url}/inputs")
        page.fill("input[type='number']", "999")
        page.screenshot(path="inputs.png")
        results["Inputs"] = "✅"

        # 5. Hovers
        page.goto(f"{base_url}/hovers")
        page.locator(".figure").first.hover()
        if page.locator("h5").first.is_visible():
            page.screenshot(path="hovers.png")
            results["Hovers"] = "✅"

        print("\nОТЧЁТ:")
        for test, status in results.items():
            print(f"{status} {test}")

        if len(results) == 5:
            print("\nВсе тесты пройдены!")

        browser.close()
