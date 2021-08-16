import time, random

from database import insert_new_liked_track_in_db, query_liked_track_ids_by_bot_id

#!! MAKE SURE BOT IS ALREADY ON TRACK PAGE BEFORE CALLING THIS FUNCTION !!
#!! OR MAKE SURE BOT IS ACTIVELY PLAYING THE TRACK THAT SHOULD BE LIKED !!
#!! ALSO MAKE SURE BOT HAS NOT ALREADY LIKED THIS SPECIFIC TRACK        !!

def bot_check_liked_track_in_db(bot_id, track_id):
    bot_likes = query_liked_track_ids_by_bot_id(bot_id)
    if bot_likes:
        for liked_track in bot_likes:
            if track_id == liked_track[1]:
                return True
            else:
                return False

def bot_like_currently_playing_track(browser, bot_id, track_id):
    bot_already_liked = bot_check_liked_track_in_db(bot_id, track_id)
    if bot_already_liked == True:
        print(f'BOT LIKE TRACK ERROR : Bot {bot_id} has already liked track {track_id}')
    else:
        print(f'BOT LIKE TRACK : Bot {bot_id} has not already liked track {track_id}')
        try:
            time.sleep(random.uniform(0.5, 1))
            like_button = browser.find_element_by_xpath('//*[@id="root"]/div/div[5]/div[2]/div/div[3]/div[1]/span/div')
            if like_button:
                like_button.click()
                print(f'BOT LIKE TRACK : Bot {bot_id} has clicked like button on track {track_id}')
                try:
                    insert_new_liked_track_in_db(bot_id, track_id)
                except Exception as e:
                    print(e)
            else:
                print(f'BOT LIKE TRACK ERROR : Bot {bot_id} could not find like button for track {track_id}')
        except Exception as e:
            print(e)

def bot_like_track_on_track_page_not_playing(browser, bot_id, track_id):
    bot_already_liked = bot_check_liked_track_in_db(bot_id, track_id)
    if bot_already_liked == True:
        print(f'BOT LIKE TRACK ERROR : Bot {bot_id} has already liked track {track_id}')
    else:
        print(f'BOT LIKE TRACK : Bot {bot_id} has not already liked track {track_id}')
        try:
            time.sleep(random.uniform(0.5, 1))
            like_button = browser.find_element_by_xpath('//button[@name="favorite"]')
            if like_button:
                like_button.click()
                print(f'BOT LIKE TRACK : Bot {bot_id} has clicked like button on track {track_id}')
            try:
                insert_new_liked_track_in_db(bot_id, track_id)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

