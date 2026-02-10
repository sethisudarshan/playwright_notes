from playwright.sync_api import sync_playwright         ## like selenium driver

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
#    page.goto('https://playwright.dev/docs/intro')
    page.goto('https://www.facebook.com/')

    print('playwright first program and chrome successfully opened through playwright')
    print(page.title())
    page.wait_for_timeout(3000)    #mili sec = 3 sec
    browser.close()


##--   PLAYWRIGHT classes ----##
### --sir class--##
### MVT = Model View  Templet
### M= Database
### V=backend
### T=frontend
