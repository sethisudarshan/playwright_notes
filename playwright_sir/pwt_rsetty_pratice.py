
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
##    page.set_viewport_size({"width":1920,"height":1080})      ## Maximize the windows
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

# ##by css
#     name=page.locator('#name')
#     name.fill("sagar das")
#     time.sleep(2)
#
# ##by xpath
#     name_1 = page.locator('//input[@name="enter-name"]')
#     name_1.fill("pintu")
#     time.sleep(2)
#
# ##by get_by_placeholder
#     name_2 = page.get_by_placeholder('Enter Your Name')
#     name_2.fill("sudarshan sethi")
#     time.sleep(2)
#
# ##by get_by_placeholder
#     name_3 = page.get_by_placeholder('Enter Your Name')
#     name_3.fill("RAM")
#
# #######.click the check box_option_2
#     check_box_click = page.locator("input[value='option2']")
#     check_box_click.click()
#     time.sleep(1)
#
# #######.click the check box_option_1
#     check_box_click_1 = page.locator("input[value='option1']")
#     check_box_click_1.click()
#     time.sleep(1)
#
# #######.click the check box_option_3
#     check_box_click_2 = page.locator("input[value='option3']")
#     check_box_click_2.click()

#####..Drop-down click
    # drpd_click = page.locator("#dropdown-class-example")
    # # drpd_click.click()
    # drpd_click.select_option("Option1")

####..Radio bottom click..##
    # page.locator('input[class="radioButton"]').nth(1).click()
    # page.locator('input[class="radioButton"]').nth(2).click()
###..xpath..
    # page.locator("(//input[@class='radioButton'])[2]").click()

###


    time.sleep(5)
    browser.close()