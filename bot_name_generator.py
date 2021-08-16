# INIT GENERAL IMPORTS
import time, string, random

# INIT CUSTOM IMPORTS
from config import *

# FUNCTION TO FETCH RANDOM FULL NAME FROM ONLINE NAME GENERATOR,
# AND RETURN FIRST AND LAST NAME
def fetch_name(browser):
    browser.get(bot_quick_name_url)
    name_element = browser.find_element_by_class_name(bot_quick_name_classname)
    full_name = name_element.text
    full_name_split = full_name.split()
    first_name = full_name_split[0]
    last_name = full_name_split[1]
    return (first_name, last_name)

# FUNCTION TO FETCH RANDOM USERNAME FROM ONLINE USERNAME GENERATOR,
# AND RETURN USERNAME
def fetch_username(browser, name):
    browser.get(bot_username_url)
    search_box = browser.find_element_by_xpath(bot_username_search_field_xPath)
    search_box.click()
    search_box.send_keys(f'{name}')
    time.sleep(0.5)
    browser.find_element_by_xpath(bot_username_search_button_xPath).click()
    user_name = browser.find_element_by_xpath(f'//*[contains(@id, "{name}")]').text
    return user_name

# FUNCTION TO FETCH MULTIPLE USERNAMES FROM ONLINE USERNAME GENERATOR,
# JOINING RANDOM USERNAMES IN RANDOM ORDER,
# AND RETURN FINAL USERNAME
def create_user_name(browser, user_name):
    nDigits = 4
    user_name_raw = fetch_username(browser, user_name)
    user_name_extras = string.digits
    user_name_extra_list = []
    for _ in range(nDigits):
        user_name_extra_list.append(random.choice(user_name_extras))
    user_name_extra_string = ''.join(user_name_extra_list)
    user_name_final = user_name_raw + user_name_extra_string
    return user_name_final