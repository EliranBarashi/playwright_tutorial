from playwright.sync_api import Playwright, sync_playwright, expect
from example_shop_women_elements import ShopWomen


def about_us_section_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    shop_women = ShopWomen(page)

    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()
    expect(shop_women.celebrating_beauty_hdr).to_be_visible()
    expect(shop_women.my_orders).to_be_hidden()
    expect(shop_women.profile_arrow).to_be_hidden()
    expect(shop_women.profile_icon).to_be_visible()
    expect(shop_women.cart_icon).to_be_hidden()
    expect(shop_women.my_orders_profile_box).to_be_hidden()

with sync_playwright() as playwright:
    about_us_section_verbiage(playwright)