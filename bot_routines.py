# General imports
from time import sleep, perf_counter
from random import uniform, randint

from selenium.webdriver.chrome.webdriver import WebDriver

# Custom imports
from setup_browser import init_browser_headful, init_browser_headless
from bot_audius_login import bot_login
from bot_stream import bot_stream_routine

# Functions to be used as main "brains" or "loop" of bot life cycle.

# ! Should make more routines with different patterns !

# This routine waits a random amount of time to begin bot work cycle,
#   to avoid all bots spinning up at the same time.
# Next, bot will attempt to login.
# If successful, bot will navigate to its own Audius profile url,
#   as a clean place to start from everytime.
# Then, a streaming routine will be chosen,
#   bot will compltete streaming routine, and upon completion,
#   bot will print its username and the time it worked this session
#   returning the elapsed time

# ! Args for routine are starmapped from main.py,
#   meaning all BotData is unpacked, even if args values are not used !


def bot_routine_one(
    bot_id: int,
    user_name: str,
    first_name: str,
    last_name: str,
    email: str,
    password: str,
    dob: str,
):
    wait_before_startup: float = randint(0, 40)
    print(
        f"BOT_ROUTINE : Bot {user_name} will wait {wait_before_startup} second(s) before spinning up"
    )
    sleep(wait_before_startup)
    start_time: float = perf_counter()
    browser: WebDriver = init_browser_headless()
    try:
        bot_login(
            browser=browser,
            bot_user_name=user_name,
            email=email,
            password=password,
        )
        sleep(uniform(1.1, 2.3))
    except Exception as e:
        print(e)
    try:
        browser.get(f"https://audius.co/{user_name}")
        sleep(uniform(1, 2))
    except Exception as e:
        print(e)
    try:
        bot_stream_routine(browser=browser, user_name=user_name)
    except Exception as e:
        print(e)
    browser.quit()
    end_time: float = perf_counter()
    elapsed_time: float = end_time - start_time
    print(f"bot {user_name} ran for {elapsed_time} seconds")
    return elapsed_time
