# INIT GENERAL IMPORTS
import time, random, math

# INIT CUSTOM IMPORTS
from config import (
    track_play_buttom_xPath,
    special_artists,
    min_stream_per_loop,
    special_streaming_weight,
)
from database import (
    query_artist_id_by_name,
    query_tracks_by_artist,
    query_all_tracks,
)
from bot_like_track import bot_like_track_on_track_page_not_playing
from bot_repost_track import bot_repost_track_on_track_page

# FUNCTION TO PLAY SPECIFIED TRACK FOR COMPLETE DURATION OF THE TRACK
# ! SHOULD UPDATE THIS TO PLAY TRACK FOR EITHER THE COMPLETE DURATION,
#   OR FOR A RANDOMLY CHOSEN DURATION BASED ON THE COMPLETE DURATION OF THE TRACK !


def play_track(play_button, track_duration, user_name, track_title):

    dur = track_duration
    print(
        f"STREAM BOT : {user_name} is streaming track {track_title} for {dur} seconds"
    )
    play_button.click()
    time.sleep(dur)
    print(
        f"STREAM BOT : {user_name} has completed streaming track {track_title}"
    )


# FUNCTION FOR BOT TO CHOOSE RANDOMLY TO TRY LIKING OR REPOSTING ANY GIVEN TRACK
# IF {like_seed} IS LESS THAN 0.61, BOT WILL NOT LIKE TRACK,
# IF BOT DOES NOT LIKE TRACK, IF {repost_seed} IS GREATER THAN 0.62, BOT WILL REPOST TRACK
# IF {like_seed} IS GREATER THAN 0.9, BOT WILL BOTH LIKE AND REPOST THE TRACK


def bot__like_repost_logic(browser, bot_id, track_id):
    like_seed = random.uniform(0.0, 1.0)
    repost_seed = random.uniform(0.0, 1.0)
    if like_seed <= 0.61:
        pass
    elif like_seed >= 0.9:
        bot_like_track_on_track_page_not_playing(browser, bot_id, track_id)
        time.sleep(random.uniform(0.6, 1.6))
        bot_repost_track_on_track_page(browser, bot_id, track_id)
        time.sleep(random.uniform(0.8, 1.9))
    else:
        bot_like_track_on_track_page_not_playing(browser, bot_id, track_id)
        time.sleep(random.uniform(1, 2.7))
        if repost_seed >= 0.62:
            bot_repost_track_on_track_page(browser, bot_id, track_id)
            time.sleep(random.uniform(0.5, 2.1))
        else:
            pass


# FUNCTION TO NAVIGATE TO SPECIFIED TRACK AUDIUS PAGE,
# AND STREAM SPECIFIED TRACK


def bot_stream_track(browser, track, user_name):

    track_title = track[2]
    track_duration = track[3]
    track_url = track[9]

    browser.get(track_url)
    time.sleep(random.uniform(1, 2.1))
    print(
        f"STREAM BOT : {user_name} has found track url for track : {track_title}"
    )

    play_button = browser.find_element_by_xpath(track_play_buttom_xPath)
    if play_button:
        print(f"STREAM BOT : {user_name} has found play button")
        play_track(play_button, track_duration, user_name, track_title)
    else:
        pass


# FUNCTION TO RETRIEVE DESIRED "extra streamed" ARISTS TRACKS,
# EACH ARTIST WILL GAIN x STREAMS THIS LOOP,
# WHERE x IS AN EQUAL PORTION OF THE TOTAL NUMBER OF EXTRA STREAMS TO BE DISTRIBUTED
# BASED ON x, A RANDOM SAMPLE OF EACH ARTISTS SONGS WILL BE SELECTED FOR STREAMING


def get_special_tracks(special_stream_count):

    each_artist_portion = math.ceil(
        special_stream_count / len(special_artists)
    )

    all_special_tracks_list = []

    for artist in special_artists:
        special_artist_id = query_artist_id_by_name(artist)
        special_artist_tracks = query_tracks_by_artist(special_artist_id)

        if len(special_artist_tracks) >= each_artist_portion:
            all_special_tracks_list.append(
                random.sample(special_artist_tracks, k=each_artist_portion)
            )
        else:
            all_special_tracks_list.append(
                random.choices, k=each_artist_portion
            )

    random.shuffle(all_special_tracks_list)
    return all_special_tracks_list


# FUNCTION TO BE "brains" OF THE STREAMING OPERATION.

# FIRST, RETRIEVE A LIST OF ALL TRACKS IN DB
# THEN, SHUFFLE TRACK LIST
# THEN, CALCULATE TOTAL NUMBER OF STREAMS TO BE COMPLETED THIS LOOP,
#       RANDOMLY BETWEEN A MIN (180) AND MAX (all_tracks)
# THEN, CALCULATE TOTAL NUMBER OF STREAMS FOR "extra streamed" ARTISTS,
#       CURRENTLY CALCULATED AS 62% OF TOTAL NUMBER OF STREAMS
#       (this helps make bots look more human, as they are sacrificing
#       pure numbers boosting, by playing other random artists and songs as well,
#       just like how any actual person listens to more than just one artist)
# THEN, RETRIEVE TRACK LIST FOR "extra streamed" ARTISTS
# THEN, PRINT THE STREAMING DISTRIBUTION
# THEN, FOR THE EACH STREAM IN TOTAL STREAMS
# RANDOMLY CHOOSE TO PLAY A RANDOM TRACK FROM "all_tracks" or from "extra streamed" ARTISTS LIST
# LOOP UNTIL THE STREAM COUNT HAS REACHED TOTAL AMOUNT OF STREAMS FOR THE LOOP


def bot_stream_routine(browser, user_name, bot_id, special_artists):
    # DB TRACK LISTS
    all_tracks = query_all_tracks()
    random.shuffle(all_tracks)

    # CALC TOTAL STREAMS, BDB STREAMS, AND RANDOM STREAMS
    nTotalStreams = random.randint(min_stream_per_loop, len(all_tracks))
    nSpecialStreams = math.ceil((nTotalStreams * special_streaming_weight))
    nRandStreams = nTotalStreams - nSpecialStreams

    special_tracks = get_special_tracks(nSpecialStreams)

    if nTotalStreams != 0:
        print(
            f"STREAM BOT : {user_name} : {nTotalStreams} track(s) will be streamed this loop"
        )
        print(
            f"STREAM BOT : {user_name} : BadDayBound will recieve {nSpecialStreams} stream(s) this loop"
        )
        print(
            f"STREAM BOT : {user_name} : {nRandStreams} stream(s) will be graciously given to random people!"
        )

        total_streams_remaining = nTotalStreams
        special_streams_remaining = nSpecialStreams
        rand_streams_remaining = nRandStreams

        for _ in range(nTotalStreams):
            rand_choice = random.uniform(0, 1)
            if rand_choice >= 0.5:
                if special_streams_remaining != 0:
                    track = random.choice(special_tracks)
                    bot_stream_track(browser, track, user_name, bot_id)
                    special_streams_remaining -= 1
                    total_streams_remaining -= 1
                else:
                    if rand_streams_remaining != 0:
                        track = random.choice(all_tracks)
                        bot_stream_track(browser, track, user_name, bot_id)
                        rand_streams_remaining -= 1
                        total_streams_remaining -= 1
                    else:
                        pass
            else:
                if rand_streams_remaining != 0:
                    track = random.choice(all_tracks)
                    bot_stream_track(browser, track, user_name, bot_id)
                    rand_streams_remaining -= 1
                    total_streams_remaining -= 1
                else:
                    if special_streams_remaining != 0:
                        track = random.choice(special_tracks)
                        bot_stream_track(browser, track, user_name, bot_id)
                        special_streams_remaining -= 1
                        total_streams_remaining -= 1
                    else:
                        pass

    else:
        print(
            f"STREAM BOT : bot has chosen to not stream any tracks this loop"
        )
