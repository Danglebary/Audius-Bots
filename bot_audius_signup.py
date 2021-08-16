# INIT GENERAL IMPORTS
import time, random

# INIT CUSTOM IMPORTS
from setup_browser import init_browser_headful, init_browser_headless
from browser_interaction_helper_funcs import browser_navigate_and_wait, find_form_field_by_xpath_then_keystroke, find_button_by_xpath_and_click

# URL AND XPATH VARIABLES
signup_url = 'https://audius.co/signup'
email_field_xPath = '//input[@type="email"]'
email_continue_xPath = '//button[@name="continue"]'
pass_one_field_xPath = '//input[@name="password"]'
pass_two_field_xPath = '//input[@name="confirmPassword"]'
sign_up_button_xPath = '//*[@id="page"]/div[2]/div[1]/form/div/div/button/span[1]'
manual_button_xPath = '//*[@id="page"]/div[2]/div[1]/form/div/div/div[3]/div[1]/div/div[3]'
username_field_xPath = '//input[@name="name"]'
handle_field_xPath = '//input[@name="nickname"]'
continue_button_xPath = '//button[@name="continue"]'
choose_for_me_button_xPath = '//*[@id="page"]/div[2]/div[1]/form/div/div/div[3]/div[1]/div[2]/div/div/div/div[1]/div'
submit_button_xPath = '//*[@id="page"]/div[2]/div[1]/form/div/div/button/span[1]'

# FUNCTION TO CREATE AUDIUS ACCOUNT FOR BOT USING {bot_data}
def bot_sign_up(bot_data):
    # INIT BROWSER INSTANCE, AND DECONSTRUCT {bot_data} VARIABLES
    browser = init_browser_headless()
    user_name = bot_data[1]
    email = bot_data[4]
    password = bot_data[5]
    # TRY TO RETRIEVE AUDIUS SIGN UP PAGE IN BROWSER, OR HANDLE ERRORS
    browser_navigate_and_wait(browser, signup_url, user_name)
    # TRY TO FILL EMAIL FIELD OF SIGN UP FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(browser, email_field_xPath, email, user_name, False)
    # TRY TO FIND CONTINUE BUTTON AND CLICK TO NAVIGATE TO NEXT PAGE, OR HANDLE ERRORS
    find_button_by_xpath_and_click(browser, email_continue_xPath, user_name)
    # TRY TO FILL FIRST PASSWORD FIELD OF FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(browser, pass_one_field_xPath, password, user_name, False)
    # TRY TO FILL SECOND PASSWORD FIELD OF FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(browser, pass_two_field_xPath, password, user_name, False)
    # TRY TO FIND SIGN UP BUTTON TO CONTINUE SIGN UP PROCESS, OR HANDLE ERRORS
    find_button_by_xpath_and_click(browser, sign_up_button_xPath, user_name)
    # TRY TO FILL OUT USER ACCOUNT DATA, OR HANDLE ERRORS
    find_button_by_xpath_and_click(browser, manual_button_xPath, user_name)
    # TRY TO FILL USERNAME FIELD OF FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(browser, username_field_xPath, user_name, user_name, False)
    # TRY TO FILL HANDLE FIELD OF FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(browser, handle_field_xPath, user_name, user_name, False)
    # TRY TO FIND AND CLICK CONTINUE BUTTON, OR HANDLE ERRORS
    find_button_by_xpath_and_click(browser, continue_button_xPath, user_name)
    # TRY TO FIND AND CLICK "choose for me" BUTTON, OR HANDLE ERRORS
    find_button_by_xpath_and_click(browser, choose_for_me_button_xPath, user_name)
    # TRY TO FIND AND CLICK SUBMIT BUTTON, OR HANDLE ERRORS
    find_button_by_xpath_and_click(browser, submit_button_xPath, user_name)

    browser.quit()