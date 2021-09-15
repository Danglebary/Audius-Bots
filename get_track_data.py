# INIT GENERAL IMPORTS
import requests

# INIT CUSTOM IMPORTS
from error_handler import handle_api_error, handle_resolve_data_error
from get_artist_data import get_artist_id_by_username
from custom_types import TrackData

# INIT URL REQUEST PARAMS
headers = {"Accept": "application/json"}

# UTILITY FUNCTIONS


def request_user_tracks_by_id(user_id: str) -> list:
    try:
        r = requests.get(
            f"https://discoveryprovider3.audius.co/v1/users/{user_id}/tracks",
            headers=headers,
        )
        result: list = r.json()["data"]
        return result
    except Exception:
        error_data = f"user tracks for user ID {user_id}"
        handle_api_error(error_data, 1)


def request_track_by_id(track_id: str) -> dict:
    try:
        r = requests.get(
            f"https://discoveryprovider3.audius.co/v1/tracks/{track_id}",
            headers=headers,
        )
        result: dict = r.json()["data"]
        return result
    except Exception:
        error_data = f"track data for track ID {track_id}"
        handle_api_error(error_data, 2)


# MAIN FUNCTIONS


def get_artist_tracks_by_id(user_name: str) -> list:
    try:
        track_list = []
        user_id: str = get_artist_id_by_username(user_name)
        tracks = request_user_tracks_by_id(user_id)
        for track in tracks:
            track_data: str = track["id"]
            track_list.append(track_data)
        return track_list
    except Exception:
        error_data = f"user tracks for user {user_name}"
        handle_resolve_data_error(error_data, 2)


def get_all_track_data_by_id(
    track_id: str,
) -> TrackData:
    try:
        r: dict = request_track_by_id(track_id)
        artist_id: str = r["user"]["id"]
        track_title: str = r["title"]
        track_duration: int = r["duration"]
        track_genre: str = r["genre"]
        track_mood: str = r["mood"]
        track_plays: int = r["play_count"]
        track_faves: int = r["favorite_count"]
        track_reposts: int = r["repost_count"]

        track_data: TrackData = (
            track_id,
            artist_id,
            track_title,
            track_duration,
            track_genre,
            track_mood,
            track_plays,
            track_faves,
            track_reposts,
        )

        return track_data
    except Exception:
        error_data = f"track data for track ID {track_id}"
        handle_resolve_data_error(error_data, 3)


def get_track_play_count_by_id(track_id: str) -> int:
    try:
        r = request_track_by_id(track_id)
        result: int = r["play_count"]
        return result
    except Exception:
        error_data = f"track play count for track ID {track_id}"
        handle_resolve_data_error(error_data, 3)


def get_track_fave_count_by_id(track_id: str) -> int:
    try:
        r = request_track_by_id(track_id)
        result: int = r["favorite_count"]
        return result
    except Exception:
        error_data = f"track fave count for track ID {track_id}"
        handle_resolve_data_error(error_data, 3)


def get_track_repost_count_by_id(track_id: str) -> int:
    try:
        r = request_track_by_id(track_id)
        result: int = r["repost_count"]
        return result
    except Exception:
        error_data = f"track repost count for track ID {track_id}"
        handle_resolve_data_error(error_data, 3)


def get_track_genre_by_id(track_id: str) -> str:
    try:
        r = request_track_by_id(track_id)
        result: str = r["genre"]
        return result
    except Exception:
        error_data = f"track genre for track ID {track_id}"
        handle_resolve_data_error(error_data, 3)


def get_track_mood_by_id(track_id: str) -> str:
    try:
        r = request_track_by_id(track_id)
        result: str = r["mood"]
        return result
    except Exception:
        error_data = f"track mood for track ID {track_id}"
        handle_resolve_data_error(error_data, 3)


def get_track_title_by_id(track_id: str) -> str:
    try:
        r = request_track_by_id(track_id)
        result: str = r["title"]
        return result
    except Exception:
        error_data = f"track title for track ID {track_id}"
        handle_resolve_data_error(error_data, 3)


def get_track_duration_by_id(track_id: str) -> int:
    try:
        r = request_track_by_id(track_id)
        result: int = r["duration"]
        return result
    except Exception:
        error_data = f"track duration for track ID {track_id}"
        handle_resolve_data_error(error_data, 3)


def get_track_artist_by_id(track_id: str) -> str:
    try:
        r = request_track_by_id(track_id)
        result: str = r["user"]["id"]
        return result
    except Exception:
        error_data = f"track artist for track ID {track_id}"
        handle_resolve_data_error(error_data, 3)


def get_user_total_tracks_play_count(user_name: str) -> int:
    track_list = get_artist_tracks_by_id(user_name)
    track_plays: list[int] = []
    for track in track_list:
        plays: int = get_track_play_count_by_id(track)
        track_plays.append(plays)
    total_plays: int = sum(track_plays)
    print(f"Artist {user_name} has {total_plays} total streams on Audius")
