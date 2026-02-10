from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.facebook.com/')
    page.goto('https://demo.automationtesting.in/Register.html') #another website for pratices


#...................XPATH............................
# use for traverse between the xpath
# it is easy to travel backwark and forward
# ------------
# 1.Absolute XPATH
# ## 2.Relative XPATH -//-- using attribute
# ..FORMULA.//tagname[@attributename="value"]
#
#     username_element = page.wait_for_selector('//input[@name="email"]').type('sethi@123')
#     password_element = page.wait_for_selector('//input[@name="pass"]').type('password@12')
#     login_element = page.wait_for_selector('//button[@name="login"]').click()
#     print('login successfully')
#
#     page.wait_for_timeout(5000)
#     browser.close()
#
# Text method
# ... //tagname[text()='text_value']

    forgot_password = page.wait_for_selector("//font[text()='Forgot password?']").click()
    page.wait_for_timeout(3000)
    browser.close()

#..contain()

#contain with attributes - //tagname[contains(@attribute,'value')]
#contain with text - //tagname[contains(text(),'forgot your')]

#Dynamic xpath - sudarshan1234 , sudarshan567 , sudarshan998
#starts-with - //tagname[starts-with(@id,'sudarshan')]
#ends-with  - //tagname[ends-with(@id,'1234')]

#family - Axes

# parent - //tagname[@id='xy']/parent::input[]
# child - //tagname[@id='xy']/child::input[]
# ancestor - //tagname[@attribute='value']/ancestor::tagname
#sibling
#preceding-sibling = //tagname[@attribute='value']/preceding-sibling::tag[4]
#following-sibling = //tagname[@attribute= 'value']/following-sibling::tag[2]











