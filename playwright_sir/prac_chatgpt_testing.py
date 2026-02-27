from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://chatgpt.com/")

###just login part
    # page.get_by_text("Log in").click()
    # page.get_by_text("Continue with Google").click()

    page.get_by_placeholder("Ask anything").fill("Hii AI i want to test you")




    time.sleep(5)
    browser.close()

### https://empmission.odisha.gov.in/Exchange/