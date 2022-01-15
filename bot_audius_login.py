# General imports
from selenium.webdriver.chrome.webdriver import WebDriver

# Custom imports
from config import sign_in_url, sign_in_email_xPath, sign_in_password_xPath
from browser_interaction_helper_funcs import (
    browser_navigate_and_wait,
    find_form_field_by_xpath_then_keystroke,
)

# Function for bot to login to Audius account


def bot_login(
    browser: WebDriver, bot_user_name: str, email: str, password: str
):
    browser_navigate_and_wait(
        browser=browser, url=sign_in_url, bot_user_name=bot_user_name
    )

    find_form_field_by_xpath_then_keystroke(
        browser=browser,
        xPath=sign_in_email_xPath,
        data=email,
        bot_user_name=bot_user_name,
        enter=False,
    )

    find_form_field_by_xpath_then_keystroke(
        browser=browser,
        xPath=sign_in_password_xPath,
        data=password,
        bot_user_name=bot_user_name,
        enter=True,
    )
