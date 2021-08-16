# INIT GENERAL IMPORTS
import time, random

# INIT CUSTOM IMPORTS
from setup_browser import init_browser_headless, init_browser_headful
from bot_audius_login import bot_login
from bot_stream import bot_stream_routine

# FUNCTIONS TO BE USED AS MAIN "brains" OR "loop" OF BOT LIFE CYCLE.

# ! SHOULD MAKE MORE ROUTINES, WITH DIFFERENT PATTERS,
# TO HELP MAKE THE BOT LOOK MORE LIFELIKE !

# THIS ROUTINE WAITS A RANDOM AMOUNT OF TIME TO BEGIN BOT WORK CYCLE,
# TO AVOID ALL BOTS SPINNING UP AT THE SAME TIME.
# NEXT, BOT WILL ATEMPT TO LOGIN
# IF SUCCESSFUL, BOT WILL NAVIGATE TO ITS OWN AUDIUS PROFILE 
# (AS A CLEAN PLACE TO START FROM EVERYTIME)
# THEN A STREAMING ROUTINE WILL BE CALLED,
# BOT WILL COMPLETE THE CHOSEN STREAMING ROUTINE,
# UPON COMPLETION, BOT WILL PRINT ITS USERNAME AND THE AMOUNT OF TIME IT WORKED THIS SESSION
# AND RETURN THE ELAPSED TIME

# ! PROPS FOR ROUTINE ARE STARMAPPED FROM main.py, 
#   SO ALL BOT PROFILE DATA IS UNPACKED, EVEN IF VARIABLES ARE UNUSED.

# ! HERE IS WHERE YOU ADD THE SPECIAL ARTISTS YOU WANT TO BE STREAMED MORE THAN OTHERS !
special_artists = []

def bot_routine_one(bot_id, user_name, first_name, last_name, email, password, dob):
    wait_before_startup = random.uniform(0.0, 1800.0)
    print(f'BOT_ROUTINE : Bot {user_name} will wait {wait_before_startup} second(s) before spinning up')
    time.sleep(wait_before_startup)
    start_time = time.perf_counter()
    browser = init_browser_headless()
    try:
        bot_login(browser, user_name, email, password)
        time.sleep(random.uniform(1.1, 2.3))
    except Exception as e:
        print(e)
    try:
        browser.get(f'https://audius.co/{user_name}')
        time.sleep(random.uniform(1, 2))
    except Exception as e:
        print(e)
    try:
        bot_stream_routine(browser, user_name, bot_id, special_artists)
    except Exception as e:
        print(e)
    browser.quit()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f'bot {user_name} ran for {elapsed_time} seconds')
    return elapsed_time
