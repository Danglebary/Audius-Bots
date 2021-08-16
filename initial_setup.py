# THIS FILE IS USED TO CREATE TABLES AND POPULATE THE DATABASE,
# SO THAT YOU CAN BEGIN USING THE PROGRAM.

# FIRST, YOU MUST HAVE SQLITE3 INSTALLED,
# AND THEN CREATE A DATABASE IN THIS DIRECTORY CALLED "data.db".

# EMAIL ACCOUNTS DO NOT ACTUALLY NEED TO BE CREATED.
# THERE IS NO EMAIL VERIFICATION STEP TO THE ACCOUNT CREATION,
# ONCE BOT DATA HAS BEEN CREATED AND ADDED TO DB, YOU ARE GOOD TO GO.

# AFTER THIS FILE HAS BEEN RAN, YOU CAN GO AHEAD AND RUN "main.py".

# DISCLAIMER : 
# IF ANYTHING IS MOST LIKELY TO FAIL OR ERROR IN THE MAIN
# PROCESS, IT WILL BE XPATH LOCATIONS FOR FORM FIELDS AND BUTTONS.
# THEY WILL LIKELY CHANGE UPON NEW UI UPDATES TO THE SITE, 
# AND WILL MOST LIKELY TAKE A BIT OF UPKEEP.
# THE FILE "config.py" HOLDS ALL OF THESE VARIABLES,
# AS A SINGLE PLACE TO UPDATE THEM INSTEAD OF HAVING TO LOOK FOR THEM.

# INIT CUSTOM IMPORTS
from config import init_nBots, init_extra_artists, special_artists
from database import create_all_db_tables
from bot_profile_generator import gen_bot_data
from sync_db_data import fetch_and_insert_new_artist_by_username, sync_db_tracks_for_all_artists

def first_setup():
    # CREATE DB TABLES
    create_all_db_tables()
    # CREATE AND ADD BOT DATAS TO DB
    gen_bot_data(init_nBots)
    # ADD ARTISTS AND THEIR DATAS TO DB
    for artist in init_extra_artists:
        fetch_and_insert_new_artist_by_username(artist)
    # ADD SPECIAL ARTISTS AND THEIR DATAS TO DB
    for artist in special_artists:
        fetch_and_insert_new_artist_by_username(artist)
    # FETCH AND ADD TRACKS AND TRACK DATAS TO DB
    sync_db_tracks_for_all_artists()

first_setup()