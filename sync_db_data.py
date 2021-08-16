# INIT GENERAL IMPORTS
import time, random

# INIT AUDIUS API TOOLS FUNCTIONS IMPORTS
from get_track_data import get_user_tracks_by_id, get_all_track_data_by_id
from get_artist_data import search_user_by_username, get_all_user_data_by_user_name

# DATABASE FUNCTIONS IMPORTS
from database import *

# FETCH ARTIST WITH {USERNAME} FROM AUDIUS API, 
# THEN ADD THE RESULTING ARTIST AND ARTIST DATA TO DB

def fetch_and_insert_new_artist(user_name):
    artist_data = get_all_user_data_by_user_name(user_name)
    insert_new_artist_in_db(artist_data)

# FOR ALL ARTISTS IN DB,
# FETCH ARTIST WITH {USERNAME} FROM AUDIUS API,
# RETREIVE ARTIST HANDLE FROM AUDIUS ARTIST DATA,
# AND UPDATE ARTIST DB DATA TO INCLUDE THE ARTIST HANDLE

def update_all_artists_with_handle():
    all_artists = query_all_artists()
    for artist in all_artists:
        print(artist)
        artist_name = artist[1]
        artist_api_data = search_user_by_username(artist_name)
        handle = artist_api_data['handle']
        update_artist_handle_in_db(artist_name, handle)

# FOR ALL ARTISTS IN DB,
# FETCH ARTIST WITH {USERNAME} FROM AUDIUS API,
# RETRIEVE LIST OF ALL TRACKS UPLOADED BY ARTIST,
# FOR EACH TRACK IN THE LIST, CHECK FOR THAT TRACK IN DB,
# IF TRACK IS NOT CURRENTLY IN DB, INSERT TRACK IN DB,
# AND FINALLY RETURN THE NUMBER OF NEWELY-ADDED TRACKS

def sync_db_tracks_for_all_artists():
    synced_tracks = []
    artists_list = query_all_artists_name()
    for user_name in artists_list:
        artist_track_list = get_user_tracks_by_id(user_name)
        for track_id in artist_track_list:
            time.sleep(random.uniform(3.0, 15.0))
            fetched_track_data = get_all_track_data_by_id(track_id)
            db_id = query_tracks_by_id(track_id)
            if db_id:
                print(f'track {track_id} skipped : already in db')
            else:
                insert_new_track_in_db(fetched_track_data)
                synced_tracks.append(fetched_track_data[2])
                print(f'track {track_id} successfully written to db')
    if len(synced_tracks) != 0:
        print(f'TOTAL NEW TRACKS SYNCED TO DB : {len(synced_tracks)}')        
    else:
        print(f'NO NEW TRACKS TO SYNC')
