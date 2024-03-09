from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    # assert page.is_hidden("text=Celebrating Beauty and Style")   # Python-specific

    expect(page.locator("text=Celebrating Beauty and Style")).to_be_hidden()  # Playwright-specific

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
