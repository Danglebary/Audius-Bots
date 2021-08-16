# INIT GENERAL IMPORTS

import time, random

# INIT SELENIUM IMPORTS

from selenium.webdriver.common.keys import Keys

# INIT CUSTOM IMPORTS
from xpathconfig import *
from browser_interaction_helper_funcs import browser_navigate_and_wait, find_form_field_by_xpath_then_keystroke

# FUNCTION FOR BOT TO LOGIN TO AUDIUS ACCOUNT

def bot_login(browser, user_name, email, password):

    # TRY TO RETRIEVE AUDIUS LOGIN PAGE IN BROWSER, OR HANDLE ANY ERRORS
    browser_navigate_and_wait(browser, sign_in_url, user_name)

    # TRY TO FILL EMAIL FIELD OF LOGIN FORM, OR HANDLE ANY ERRORS
    find_form_field_by_xpath_then_keystroke(browser, sign_in_email_xPath, user_name, user_name, False)
    
    # TRY TO FILL PASSWORD FIELD OF LOGIN PAGE, OR HANDLE ANY ERRORS
    find_form_field_by_xpath_then_keystroke(browser, sign_in_password_xPath, password, user_name, True)