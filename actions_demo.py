# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto('https://demo.automationtesting.in/Windows.html')

# ####..........mouse Actions.....####
# # mouse Hover
#     page.wait_for_selector('//a[text()="SwitchTo"]').hover()
#
# #click on element
#     page.wait_for_selector('//a[text()="SwitchTo"]').click()
#
# # double click
#     page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()
#
# #right click on element
#     page.wait_for_selector('//a[text()="SwitchTo"]').click(button='right')
#
# #sift + click
#     page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers=["shift"])
#
# ###...keyboard Actions
# ## A-Z , 0-9 , F1-F12 ,ALL SPECIAL CHARACTER ,ALL ARROW BOTTOMS , pageup ,Enter,Control ,Command
#     page.wait_for_selector('//a[text()="SwitchTo"]').press('A')
#     page.wait_for_selector('//a[text()="SwitchTo"]').press('@')
#
#
#
#
#
#
#     page.wait_for_timeout(2000)
#     browser.close()

####....................................... video no -10...............
##
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Windows.html')

#how to store multiple elements useing list
    elements = page.query_selector_all('a')
    print(len(elements))
# view all tags text
    for i in elements:
#        print(i.text_content())
        print(i.get_attribute('href'))

    page.wait_for_timeout(5000)
#    browser.close()
# how to read the text in the web elements



####...................exception handling













