from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https')

    ###..Wait Mecanism ........
    # page.wait_for_timeout(3000) ### playwright Hard wait
    # page.wait_for_selector()
    ##wait_for_selector
    ##wait_for_timeout
    ##wait_for_URL
    ##wait_for_event
    ##wait_for_function
    ##wait_for_load_state

    ###print the title
    # print(page.title())

###.From of input box..##
    ##type -1
    first_name = page.locator('#fname')
    first_name.fill('sudarshan')

    ##type -2

    page.fill('#fname','sudarshan')
    page.fill('#email','sudarshan@123')

###.click radio bottom..###
    # page.locator("input[name='gender']").nth(1).click()  ##go to end element using(.nth(index))
    # page.locator("//input[@name ='gender'][1]").click()
####---xpath
    # page.locator('//input[@name="gender"][1]').click()

##--input box but mobile number max lenght 10number
    # page.fill('#mobile', "7205375180")

##--calander
    page.fill("input[type='date']",'01-03-1998')



    time.sleep(3)
    browser.close()