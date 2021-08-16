from get_artist_data import get_all_user_data_by_user_name
from get_track_data import get_all_track_data_by_id

def fetch_artist_data(user_name):
    artist_data = get_all_user_data_by_user_name(user_name)
    return artist_data

def fetch_single_track_data(track_id):
    track_data = get_all_track_data_by_id(track_id)
    return track_data
