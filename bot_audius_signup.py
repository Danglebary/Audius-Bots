# General imports
from selenium.webdriver.chrome.webdriver import WebDriver

# Custom imports
from custom_types import BotData
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

# Function to create Audius account for bot using {bot_data}
def bot_sign_up(bot_data: BotData):
    browser: WebDriver = init_browser_headless()
    bot_user_name = bot_data[1]
    bot_email = bot_data[4]
    bot_password = bot_data[5]
    browser_navigate_and_wait(
        browser=browser, url=sign_up_url, bot_user_name=bot_user_name
    )
    # TRY TO FILL EMAIL FIELD OF SIGN UP FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(
        browser=browser,
        xpath=sign_up_email_xPath,
        data=bot_email,
        bot_user_name=bot_user_name,
        enter=False,
    )
    # TRY TO FIND CONTINUE BUTTON AND CLICK TO NAVIGATE TO NEXT PAGE, OR HANDLE ERRORS
    find_button_by_xpath_and_click(
        browser, sign_up_email_continue_xPath, bot_user_name
    )
    # TRY TO FILL FIRST PASSWORD FIELD OF FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(
        browser, sign_up_password_one_xPath, bot_password, bot_user_name, False
    )
    # TRY TO FILL SECOND PASSWORD FIELD OF FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(
        browser, sign_up_password_two_xPath, bot_password, bot_user_name, False
    )
    # TRY TO FIND SIGN UP BUTTON TO CONTINUE SIGN UP PROCESS, OR HANDLE ERRORS
    find_button_by_xpath_and_click(
        browser, sign_up_button_xPath, bot_user_name
    )
    # TRY TO FILL OUT USER ACCOUNT DATA, OR HANDLE ERRORS
    find_button_by_xpath_and_click(
        browser, sign_up_manual_button_xPath, bot_user_name
    )
    # TRY TO FILL USERNAME FIELD OF FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(
        browser, sign_up_username_xPath, bot_user_name, bot_user_name, False
    )
    # TRY TO FILL HANDLE FIELD OF FORM, OR HANDLE ERRORS
    find_form_field_by_xpath_then_keystroke(
        browser, sign_up_handle_xPath, bot_user_name, bot_user_name, False
    )
    # TRY TO FIND AND CLICK CONTINUE BUTTON, OR HANDLE ERRORS
    find_button_by_xpath_and_click(
        browser, sign_up_continue_button_xPath, bot_user_name
    )
    # TRY TO FIND AND CLICK "choose for me" BUTTON, OR HANDLE ERRORS
    find_button_by_xpath_and_click(
        browser, sign_up_choose_for_me_button_xPath, bot_user_name
    )
    # TRY TO FIND AND CLICK SUBMIT BUTTON, OR HANDLE ERRORS
    find_button_by_xpath_and_click(
        browser, sign_up_submit_button_xPath, bot_user_name
    )

    browser.quit()
