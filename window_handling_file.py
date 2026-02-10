# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto('https://demo.automationtesting.in/Windows.html')
###    page.wait_for_selector('//button[text()="    click   "]')
###    page.wait_for_selector('//div[@id="Tabbed"]/a/button')   #or means different xpath
    # page.wait_for_selector('//button[contains(text(),"    click   ")]').click()
    # page.wait_for_timeout(3000)

'''# #how to find the total pages
#     total_pages= context.pages    #context page return the list
#     print(len(total_pages))
#     for i in total_pages:
#         print(i)
#
#     print(page.title())
# #how to store the new page in the veriable
#     new_page = total_pages[1]
# #how to switch to new pages
#     new_page.bring_to_front()
#     page.wait_for_timeout(3000)
#     print(new_page.title())
#     new_page.close()        #close current tab
#     page.bring_to_front()   #comeback to parent tab
#     page.wait_for_timeout(3000)
#
#     browser.close()     #close all the browser
#
'''
# page vs context
#page can store only one page or tab
#context can store multiple tabs or pages in a list[]



#open new tab or pages switch
# move from parent page to child page called

##............................................................................................
##.......................managing cooking and screenshort.....................................
##............................................................................................
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.redbus.in/')
#    page.goto('https://www.facebook.com/')

# ###Give all the cookies
#     my_cookies = page.context.cookies()
#     print(my_cookies)
# ###clear all the cookies
#     page.context.clear_cookies()
#
# ## how can i insert sutten cookies
#     new_cookies ={
#         'name' : 'sudarshan sethi',
#         'udid' : '25455279'
#     }
#
# #    page.context.add_cookies([new_cookies])
#

###Takeing screenshort
    page.screenshot(path='test1.png')                  # it taking only browser
#    page.screenshot(path='test.png',full_page= True) #taking entire screen


















