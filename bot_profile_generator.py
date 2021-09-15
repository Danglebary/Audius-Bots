# General imports
from custom_types import BotData
from random import uniform
from selenium.webdriver.chrome.webdriver import WebDriver

# Custom imports
from bot_name_generator import fetch_name, create_user_name
from bot_password_generator import gen_bot_pass
from bot_birthday_generator import gen_birthdate
from setup_browser import init_browser_headless
from database import insert_new_bot_in_db

# Function to create email address for bot, from its {user_name}
def choose_email(user_name: str) -> str:
    email: str = ""
    randN: float = uniform(0.0, 1.0)
    if randN >= 0.5:
        email = f"{user_name}@outlook.com"
    else:
        email = f"{user_name}@hotmail.com"
    return email


# TODO: UPDATE TO REFLECT UPDATED DATABASE.PY FUNCTIONS.

# Function to generate any number of bot profiles
def gen_bot_data(nBots: int):
    browser: WebDriver = init_browser_headless()
    for _ in range(nBots):
        name_data: tuple[str, str] = fetch_name(browser=browser)
        first_name: str = name_data[0].lower()
        last_name: str = name_data[1].lower()
        user_name: str = create_user_name(
            browser=browser, user_name=first_name
        )
        password: str = gen_bot_pass()
        dob: str = gen_birthdate(max_age=30)
        email: str = choose_email(user_name=user_name)
        bot_data: list[str] = [
            user_name,
            first_name,
            last_name,
            email,
            password,
            dob,
        ]
        try:
            insert_new_bot_in_db(bot_data=bot_data)
            browser.quit()
        except Exception as e:
            print(e)
