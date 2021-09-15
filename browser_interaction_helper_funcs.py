# General imports
from time import sleep
from random import uniform
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

# Custom imports
from error_handler import (
    handle_browser_navigation_error,
    handle_browser_element_xpath_keystroke_error,
    handle_browser_element_xpath_click_error,
)

# wait min/max variables (in seconds)
WAIT_NAVIGATE_MIN = 1.3
WAIT_NAVIGATE_MAX = 5.24

WAIT_KEYSTROKE_MIN = 0.1
WAIT_KEYSTROKE_MAX = 0.97

WAIT_TASK_MIN = 3.1
WAIT_TASK_MAX = 12.1

wait_enter = 20

# Try to navigate to url, then wait... or handle errors!
def browser_navigate_and_wait(
    browser: WebDriver, url: str, bot_user_name: str
) -> None:
    try:
        browser.get(url)
        print(f"{bot_user_name} : NAVIGATION - navigated to {url}")
        sleep(uniform(WAIT_NAVIGATE_MIN, WAIT_NAVIGATE_MAX))
    except Exception:
        error_data = url
        handle_browser_navigation_error(bot_user_name, error_data, 1)


# Try to find input element of form, click to focus form input element,
#   then input data... or handle errors!
def find_form_field_by_xpath_then_keystroke(
    browser: WebDriver, xPath: str, data: str, bot_user_name: str, enter: bool
):
    try:
        element = browser.find_element_by_xpath(xPath)
        if element:
            element.click()
            for char in data:
                element.send_keys(char)
                sleep(uniform(WAIT_KEYSTROKE_MIN, WAIT_KEYSTROKE_MAX))
            sleep(uniform(WAIT_TASK_MIN, WAIT_TASK_MAX))
            # Check to see if enter key should be clicked, and send Enter key if True
            if enter == True:
                element.send_keys(Keys.ENTER)
                sleep(20)
            print(
                f'{bot_user_name} : BROWSER - entered {data} into element with xPath "{xPath}"'
            )
        else:
            # Element could not be found or doesn't exist, raise error
            raise ValueError(f"element with xPath {xPath} could not be found")
    except (Exception, ValueError) as error:
        handle_browser_element_xpath_keystroke_error(bot_user_name, error, 1)


def find_button_by_xpath_and_click(browser, xPath, bot_name):
    try:
        browser.find_element_by_xpath(xPath).click()
        sleep(uniform(WAIT_TASK_MIN, WAIT_TASK_MAX))
    except Exception:
        error_data = f"element with xPath {xPath} could not be found, or could not be clicked"
        handle_browser_element_xpath_click_error(bot_name, error_data, 1)
