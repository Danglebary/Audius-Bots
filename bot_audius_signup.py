# INIT CUSTOM IMPORTS
from config import (
    sign_up_url,
    sign_up_email_xPath,
    sign_up_email_continue_xPath,
    sign_up_password_one_xPath,
    sign_up_password_two_xPath,
    sign_up_button_xPath,
    sign_up_manual_button_xPath,
    sign_up_username_xPath,
    sign_up_handle_xPath,
    sign_up_continue_button_xPath,
    sign_up_choose_for_me_button_xPath,
    sign_up_submit_button_xPath,
)
from setup_browser import init_browser_headless
from browser_interaction_helper_funcs import (
    browser_navigate_and_wait,
    find_form_field_by_xpath_then_keystroke,
    find_button_by_xpath_and_click,
)

# FUNCTION TO CREATE AUDIUS ACCOUNT FOR BOT USING {bot_data}
def bot_sign_up(bot_data):
    # INIT BROWSER INSTANCE, AND DECONSTRUCT {bot_data} VARIABLES
    browser = init_browser_headless()
    user_name = bot_data[1]
    email = bot_data[4]
    password = bot_data[5]
    # TRY TO RETRIEVE AUDIUS SIGN UP PAGE IN BROWSER, OR HANDLE ERRORS
    browser_navigate_and_wait(browser, sign_up_url, user_name)
    # TRY TO FILL EMAIL FIELD OF SIGN UP FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(
        browser, sign_up_email_xPath, email, user_name, False
    )
    # TRY TO FIND CONTINUE BUTTON AND CLICK TO NAVIGATE TO NEXT PAGE, OR HANDLE ERRORS
    find_button_by_xpath_and_click(
        browser, sign_up_email_continue_xPath, user_name
    )
    # TRY TO FILL FIRST PASSWORD FIELD OF FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(
        browser, sign_up_password_one_xPath, password, user_name, False
    )
    # TRY TO FILL SECOND PASSWORD FIELD OF FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(
        browser, sign_up_password_two_xPath, password, user_name, False
    )
    # TRY TO FIND SIGN UP BUTTON TO CONTINUE SIGN UP PROCESS, OR HANDLE ERRORS
    find_button_by_xpath_and_click(browser, sign_up_button_xPath, user_name)
    # TRY TO FILL OUT USER ACCOUNT DATA, OR HANDLE ERRORS
    find_button_by_xpath_and_click(
        browser, sign_up_manual_button_xPath, user_name
    )
    # TRY TO FILL USERNAME FIELD OF FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(
        browser, sign_up_username_xPath, user_name, user_name, False
    )
    # TRY TO FILL HANDLE FIELD OF FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(
        browser, sign_up_handle_xPath, user_name, user_name, False
    )
    # TRY TO FIND AND CLICK CONTINUE BUTTON, OR HANDLE ERRORS
    find_button_by_xpath_and_click(
        browser, sign_up_continue_button_xPath, user_name
    )
    # TRY TO FIND AND CLICK "choose for me" BUTTON, OR HANDLE ERRORS
    find_button_by_xpath_and_click(
        browser, sign_up_choose_for_me_button_xPath, user_name
    )
    # TRY TO FIND AND CLICK SUBMIT BUTTON, OR HANDLE ERRORS
    find_button_by_xpath_and_click(
        browser, sign_up_submit_button_xPath, user_name
    )

    browser.quit()
