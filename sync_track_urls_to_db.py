# INIT GENERAL IMPORTS
import time, random

# INIT SELENIUM IMPORTS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# INIT CUSTOM IMPORTS
from setup_browser import init_browser_headless
from database import *

# FETCH ARTIST WITH {artist_id} FROM AUDIUS API,
# RETRIEVE ARTIST TRACK LIST,
# ORGANIZE TRACK DATA FOR EACH TRACK IN TRACK LIST,
# AND RETURN LIST OF TRACK DATAS


def get_artist_track_list(artist_id):
    artist_track_list = query_tracks_by_artist(artist_id)
    track_datas_list = []
    for track in artist_track_list:
        track_id = track[0]
        track_name = track[2]
        track_duration = track[3]
        track_url = track[9]
        track_data = (
            track_id,
            artist_id,
            track_name,
            track_duration,
            track_url,
        )
        track_datas_list.append(track_data)
    return track_datas_list


# FETCH ARTIST WITH {artist_id} FROM AUDIUS API,
# AND RETURN ARTIST AUDIUS HANDLE


def get_artist_handle(artist_id):
    artist_handle = query_artist_handle_by_id(artist_id)
    return artist_handle


# USING SELENIUM BROWSER INSTANCE,
# NAVIGATE TO ARTIST AUDIUS PAGE WITH {artist_id}


def nav_artist_page(browser, artist_id):
    handle = get_artist_handle(artist_id)
    browser.get(f"https://audius.co/{handle}")


found_track = False

# USING SELENIUM BROWSER INSTANCE,
# SEARCH FOR TRACK WITH {track_title}
# IF TRACK IS FOUND,
# RETURN TRACK BROWSER ELEMENT


def find_track(browser, track_title):
    global found_track
    track_elements = browser.find_elements_by_class_name(
        "TrackTile_title__1zakm"
    )
    for track in track_elements:
        if track_title == track.text:
            found_track = True
            return track
        else:
            pass


def scroll(browser):
    ActionChains(browser).key_down(Keys.LEFT_ALT).key_down(Keys.DOWN).key_up(
        Keys.LEFT_ALT
    ).key_up(Keys.DOWN).perform()


def scroll_artist_page(browser, track_title):
    global found_track
    browser.implicitly_wait(10)
    browser.find_element_by_xpath('//*[@id="mainContent"]').click()
    time.sleep(0.2)


def bot_find_url_and_update(browser, track_id):
    track_url = browser.current_url
    print(f"TRACK ID {track_id} has the url : {track_url}")
    update_track_url_in_db(track_id, track_url)


def get_track_url(browser, data):
    track_id = data[0]
    artist_id = data[1]
    track_title = data[2]
    track_duration = data[3]
    track_url = data[4]
    nav_artist_page(browser, artist_id)
    print("got artist page")
    time.sleep(random.uniform(2, 5.1))
    print("time to scroll")
    scroll_artist_page(browser, track_title)
    print("scrolling done")
    time.sleep(random.uniform(1.3, 2.9))
    bot_find_url_and_update(browser, track_id)


def sync_track_urls_to_db():
    browser = init_browser_headless()
    artists_list = query_all_artists()
    print("got artist list")
    for artist in artists_list:
        artist_id = artist[0]
        print(f"working for artist : {artist[1]} right now")
        track_datas_list = get_artist_track_list(artist_id)
        print("got artist track_data_list")
        for data in track_datas_list:
            get_track_url(browser, data)


if __name__ == "__main__":
    sync_track_urls_to_db()
