# INIT GENERAL IMPORTS
import requests

# INIT CUSTOM IMPORTS
from error_handler import handle_api_error, handle_resolve_data_error

# INIT URL REQUEST PARAMS
headers = {"Accept": "application/json"}

# UTILITY FUNCTIONS
def search_user_by_username(user_name: str) -> dict:
    try:
        r = requests.get(
            "https://discoveryprovider3.audius.co/v1/users/search",
            params={"query": user_name},
            headers=headers,
        )
        return r.json()["data"][0]
    except Exception:
        error_data = f"data for user : {user_name}"
        handle_api_error(error_data, 1)


def search_user_favorites(user_id: str) -> list:
    try:
        r = requests.get(
            f"https://discoveryprovider3.audius.co/v1/users/{user_id}/favorites",
            headers=headers,
        )
        results: list = r.json()["data"]
        return results
    except Exception:
        error_data = f"favorites data for user id : {user_id}"
        handle_api_error(error_data, 2)


# MAIN FUNCTIONS
def get_all_user_data_by_user_name(
    user_name: str,
) -> tuple[str, str, int, int]:
    try:
        r = search_user_by_username(user_name)
        artist_id: str = r["id"]
        following_count: int = r["followee_count"]
        follower_count: int = r["follower_count"]
        artist_data: tuple[str, str, int, int] = (
            artist_id,
            user_name,
            following_count,
            follower_count,
        )
        return artist_data
    except Exception:
        error_data = f"user data from {user_name}"
        handle_resolve_data_error(error_data, 3)


def get_user_id_by_username(user_name: str) -> str:
    try:
        r = search_user_by_username(user_name)
        result: str = r["id"]
        return result
    except Exception:
        error_data = f"user ID for {user_name}"
        handle_resolve_data_error(error_data, 3)


def get_user_follower_count_by_username(user_name: str) -> int:
    try:
        r = search_user_by_username(user_name)
        result: int = r["follower_count"]
        return result
    except Exception:
        error_data = f"user follower count for {user_name}"
        handle_resolve_data_error(error_data, 3)


def get_user_following_count_by_username(user_name: str) -> int:
    try:
        r = search_user_by_username(user_name)
        result: int = r["followee_count"]
        return result
    except Exception:
        error_data = f"user following count for {user_name}"
        handle_resolve_data_error(error_data, 3)


def get_user_track_count_by_username(user_name: str) -> int:
    try:
        r = search_user_by_username(user_name)
        result: int = r["track_count"]
        return result
    except Exception:
        error_data = f"user track count for {user_name}"
        handle_resolve_data_error(error_data, 3)


def get_user_album_count_by_username(user_name: str) -> int:
    try:
        r = search_user_by_username(user_name)
        result: int = r["album_count"]
        return result
    except Exception:
        error_data = f"user album count for {user_name}"
        handle_resolve_data_error(error_data, 3)


def get_user_favorites_count_by_username(user_name: str) -> int:
    try:
        user_id = get_user_id_by_username(user_name)
        favorites = search_user_favorites(user_id)
        result = len(favorites)
        return result
    except Exception:
        error_data = f"user favorites count for {user_name}"
        handle_resolve_data_error(error_data, 3)
