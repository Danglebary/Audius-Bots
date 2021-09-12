# INIT GENERAL IMPORTS
import random

# INIT CUSTOM IMPORTS
from bot_name_generator import fetch_name, create_user_name
from bot_password_generator import gen_bot_pass
from bot_birthday_generator import gen_birthdate
from setup_browser import init_browser_headless
from database import insert_new_bot_in_db

# FUNCTION TO CREATE EMAIL ADDRESS FOR BOT FROM ITS {user_name}
def choose_email(user_name):
    email = ""
    randN = random.uniform(0.0, 1.0)
    if randN >= 0.5:
        email = f"{user_name}@outlook.com"
    else:
        email = f"{user_name}@hotmail.com"
    return email


# FUNCTION TO GENERATE ANY NUMBER OF BOT PROFILES RANDOMLY
def gen_bot_data(nBots):
    # INIT BROWSER INSTANCE
    browser = init_browser_headless()
    # FETCH AND CREATE BOT PROFILE DATA FOR {nBots}
    for x in range(nBots):
        name_data = fetch_name(browser)
        first_name = name_data[0].lower()
        last_name = name_data[1].lower()
        user_name = create_user_name(browser, first_name)
        password = gen_bot_pass()
        dob = gen_birthdate(30)
        email = choose_email(user_name)
        bot_data = [user_name, first_name, last_name, email, password, dob]

        print(bot_data)
        # TRY TO INSERT NEW BOT PROFILE INTO DB, OR HANDLE ERRORS
        try:
            insert_new_bot_in_db(bot_data)
            # NEW BOT PROFILE HAS BEEN INSERTED INTO DB, EXIT BROWSER
            print(f"bot number {x} successfully written to db")
            browser.quit()
        except Exception as e:
            # NEW BOT PROFILE COULD NOT BE INSERTED INTO DB, HANDLE ERROR
            print(e)
