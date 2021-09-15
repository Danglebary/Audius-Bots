# GENERAL IMPORTS
from random import uniform
from time import sleep

# CUSTOM IMPORTS
from custom_types import ArtistData, TrackData

# AUDIUS API TOOLS FUNCTIONS IMPORTS
from get_track_data import get_artist_tracks_by_id, get_all_track_data_by_id
from get_artist_data import get_all_artist_data_by_user_name

# DATABASE FUNCTIONS IMPORTS
from database import *

# FETCH ARTIST WITH {USERNAME} FROM AUDIUS API,
# THEN ADD THE RESULTING ARTIST AND ARTIST DATA TO DB


def fetch_and_insert_new_artist_by_username(user_name: str) -> None:
    artist_data: ArtistData = get_all_artist_data_by_user_name(user_name)
    insert_new_artist_in_db(artist_data)


# FOR ALL ARTISTS IN DB,
# FETCH ARTIST WITH {USERNAME} FROM AUDIUS API,
# RETRIEVE LIST OF ALL TRACKS UPLOADED BY ARTIST,
# FOR EACH TRACK IN THE LIST, CHECK FOR THAT TRACK IN DB,
# IF TRACK IS NOT CURRENTLY IN DB, INSERT TRACK IN DB,
# AND FINALLY PRINT THE NUMBER OF NEWELY-ADDED TRACKS


def sync_db_tracks_for_all_artists() -> None:
    synced_tracks = []
    artists_list: list[str] = query_all_artists_name()
    for user_name in artists_list:
        artist_track_list: list[str] = get_artist_tracks_by_id(user_name)
        for track_id in artist_track_list:
            sleep(uniform(3.0, 15.0))
            fetched_track_data: TrackData = get_all_track_data_by_id(track_id)
            db_id: TrackData = query_track_by_id(track_id)
            if db_id:
                print(f"track {track_id} skipped : already in db")
            else:
                insert_new_track_in_db(fetched_track_data)
                synced_tracks.append(fetched_track_data["track_id"])
                print(f"track {track_id} successfully written to db")
    if len(synced_tracks) != 0:
        print(f"TOTAL NEW TRACKS SYNCED TO DB : {len(synced_tracks)}")
    else:
        print(f"NO NEW TRACKS TO SYNC")
