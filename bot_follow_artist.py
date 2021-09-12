# DISCLAIMER ! THIS FUNCTIONALITY IS NOT COMPLETE !

# INIT CUSTOM IMPORTS
from config import artist_follow_button_xPath
from database import (
    insert_bot_new_artist_follow_in_db,
    query_bot_following_artists_by_bot_id,
)

# CHECK TO SEE IF BOT ACCOUNT WITH {bot_id} IS FOLLOWING ARTIST WITH {artist_id}
# RETURN TRUE OR FALSE
def bot_check_follow_artists(bot_id, artist_id):
    bot_all_following = query_bot_following_artists_by_bot_id(bot_id)
    if bot_all_following:
        # FOLLOWING DATA FOR BOT WITH {bot_id} WAS FOUND
        for artist in bot_all_following:
            if artist_id == artist[0]:
                return True
            else:
                return False
    else:
        # FOLLOWING DATA FOR BOT WITH {bot_id} WAS NOT FOUND OR DOES NOT EXIST, HANDLE ERRORS
        print(
            f"BOT {bot_id} : could not retrieve list of accounts they follow"
        )


# TRY TO FOLLOW ARTIST WITH {artist_id} BY NAVIGATING TO THEIR AUDIUS PAGE
# AND CLICKING FOLLOW BUTTON
def bot_follow_artist_on_artist_page(browser, bot_id, artist_id):
    # FIRST CHECK TO SEE IF BOT WITH {bot_id} IS ALREADY FOLLOWING ARTIST WITH {artist_id}
    bot_already_followed = bot_check_follow_artists(bot_id, artist_id)
    if bot_already_followed == True:
        print(
            f"BOT CHECK ARTIST FOLLOW ERROR : Bot {bot_id} has already followed artist {artist_id}"
        )
    else:
        print(
            f"BOT CHECK ARTIST FOLLOW : Bot {bot_id} does not already follow artist {artist_id}"
        )
        # TRY TO FOLLOW ARTIST WITH {artist_id}, OR HANDLE ERRORS
        try:
            follow_button = browser.find_element_by_xpath(
                artist_follow_button_xPath
            )
            if follow_button:
                # FOLLOW BUTTON FOUND, CLICK TO FOLLOW ARTIST
                follow_button.click()
                print(
                    f"BOT FOLLOW ARTIST : Bot {bot_id} has clicked follow button for artist {artist_id}"
                )
                # FOLLOW BUTTON CLICKED, TRY TO INSERT NEW ENTRY FOR ARTIST IN BOT
                # FOLLOWING LIST IN DB
                try:
                    insert_bot_new_artist_follow_in_db(bot_id, artist_id)
                except Exception as e:
                    # COULD NOT INSERT NEW ENTRY FOR ARTIST IN FOLLOWING LIST, HANDLE ERRORS
                    print(e)
            else:
                print(
                    f"BOT FOLLOW ARTIST ERROR : Bot {bot_id} could not find follow button for artist {artist_id}"
                )
        except Exception as e:
            # BOT WAS NOT ABLE TO FOLLOW ARTIST, OR ARTIST ALREADY FOLLOWED, HANDLE ERRORS
            print(e)
