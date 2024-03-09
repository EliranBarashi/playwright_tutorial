from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


# stack parametrize for better test dada coverage (in this example gives 9 different tests)
@pytest.mark.parametrize("email", ["symon.storozhenko@gmail.com",
                                   pytest.param("fakeemail@gmail.com", marks=pytest.mark.xfail),
                                   pytest.param("symon.storozhenko@gmail", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("passwrd", ["test123",
                                     pytest.param("fakepassword", marks=pytest.mark.xfail),
                                     pytest.param("tes123", marks=pytest.mark.xfail)])
def test_user_login_stack(page, email, passwrd) -> None:
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
