###playwright link given by krishna sir
##### https://drive.google.com/drive/folders/1R3FqvXk6gFQClqcmQmZ0aGIQRRuIuMzy?usp=drive_link

##import playwright's synchrounous api
##sync_playwright() manage browser life cycle
#
# from playwright.sync_api import sync_playwright         ##sync_playwright its like selenium web driver and it makeing in node js
#
# ##with help of with statement open the context manager of playwright
#
# with sync_playwright() as p:      #### due to context manager we use with keyword to call sync_playwright
#     ###lunch the broswer /crome/safari
#     browser = p.chromium.launch(headless=False) ### (headless = false - it showing the screen//and working with DOM not in head) ##call the crome
#     '''when you opan a browser in selenium its open automatically open the first page but
#     in playwright its not able to open the first page  so we create a variable and open the page'''
#     page = browser.new_page()   ##open a new page in your recomned browser
#
#     ###open a link and hit in api and call the URL
#     page.goto("facebook.com")
#
#     browser.close()         ##close the browser
#


###.....Again wrighting the same code............############

# from playwright.sync_api import sync_playwright  ## call the sync_playwright(webdriver)
#
# with sync_playwright() as p:                     ##because of context manager use with
#     browser = p.chromium.launch(headless=False)  ##lunch the browser
#     page = browser.new_page()                    ##open a page
#     page.goto("https facebook.com")              ##open the url or link
#     browser.close()                              ## close the browser
#

####...selenium first program lets compair each other...####

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_object = Service('C:\\chromrdriver\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://www.freejobalert.com/') #opening url/heat url
time.sleep(5)
driver.quit()
'''
#
#### PLAYWRIGHT LOCATORS
#### =============================
####
###.1. get_by_text_id()
###.2. get_by_role()
###.3. get_by_label()
###.4. get_by_text()
###.5. get_by_placeholder()
###---
###.6. locator(id,name)
##---
###.7. locator(xpath)
###.8. locator(css)
###.9. get_by_title()###


#####==========...............Main Program.......................===============#################

from playwright.sync_api import sync_playwright  ## call the sync_playwright(webdriver)
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https facebook.com")

#####.6.locator(id/name).....##
    email = page.locator("#email").fill('sudarshan@123')
    password = page.locator("#pass").fill("Sethi@123")          ### fill the feild
    login = page.locator("#loginbutton").click()

#####.1. get_by_test_id.....##
    ##which attribute is data-testid we can find its path
    page.get_by_test_id("101").click()                 ##click the web element
    page.get_by_test_id("101").text_content()       ##print the text

#######----------------------------------------------------------------------------------
####.2.get_by_role()......##(tag name,text)
    ## first find the tag name and text  , and it also need a parameter/keyword argument (name)
    page.get_by_role("button", name = "Open Windows")


####.3.get_by_label()....##
    ##..checkbox with label "Option1"
    page.get_by_label("Option1").check()

####.4.get_by_text()...###
    page.get_by_text("Radio Button Example").click()

####.5.get_by_placeholder()...##
    page.get_by_placeholder("Type to select Countries").fill("india")

####.6.Locator(id,name)..###
    page.locator("#CheckBoxOption2").check()
    page.locator("[name='radioButton']").first.check()

    time.sleep(5)

    browser.close()
####==================

#####==========...................Main Program.......................===============#################
#
# from playwright.sync_api import sync_playwright  ## call the sync_playwright(webdriver)
# import time
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https facebook.com")
#
#     #####.0.locator(id/name).....##
#     email = page.locator("#email").fill('sudarshan@123')
#     password = page.locator("#pass").fill("Sethi@123")  ### fill the feild
#     login = page.locator("#loginbutton").click()
#
#     #####.1. get_by_test_id.....##
#     page.get_by_test_id("101").click()  ##click the web element
#     page.get_by_test_id("101").text_content()  ##print the text
#
#     ####.2.get_by_role()......##
#     page.get_by_role("button", name="Open Windows").click()
#
#     ####.3.get_by_label()....##
#     ##..checkbox with label "Option1"
#     page.get_by_label("Option1").check()
#
#     ####.4.get_by_text()...###
#     page.get_by_text("Radio Button Example").click()
#
#     ####.5.get_by_placeholder()...##
#     page.get_by_placeholder("Type to select Countries").fill("india")
#
#     ####.6.Locator(id,name)..###
#     page.locator("#CheckBoxOption2").check()
#     page.locator("[name='radioButton']").first.check()
#
#     time.sleep(5)
#
#     browser.close()
#

