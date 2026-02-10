from playwright.sync_api import sync_playwright  ## call the sync_playwright(webdriver)
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

# #####.6.locator(id/name).....##
#     email = page.locator("#email").fill('sudarshan@123')
#     password = page.locator("#pass").fill("Sethi@123")          ### fill the feild
#     login = page.locator("#loginbutton").click()

####.7.locator(XPATH)...###
    motorola=page.locator("//div[text()='realme P4x 5G (Lake Green, 128 GB)']").click()



####.8.locator(CSS)...###
    motorola=page.locator("#email").fill("sudarshan")



###.9.get_by_title()..##

    time.sleep(5)

    browser.close()