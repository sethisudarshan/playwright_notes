## selenium -alert
## playwright - dialog
##playwright automatically handles the alert but selenium not

from playwright.sync_api import sync_playwright


with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')

####.........................1..click only............................(ok)
####playwright automatically handles the alert means automatically click on (OK) button
    # page.wait_for_selector('//div[@id="OKTab"]/button').click()
    #
    # page.wait_for_timeout(5000)    #mili sec = 3 sec
    # browser.close()


####........................2..click cancel and ok................... (alert)
    # page.wait_for_selector('//a[@href="#CancelTab"]').click()
    # page.wait_for_timeout(2000)
    # page.wait_for_selector('//button[text()="click the button to display a confirm box "]').click()
# system automatically click so this is not a proper way so  bellow is the proper way

##control alert action
#     page.wait_for_selector('//a[@href="#CancelTab"]').click()
#     page.wait_for_timeout(2000)
#     page.on('dialog',lambda dialog:dialog.accept())
# #    page.on('dialog', lambda a: a.dismiss())
#     page.wait_for_selector('//button[text()="click the button to display a confirm box "]').click()
#     page.wait_for_timeout(5000)    #mili sec = 3 sec
#     browser.close()

#...print the messege which inside the alert
# from playwright.sync_api import sync_playwright
# text_alert =[]
#
#
# def handle_dialog(dialog):
#     message = dialog.message
#     text_alert.append(message)
#     dialog.accept()
#
#
# with sync_playwright() as play:
#     browser = play.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto('https://demo.automationtesting.in/Alerts.html')
#
#
#     page.wait_for_selector('//a[@href="#CancelTab"]').click()
#     page.on('dialog', handle_dialog)
#     page.wait_for_selector('//div[@id="CancelTab"]/button').click()
#     page.wait_for_timeout(2000)    #mili sec = 3 sec
#     browser.close()
#     print(text_alert[0])
#


####......................3.. alert  with text message......................................####
# from playwright.sync_api import sync_playwright
#
# text_alert =[]
#
# def handle_dialog(dialog):
#     message = dialog.type
#     text_alert.append(message)
#     dialog.accept()
#
# with sync_playwright() as play:
#     browser = play.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto('https://demo.automationtesting.in/Alerts.html')
#
#
#     page.wait_for_selector('//a[@href="#Textbox"]').click()
#     page.on('dialog', handle_dialog)
#     page.wait_for_selector('//div[@id="Textbox"]/button').click()
#     page.wait_for_timeout(2000)    #mili sec = 3 sec
#     browser.close()
#     print(text_alert[0])

