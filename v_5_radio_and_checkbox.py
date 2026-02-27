#@@@@@@@@@@@@@@@@@@@@@@@...........Radio button and check box...............v.no.-5..............#######

#you can able to check only one button is called radio button
#you can able to check multiple button is called check box

# from playwright.sync_api import sync_playwright
#
#
# with sync_playwright() as play:
#     browser = play.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto('https://demo.automationtesting.in/Register.html') #pratice for dropdown purpose

#####1.Radio button
##=================

    # radio_button = page.query_selector('//input[@value="Male"]')

####click or check(same)
#    radio_button.click()
#     radio_button.check()
#
# #if statement
#     if radio_button.is_checked():
#         print('passed')
#     else:
#         print('failed')

####2.CHECK BOX
# ####===============
#     check_box = page.query_selector('//input[@value="Cricket"]')
#     check_box_2=page.query_selector('//input[@value="Movies"]')
#
# #click or check
# #    check_box.click()
#     check_box.check()
#     check_box_2.check()

# VALIDATION
# # if statement
#     if check_box.is_checked():
#         print('passed')
#     else:
#         print('failed')
#
#     page.wait_for_timeout(3000)    #mili sec = 3 sec
#     browser.close()

