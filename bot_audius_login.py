# INIT GENERAL IMPORTS

import time, random

# INIT SELENIUM IMPORTS

from selenium.webdriver.common.keys import Keys

# INIT CUSTOM IMPORTS

from browser_interaction_helper_funcs import browser_navigate_and_wait, find_form_field_by_xpath_then_keystroke

# FUNCTION FOR BOT TO LOGIN TO AUDIUS ACCOUNT

def bot_login(browser, user_name, email, password):

    # TRY TO RETRIEVE AUDIUS LOGIN PAGE IN BROWSER, OR HANDLE ANY ERRORS
    browser_navigate_and_wait(browser, 'https://audius.co/signin', user_name)

    # TRY TO FILL EMAIL FIELD OF LOGIN FORM, OR HANDLE ANY ERRORS
    find_form_field_by_xpath_then_keystroke(browser, '//input[@name="email"]', user_name, user_name, False)
    
    # TRY TO FILL PASSWORD FIELD OF LOGIN PAGE, OR HANDLE ANY ERRORS
    find_form_field_by_xpath_then_keystroke(browser, '//input[@name="password"]', password, user_name, True)