# INIT CUSTOM IMPORTS
from config import track_repost_from_track_page_xPath
from database import (
    insert_new_reposted_track_in_db,
    query_reposted_track_ids_by_bot_id,
)

#!! MAKE SURE BOT IS ALREADY ON TRACK PAGE BEFORE CALLING THIS FUNCTION    !!
#!! OR MAKE SURE BOT IS ACTIVELY PLAYING THE TRACK THAT SHOULD BE REPOSTED !!
#!! ALSO MAKE SURE BOT HAS NOT ALREADY REPOSTED THIS SPECIFIC TRACK        !!

# FUNCTION TO CHECK IF BOT HAS ALREADY REPOSTED TRACK WITH {track_id}


def bot_check_reposted_tracks_in_db(bot_id, track_id):
    bot_reposts = query_reposted_track_ids_by_bot_id(bot_id)
    if bot_reposts:
        for reposted_track in bot_reposts:
            if track_id == reposted_track[1]:
                return True
            else:
                return False


# FUNCTION TO REPOST TRACK WITH {track_id} FROM TRACK PAGE


def bot_repost_track_on_track_page(browser, bot_id, track_id):
    bot_already_reposted = bot_check_reposted_tracks_in_db(bot_id, track_id)
    if bot_already_reposted == True:
        print(
            f"BOT REPOST TRACK ERROR : Bot {bot_id} has already reposted track {track_id}"
        )
    else:
        print(
            f"BOT REPOST TRACK : Bot {bot_id} has not already reposted track {track_id}"
        )
        try:
            repost_button = browser.find_element_by_xpath(
                track_repost_from_track_page_xPath
            )
            if repost_button:
                repost_button.click()
                print(
                    f"BOT REPOST TRACK : Bot {bot_id} has clicked repost button on track {track_id}"
                )
                try:
                    insert_new_reposted_track_in_db(bot_id, track_id)
                except Exception as e:
                    print(e)
            else:
                print(
                    f"BOT REPOST TRACK ERROR : Bot {bot_id} could not find repost button for track {track_id}"
                )
        except Exception as e:
            print(e)
