# from playwright.sync_api import sync_playwright
#
#
# with sync_playwright() as play:
#     browser = play.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto('https://demo.automationtesting.in/Register.html') #pratice for dropdown purpose

# # select drop down
# # 1.find the select location
#     select_dropdown = page.query_selector('//select[@id="Skills"]')
# # 2.select the option
#     select_dropdown.select_option(label='HTML')

#above are the process of selenium how to clock a drop down
#but playwrite make it simple like bellow and we give two parameter in one statement
    # page.select_option('//select[@id="Skills"]',label='HTML')
    # page.wait_for_timeout(5000)
    # browser.close()


#@@@@@@@@@@@@@@@@@@@@@@@...........Radio button and check box...............................#######

#you can able to check only one button is called radio button
#you can able to check multiple button is called check box

from playwright.sync_api import sync_playwright


with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html') #pratice for dropdown purpose
#Radio button

    radio_button = page.query_selector('//input[@value="FeMale"]')

#click and check
#    radio_button.click()
    radio_button.check()

#if statement
    if radio_button.is_checked():
        print('passed')
    else:
        print('failed')
####.............................................
#check box
    check_box = page.query_selector('//input[@value="Cricket"]')

#click and check
#    check_box.click()
    check_box.check()

# if statement
    if check_box.is_checked():
        print('passed')
    else:
        print('failed')

    page.wait_for_timeout(3000)    #mili sec = 3 sec
    browser.close()




















