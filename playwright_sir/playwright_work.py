from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')

    ###..Wait Mecanism ........
    page.wait_for_timeout(3000) ### playwright Hard wait
    page.wait_for_selector()


    time.sleep(3)
    browser.close()