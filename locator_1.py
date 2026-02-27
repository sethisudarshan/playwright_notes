from playwright.sync_api import sync_playwright


with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
#    page.goto('https://playwright.dev/docs/intro')
#    page.goto('https://demo.automationtesting.in/Index.html')
    page.goto('https://www.facebook.com/')

#what are the type of locator in Playwright (9)

# 1.css selector
# 2.Text
# 3.Role
# 4.place holder
# 5.Label
# 6.Test ID
# 7.Xpath
# 8.Chaining locator
# 9.nth locator


# css selector - id - # , class - . , attribute - tagname[attribute ='value']
####----------------------------------------------------------------------
# #id using
    #
    # email_textbox=page.wait_for_selector('#email').type('sethi@123')
    #
    # button_login = page.wait_for_selector('#enterimg').click()
    #
    #
    # page.wait_for_timeout(3000)    #mili sec = 3 second
    # browser.close()

#attribute - tagname[attribute ='value']
    #
    # username = page.wait_for_selector('input[name="email"]').type('Tester')
    # password = page.wait_for_selector('input[name="pass"]').type('Tester2123')
    #
    # login_button = page.wait_for_selector('button[name="login"]').click()
    #
    # page.wait_for_timeout(5000)    #mili sec = 3 second
    # browser.close()

# XPATH
#------------
# 1.Absolute XPATH
# 2.Relative XPATH












