# INIT GENERAL IMPORTS

import requests

# INIT CUSTOM IMPORTS

from error_handler import handle_api_error, handle_resolve_data_error
from get_artist_data import get_user_id

# INIT URL REQUEST PARAMS

headers = {
  'Accept': 'application/json'
}

# UTILITY FUNCTIONS

def request_user_tracks_by_id(user_id):
    try:
        r = requests.get(f'https://discoveryprovider3.audius.co/v1/users/{user_id}/tracks', headers=headers)
        result = (r.json()['data'])
        return result
    except Exception:
        error_data = f'user tracks for user ID {user_id}'
        handle_api_error(error_data, 1)

def request_track_by_id(track_id):
    try:
        r = requests.get(f'https://discoveryprovider3.audius.co/v1/tracks/{track_id}', headers=headers)
        result = (r.json()['data'])
        return result
    except Exception:
        error_data = f'track data for track ID {track_id}'
        handle_api_error(error_data, 2)

# MAIN FUNCTIONS

def get_user_tracks_by_id(user_name):
    try:
        track_list = []
        user_id = get_user_id(user_name)
        r = request_user_tracks_by_id(user_id)
        for x in r:
            track_data = x['id']
            track_list.append(track_data)
        return track_list
    except Exception:
        error_data = f'user tracks for user {user_name}'
        handle_resolve_data_error(error_data, 2)

def get_all_track_data_by_id(track_id):
    try:
        r = request_track_by_id(track_id)
        artist_id = r['user']['id']
        track_title = r['title']
        track_duration = r['duration']
        track_genre = r['genre']
        track_mood = r['mood']
        track_plays = r['play_count']
        track_faves = r['favorite_count']
        track_reposts = r['repost_count']

        track_data = (
            track_id,
            artist_id,
            track_title,
            track_duration,
            track_genre,
            track_mood,
            track_plays,
            track_faves,
            track_reposts
        )
        
        return track_data
    except Exception:
        error_data = f'track data for track ID {track_id}'
        handle_resolve_data_error(error_data, 3)

def get_track_play_count_by_id(track_id):
    try:
        r = request_track_by_id(track_id)
        result = r['play_count']
        return result
    except Exception:
        error_data = f'track play count for track ID {track_id}'
        handle_resolve_data_error(error_data, 3)

def get_track_fave_count_by_id(track_id):
    try:
        r = request_track_by_id(track_id)
        result = r['favorite_count']
        return result
    except Exception:
        error_data = f'track fave count for track ID {track_id}'
        handle_resolve_data_error(error_data, 3)

def get_track_repost_count_by_id(track_id):
    try:
        r = request_track_by_id(track_id)
        result = r['repost_count']
        return result
    except Exception:
        error_data = f'track repost count for track ID {track_id}'
        handle_resolve_data_error(error_data, 3)

def get_track_genre_by_id(track_id):
    try:
        r = request_track_by_id(track_id)
        result = r['genre']
        return result
    except Exception:
        error_data = f'track genre for track ID {track_id}'
        handle_resolve_data_error(error_data, 3)

def get_track_mood_by_id(track_id):
    try:
        r = request_track_by_id(track_id)
        result = r['mood']
        return result
    except Exception:
        error_data = f'track mood for track ID {track_id}'
        handle_resolve_data_error(error_data, 3)

def get_track_title_by_id(track_id):
    try:
        r = request_track_by_id(track_id)
        result = r['title']
        return result
    except Exception:
        error_data = f'track title for track ID {track_id}'
        handle_resolve_data_error(error_data, 3)

def get_track_duration_by_id(track_id):
    try:
        r = request_track_by_id(track_id)
        result = r['duration']
        return result
    except Exception:
        error_data = f'track duration for track ID {track_id}'
        handle_resolve_data_error(error_data, 3)

def get_track_artist_by_id(track_id):
    try:
        r = request_track_by_id(track_id)
        result = r['user']['id']
        return result
    except Exception:
        error_data = f'track artist for track ID {track_id}'
        handle_resolve_data_error(error_data, 3)

def get_user_total_tracks_play_count(user_name):
    track_list = get_user_tracks_by_id(user_name)
    track_plays = []
    for track in track_list:
        plays = get_track_play_count_by_id(track)
        track_plays.append(plays)
    total_plays = sum(track_plays)
    print(f'Artist {user_name} has {total_plays} total streams on Audius')
