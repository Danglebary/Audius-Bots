# INIT GENERAL IMPORTS
import time, random

# INIT CUSTOM IMPORTS
from error_handler import handle_browser_navigation_error, handle_browser_element_xpath_keystroke_error, handle_browser_element_xpath_click_error

# INIT SELENIUM IMPORTS
from selenium.webdriver.common.keys import Keys

# INIT WAIT MIN AND MAX VARIABLES (in seconds)
wait_navigate_min = 1.3
wait_navigate_max = 5.24

wait_keystroke_min = 0.1
wait_keystroke_max = 0.97

wait_task_min = 3.1
wait_task_max = 12.1

wait_enter = 20

# TRY TO NAVIGATE TO URL, THEN WAIT... OR HANDLE ERRORS
def browser_navigate_and_wait(browser, url, bot_name):
    # TRY TO NAVIGATE TO URL, THEN WAIT
    try:
        browser.get(url)
        print(f'{bot_name} : NAVIGATION - navigated to {url}')
        time.sleep(random.uniform(1.3, 4.6))
    except Exception:
        # HANDLE ERROR
        error_data = url
        handle_browser_navigation_error(bot_name, error_data, 1)

# TRY TO FIND ELEMENT OF FORM, CLICK, THEN INPUT DATA... OR HANDLE ERRORS
def find_form_field_by_xpath_then_keystroke(browser, xPath, data, bot_name, enter):
    try:
        element = browser.find_element_by_xpath(xPath)
        if element:
            # ELEMENT FOUND, CLICK TO SET ACTIVE
            element.click()
            for x in data:
                element.send_keys(x) 
                # KEY STROKE COMPLETE, WAIT BEFORE NEXT KEY STROKE
                time.sleep(random.uniform(wait_keystroke_min, wait_keystroke_max))           
            # DATA ENTERED INTO ELEMENT SUCCESSFULLY, WAIT BEFORE NEXT TASK
            time.sleep(random.uniform(wait_task_min, wait_task_max)) 
            # CHECK TO SEE IF ENTER KEY SHOULD BE PRESSED, IF TRUE, PRESS ENETER
            if enter == True:
                element.send_keys(Keys.ENTER)
                time.sleep(20)
            print(f'{bot_name} : BROWSER - entered {data} into element with xPath "{xPath}"')  
        else:
            # ELEMENT COULD NOT BE FOUND OR DOESN'T EXIST, RAISE ERROR
            raise ValueError(f'element with xPath {xPath} could not be found')
    except (Exception, ValueError) as error:
        # HANDLE ERRORS
        handle_browser_element_xpath_keystroke_error(bot_name, error, 1)

def find_button_by_xpath_and_click(browser, xPath, bot_name):
    try:
        browser.find_element_by_xpath(xPath).click()
        # ELEMENT FOUND AND CLICKED, WAIT BEFORE NEXT TASK
        time.sleep(random.uniform(wait_task_min, wait_task_max))
    except Exception:
        # HANDLE ERRORS
        error_data = f'element with xPath {xPath} could not be found, or could not be clicked'
        handle_browser_element_xpath_click_error(bot_name, error_data, 1)
