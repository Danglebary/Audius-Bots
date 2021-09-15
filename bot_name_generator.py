# GENERAL IMPORTS
from string import digits
from random import choice
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver

# CUSTOM IMPORTS
from config import (
    bot_quick_name_url,
    bot_quick_name_classname,
    bot_username_url,
    bot_username_search_button_xPath,
    bot_username_search_field_xPath,
)

# FUNCTION TO FETCH RANDOM FULL NAME FROM ONLINE NAME GENERATOR,
# AND RETURN FIRST AND LAST NAME
def fetch_name(browser: WebDriver) -> tuple[str, str]:
    browser.get(bot_quick_name_url)
    name_element = browser.find_element_by_class_name(bot_quick_name_classname)
    full_name: str = name_element.text
    full_name_split: list = full_name.split()
    first_name: str = full_name_split[0]
    last_name: str = full_name_split[1]
    return (first_name, last_name)


# FUNCTION TO FETCH RANDOM USERNAME FROM ONLINE USERNAME GENERATOR,
# AND RETURN USERNAME
def fetch_username(browser: WebDriver, first_name: str) -> str:
    browser.get(bot_username_url)
    search_box = browser.find_element_by_xpath(bot_username_search_field_xPath)
    search_box.click()
    search_box.send_keys(f"{first_name}")
    sleep(0.5)
    browser.find_element_by_xpath(bot_username_search_button_xPath).click()
    user_name: str = browser.find_element_by_xpath(
        f'//*[contains(@id, "{first_name}")]'
    ).text
    return user_name


# FUNCTION TO FETCH MULTIPLE USERNAMES FROM ONLINE USERNAME GENERATOR,
# JOINING RANDOM USERNAMES IN RANDOM ORDER,
# AND RETURN FINAL USERNAME
def create_user_name(browser: WebDriver, first_name: str) -> str:
    nDigits: int = 4
    user_name_raw: str = fetch_username(browser=browser, first_name=first_name)
    user_name_extras: str = digits
    user_name_extra_list: list[str] = []
    for _ in range(nDigits):
        user_name_extra_list.append(choice(user_name_extras))
    user_name_extra_string: str = "".join(user_name_extra_list)
    user_name_final: str = user_name_raw + user_name_extra_string
    return user_name_final
