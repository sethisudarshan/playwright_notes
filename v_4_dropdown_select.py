# from playwright.sync_api import sync_playwright
#
#
# with sync_playwright() as play:
#     browser = play.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto('https://demo.automationtesting.in/Register.html') #pratice for dropdown purpose

###Dropdown 2 types
##1.select Drop down  ##static dropdown
##2.Bootstrap Dropdown   ##Dynamic Dropdown

# # select drop down
# # 1.find the select location
#     select_dropdown = page.query_selector('//select[@id="Skills"]')
#
# # 2.select the option(select by option)
#     select_dropdown.select_option(label='Java')

###above are the process of selenium how to click a drop down     ^^

#### playwright....
####but playwrite make it simple like bellow and we give two parameter in one statement

    # page.select_option('//select[@id="Skills"]',label='Java')
    # page.wait_for_timeout(5000)
    # browser.close()






















