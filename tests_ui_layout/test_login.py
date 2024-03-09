from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.mark.smoke
def test_logged_user_can_view_my_orders_menu(login_set_up) -> None:
    page = login_set_up
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.wait_for_load_state("networkidle")
    # page.get_by_role("button", name="Log In").click()
    # page.get_by_test_id("signUp.switchToSignUp").click()
    # page.get_by_role("button", name="Log in with Email").click()
    # page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    # page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    # page.get_by_label("Password").fill("test123")
    # page.get_by_label("Password").press("Enter")
    # print("bla")

    # ---------------------
    # context.close()
    # browser.close()
    #
    #


