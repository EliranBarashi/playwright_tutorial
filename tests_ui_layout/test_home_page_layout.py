from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
import pytest

@pytest.mark.integration
def test_about_us_section_verbiage(login_set_up) -> None:
    page = login_set_up
    # browser = playwright.chromium.launch(headless=False,slow_mo=500)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()

    # context.close()
    # browser.close()

@pytest.mark.regression
def test_about_us_section_verbiage_2(login_set_up) -> None:
    page = login_set_up
    # browser = playwright.chromium.launch(headless=False,slow_mo=500)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    expect(home_page.celebrate_body_fake).to_be_visible()

    # context.close()
    # browser.close()

