import time

from playwright.sync_api import Playwright, sync_playwright
# import pytest
from pom.contact_us_page import ContactUsPage


def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("Eliran", "123 Main st", "test@gmail.com", "123-549-8798", "test subject", "bla bla bla")


with sync_playwright() as playwright:
    test_submit_form(playwright)
