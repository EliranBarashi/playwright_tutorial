from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


# in this example it tries to log in 3 times with different mails and passwords
@pytest.mark.parametrize("email, passwrd", [("symon.storozhenko@gmail.com", "test123"),
                                            pytest.param("fakeemail@gmail.com", "fakepassword", marks=pytest.mark.xfail),
                                            pytest.param("symon.storozhenko@gmail", "test123", marks=pytest.mark.xfail)])
def test_user_login(page, email, passwrd) -> None:
    page.set_default_timeout(3000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill(email)
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill(passwrd)
    page.get_by_label("Password").press("Enter")
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
