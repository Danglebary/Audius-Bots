# GENERAL IMPORTS
import sqlite3

# CUSTOM IMPORTS
from custom_types import (
    BotData,
    ArtistData,
    TrackData,
    BotArtistRelationshipData,
)

# BOT PROFILES AND ACCOUNT FUNCTIONS

# CREATE BOTS DB TABLE
def create_bot_table() -> None:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE bots (
                bot_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name String NOT NULL,
                first_name String NOT NULL,
                last_name String NOT NULL,
                email String NOT NULL,
                password String NOT NULL,
                dob String NOT NULL
                )
            """
    )
    conn.commit()
    conn.close()


# FETCH BOT DATA FROM DB
def query_all_bots() -> list[BotData]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from bots")
    r: list[BotData] = c.fetchall()
    conn.close()
    return r


def query_first_x_bots(nbots: int) -> list[BotData]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from bots")
    r: list[BotData] = c.fetchmany(nbots)
    conn.close()
    return r


def query_bot_by_user_name(user_name: str) -> BotData:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute('select * from bots WHERE user_name="{user_name}"')
    r: BotData = c.fetchone()
    conn.close()
    return r


# WRITE BOT DATA TO DB
def insert_new_bot_in_db(bot_data: BotData) -> None:
    user_name = bot_data["user_name"]
    first_name = bot_data["first_name"]
    last_name = bot_data["last_name"]
    email = bot_data["email"]
    password = bot_data["password"]
    dob = bot_data["dob"]
    try:
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute(
            f"""INSERT INTO bots (user_name,first_name,last_name,email,password,dob) VALUES (
                    "{user_name}", 
                    "{first_name}", 
                    "{last_name}", 
                    "{email}",
                    "{password}",
                    "{dob}"
                    )
                """
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


# ARTIST PROFILES AND ACCOUNT FUNCTIONS

# CREATE ARTISTS DB TABLE
def create_artist_table() -> None:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE artists (
                artist_id Text,
                artist_name Text,
                artist_handle Text,
                following_count Int,
                follower_count Int
                )
            """
    )
    conn.commit()
    conn.close()


# FETCH ARTIST DATA FROM DB
def query_all_artists() -> list[ArtistData]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from artists")
    r: list[ArtistData] = c.fetchall()
    conn.close()
    return r


def query_x_artists_in_db(n_artists: int) -> list[ArtistData]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from artists")
    r: list[ArtistData] = c.fetchmany(n_artists)
    conn.close()
    return r


def query_artist_id_by_name(user_name: str) -> str:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(f'select * from artists WHERE artist_name="{user_name}"')
    r: ArtistData = c.fetchone()
    uId: str = r[0]
    conn.close()
    return uId


def query_artist_name_by_id(user_id: str) -> str:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(f'select * from artists WHERE artist_id="{user_id}"')
    r: ArtistData = c.fetchone()
    name: str = r[1]
    conn.close()
    return name


def query_all_artists_name() -> list[str]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from artists")
    r: list[ArtistData] = c.fetchall()
    artist_list: list[str] = [artist[1] for artist in r]
    conn.close()
    return artist_list


def query_artist_handle_by_name(artist_name: str) -> str:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(f'select * from artists WHERE artist_name="{artist_name}"')
    r: ArtistData = c.fetchone()
    handle: str = r[2]
    conn.close()
    return handle


def query_artist_handle_by_id(artist_id: str) -> str:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(f'select * from artists WHERE artist_id="{artist_id}"')
    r: ArtistData = c.fetchone()
    handle: str = r[2]
    conn.close()
    return handle


# WRITE ARTIST DATA TO DB
def insert_new_artist_in_db(artist_data: ArtistData) -> None:
    artist_id: str = artist_data["artist_id"]
    artist_name: str = artist_data["user_name"]
    artist_handle: str = artist_data["artist_handle"]
    following_count: int = artist_data["following_count"]
    follower_count: int = artist_data["follower_count"]

    try:
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute(
            f"""INSERT INTO artists VALUES (
                    "{artist_id}", 
                    "{artist_name}", 
                    "{following_count}", 
                    "{follower_count}",
                    "{artist_handle}"
                    )
                """
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


# TRACK DATA AND FUNCTIONS

# CREATE TRACKS DB TABLE
def create_tracks_table() -> None:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE tracks (
                track_id Text,
                artist_id Text,
                track_title Text,
                track_duration Int,
                track_genre Text,
                track_mood Text,
                track_plays Int,
                track_faves Int,
                track_reposts Int,
                track_url Text
                FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
                )
            """
    )
    conn.commit()
    conn.close()


# FETCH TRACK DATA FROM DB
def query_all_tracks() -> list[TrackData]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from tracks")
    r: list[TrackData] = c.fetchall()
    conn.close()
    return r


def query_x_tracks_in_db(n_tracks: int) -> list[TrackData]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from tracks")
    r: list[TrackData] = c.fetchmany(n_tracks)
    conn.close()
    return r


def query_tracks_by_artist(artist_id: str) -> list[TrackData]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(f'select * from tracks WHERE artist_id="{artist_id}"')
    r: list[TrackData] = c.fetchall()
    conn.close()
    return r


def query_track_by_id(track_id: str) -> TrackData:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(f'select * from tracks WHERE track_id="{track_id}"')
    r: TrackData = c.fetchone()
    conn.close()
    return r


def query_track_url_by_id(track_id: str) -> str:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(f'select * from tracks WHERE track_id="{track_id}"')
    r: TrackData = c.fetchone()
    url = r["track_url"]
    conn.close()
    return url


def query_all_track_urls() -> list[str]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from tracks")
    r: list[TrackData] = c.fetchall()
    urls: list[str] = [track_data["track_url"] for track_data in r]
    conn.close()
    return urls


# WRITE TRACK DATA TO DB
def update_track_url_in_db(track_id: str, track_url: str) -> None:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(
        f'Update tracks set track_url = "{track_url}" WHERE track_id="{track_id}"'
    )
    conn.commit()
    conn.close()
    print(f"track : {track_id} url : {track_url} successfully updated in db")


def insert_new_track_in_db(track_data: TrackData) -> None:
    track_id = track_data["track_id"]
    artist_id = track_data["artist_id"]
    track_title = track_data["track_title"]
    track_duration = track_data["track_duration"]
    track_genre = track_data["track_genre"]
    track_mood = track_data["track_mood"]
    track_plays = track_data["track_plays"]
    track_faves = track_data["track_faves"]
    track_reposts = track_data["track_reposts"]
    try:
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute(
            f"""INSERT INTO tracks VALUES (
                    "{track_id}",
                    "{artist_id}",
                    "{track_title}",
                    "{track_duration}",
                    "{track_genre}",
                    "{track_mood}",
                    "{track_plays}",
                    "{track_faves}",
                    "{track_reposts}"
                    )
                """
        )
        conn.commit()
        conn.close()
        print(f"{track_title} data successfully written to db")
    except Exception as e:
        print(e)


# LIKED TRACKS TABLE AND FUNCTIONS

# CREATE LIKED TRACKS TABLE
def create_liked_tracks_table() -> None:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE liked_tracks (
                    bot_id Int NOT NULL,
                    track_id Text NOT NULL,
                    FOREIGN KEY (bot_id) REFERENCES bots (bot_id),
                    FOREIGN KEY (track_id) REFERENCES tracks (track_id)
                )
            """
    )
    conn.commit()
    conn.close()


# WRITE LIKED TRACKS DATA TO DB
def insert_new_liked_track_in_db(bot_id, track_id: str) -> None:
    try:
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute(
            f"""INSERT INTO liked_tracks VALUES (
                "{bot_id}",
                "{track_id}"
                )
            """
        )
        conn.commit()
        conn.close()
        print(
            f"LIKED TRACK INSERT : Bot {bot_id} liked track {track_id} and was written to db"
        )
    except Exception as e:
        print(e)


# FETCH LIKED TRACKS DATA FROM DB
def query_liked_track_ids_by_bot_id(bot_id: int) -> list[str]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(f'select * from liked_tracks WHERE bot_id="{bot_id}"')
    r: list[BotArtistRelationshipData] = c.fetchall()
    track_ids: list[str] = [liked_track["track_id"] for liked_track in r]
    conn.close()
    return track_ids


def query_bot_ids_by_liked_track_id(track_id: str) -> list[int]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(f'select * from liked_tracks WHERE track_id="{track_id}"')
    r: list[BotArtistRelationshipData] = c.fetchall()
    bot_ids: list[int] = [liked_track["bot_id"] for liked_track in r]
    conn.close()
    return bot_ids


def query_all_liked_tracks() -> list[BotArtistRelationshipData]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from liked_tracks")
    r: list[BotArtistRelationshipData] = c.fetchall()
    conn.close()
    return r


# REPOSTED TRACKS TABLE AND FUNCTIONS

# CREATE REPOSTED TRACKS TABLE
def create_track_reposts_table() -> None:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE reposted_tracks (
                    bot_id Int NOT NULL,
                    track_id Text NOT NULL,
                    FOREIGN KEY  (bot_id) REFERENCES bots (bot_id),
                    FOREIGN KEY (track_id) REFERENCES tracks (track_id)
                )
            """
    )
    conn.commit()
    conn.close()


# WRITE REPOSTED TRACKS DATA TO DB
def insert_new_reposted_track_in_db(bot_id: int, track_id: str) -> None:
    try:
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute(
            f"""INSERT INTO reposted_tracks VALUES (
                "{bot_id}",
                "{track_id}"
                )
            """
        )
        conn.commit()
        conn.close()
        print(
            f"REPOSTED TRACK INSERT : Bot {bot_id} reposted track {track_id} and was written to db"
        )
    except Exception as e:
        print(e)


# FETCH REPOSTED TRACKS DATA FROM DB
def query_reposted_track_ids_by_bot_id(bot_id: int) -> list[str]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(f'select * from reposted_tracks WHERE bot_id="{bot_id}"')
    r: list[BotArtistRelationshipData] = c.fetchall()
    track_ids: list[str] = [reposted_track["track_id"] for reposted_track in r]
    conn.close()
    return track_ids


def query_bot_ids_by_reposted_track_id(track_id: str) -> list[int]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(f'select * from reposted_tracks WHERE track_id="{track_id}"')
    r: list[BotArtistRelationshipData] = c.fetchall()
    bot_ids: list[int] = [reposted_track["bot_id"] for reposted_track in r]
    conn.close()
    return bot_ids


def query_all_reposted_tracks() -> list[BotArtistRelationshipData]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from reposted_tracks")
    r: list[BotArtistRelationshipData] = c.fetchall()
    conn.close()
    return r


# BOT ARTISTS FOLLOWING DATA AND FUNCTIONS

# CREATE BOT ARTISTS FOLLOWING TABLE
def create_bot_following_artists_table() -> None:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE bot_following_artists (
                    bot_id Int NOT NULL,
                    artist_id Text,
                    FOREIGN KEY (bot_id) REFERENCES bots (bot_id),
                    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
                )
            """
    )
    conn.commit()
    conn.close()


# WRITE BOT FOLLOWING ARTISTS DATA TO DB
def insert_bot_new_artist_follow_in_db(bot_id: int, artist_id: str) -> None:
    try:
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute(
            f"""INSERT INTO bot_following_artists VALUES (
                    "{bot_id}",
                    "{artist_id}"
                )
            """
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


# FETCH BOT FOLLOWING ARTISTS DATA FROM DB
def query_bot_following_artists_by_bot_id(bot_id: int) -> list[str]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(f'select * from bot_following_artists WHERE bot_id="{bot_id}"')
    r: list[BotArtistRelationshipData] = c.fetchall()
    artist_ids: list[str] = [
        following_data["artist_id"] for following_data in r
    ]
    conn.close()
    return artist_ids


def query_bots_following_artist_by_artist_id(artist_id: str) -> list[int]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(
        f'select * from bot_following_artists WHERE artist_id="{artist_id}"'
    )
    r: list[BotArtistRelationshipData] = c.fetchall()
    bot_ids: list[int] = [following_data["bot_id"] for following_data in r]
    conn.close()
    return bot_ids


def query_all_following_artists_data() -> list[BotArtistRelationshipData]:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("select * from bot_following_artists")
    r: list[BotArtistRelationshipData] = c.fetchall()
    conn.close()
    return r


# DROP TABLES (BE CAREFUL WITH THIS!)
def drop_table(table_name: str) -> None:
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(f'DROP TABLE "{table_name}"')
    conn.commit()
    conn.close()


# CREATE ALL DB TABLES
def create_all_db_tables() -> None:
    create_bot_table()
    create_artist_table()
    create_tracks_table()
    create_bot_following_artists_table()
    create_liked_tracks_table()
    create_track_reposts_table()
