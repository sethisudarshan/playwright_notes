from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')

    ###..Wait Mecanism ........
    page.wait_for_timeout(3000) ### playwright Hard wait
    page.wait_for_selector()
    ##wait_for_selector
    ##wait_for_timeout
    ##wait_for_URL
    ##wait_for_event
    ##wait_for_function
    ##wait_for_load_state



    time.sleep(3)
    browser.close()