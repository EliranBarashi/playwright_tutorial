import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def set_up(browser):
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")

    yield page
    page.close()


@pytest.fixture
def login_set_up(set_up):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("")
    # page.wait_for_load_state("networkidle")
    page = set_up
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill("test123")
    page.get_by_label("Password").press("Enter")

    yield page


def go_to_new_collection_page(page):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("/new-collection")
    page.wait_for_load_state("networkidle")

    yield page
