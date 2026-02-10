###Here the described locators are
###
###.2.get_by_role()
###.3.get_by_label()
###.4.get_by_text()
###.5.get_by_placeholder()


from playwright.sync_api import sync_playwright  ## call the sync_playwright(webdriver)
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("file://D:/Project/TREENETRACLASSNOTES/TREENETRA_AT_23/playwright_prac/Locaters/other_Locaters.html")


####.2.get_by_role()......##(tag name,text)
## first find the tag name and text  , and it also need a parameter/keyword argument (name)
    submit=page.get_by_role("button", name = "submit")
    submit.click()
    print(submit.text_content())

###.3.get_by_label()....##(label tag) and put the text of the label tag name
    username=page.get_by_label("Username")
    username.fill("sudarshan")

    password =page.get_by_label("Password")
    password.fill("Sethi@123")

###.4.get_by_text()...###
    text1=page.get_by_text("Welcome to playwright automation pratice").is_visible()  ###  return true and false
    print(text1)
    page.get_by_text("Acept term and condition").click()

###.5.get_by_placeholder..##
    email= page.get_by_placeholder("Enter your email").fill("sudarshan@gmail.com")
    search =page.get_by_placeholder("search here").fill("email")

    time.sleep(5)
    browser.close()