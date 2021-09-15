# GENERAL IMPORTS
from typing import TypedDict
from typing_extensions import NotRequired

# CUSTOM DATA TYPES -> strictly typed dicts


class BotData(TypedDict):
    """
    custom dataType for bot datas

    bot_id: int
    user_name: str
    first_name: str
    last_name: str
    email: str
    password: str
    dob: str
    """

    bot_id: int
    user_name: str
    first_name: str
    last_name: str
    email: str
    password: str
    dob: str


class ArtistData(TypedDict):
    """
    custom dataType for artist datas

    artist_id: str
    user_name: str
    artist_handle: str
    following_count: int
    follower_count: int
    """

    artist_id: str
    user_name: str
    artist_handle: str
    following_count: int
    follower_count: int


class TrackData(TypedDict):
    """
    custom dataType for track datas

    track_id: str
    artist_id: str
    track_title: str
    track_duration: int
    track_genre: str
    track_mood: str
    track_plays: int
    track_faves: int
    track_reposts: int
    track_url: notRequired[str]
    """

    track_id: str
    artist_id: str
    track_title: str
    track_duration: int
    track_genre: str
    track_mood: str
    track_plays: int
    track_faves: int
    track_reposts: int
    track_url: NotRequired[str]


class BotArtistRelationshipData(TypedDict):
    """
    custom dataType for liked track datas, reposted track datas, and bot following artist datas

    bot_id: int
    track_id: str
    """

    bot_id: int
    track_id: str
