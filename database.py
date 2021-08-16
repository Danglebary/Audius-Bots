# INIT GENERAL IMPORTS

import sqlite3

# BOT PROFILES AND ACCOUNT FUNCTIONS

# CREATE BOTS DB TABLE

def create_bot_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE bots (
                bot_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name String NOT NULL,
                first_name String NOT NULL,
                last_name String NOT NULL,
                email String NOT NULL,
                password String NOT NULL,
                dob String NOT NULL
                )
            ''')
    conn.commit()
    conn.close()

# FETCH BOT DATA FROM DB

def query_all_bots():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('select * from bots')
    r = c.fetchall()
    conn.close()
    return r

def query_first_x_bots(nbots):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('select * from bots')
    r = c.fetchmany(nbots)
    conn.close()
    return r

def query_bot_by_user_name(user_name):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('select * from bots WHERE user_name="{user_name}"')
    r = c.fetchall()
    conn.close()
    return r

# WRITE BOT DATA TO DB

def insert_new_bot_in_db(bot_data):
    if bot_data:
        user_name = bot_data[0]
        first_name = bot_data[1]
        last_name = bot_data[2]
        email = bot_data[3]
        password = bot_data[4]
        dob = bot_data[5]
        try:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute(f'''INSERT INTO bots (user_name,first_name,last_name,email,password,dob) VALUES (
                        "{user_name}", 
                        "{first_name}", 
                        "{last_name}", 
                        "{email}",
                        "{password}",
                        "{dob}"
                        )
                    ''')
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
    else:
        print('ERROR: failed to write bot to db, no bot_data exists')

# ARTIST PROFILES AND ACCOUNT FUNCTIONS

# CREATE ARTISTS DB TABLE

def create_artist_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE artists (
                artist_id Text,
                artist_name Text,
                following_count Int,
                follower_count Int,
                artist_handle Text
                )
            ''')
    conn.commit()
    conn.close()

# FETCH ARTIST DATA FROM DB

def query_all_artists():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('select * from artists')
    r = c.fetchall()
    conn.close()
    return r

def query_x_artists_in_db(x):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('select * from artists')
    r = c.fetchmany(x)
    print(r)
    conn.close()

def query_artist_id_by_name(user_name):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'select * from artists WHERE artist_name="{user_name}"')
    r = c.fetchone()
    uId = r[0]
    conn.close()
    return uId

def query_artist_name_by_id(user_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'select * from artists WHERE artist_id="{user_id}"')
    r = c.fetchone()
    name = r[1]
    conn.close()
    return name

def query_all_artists_name():
    artist_list = []
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('select * from artists')
    r = c.fetchall()
    for row in r:
        artist_name = row[1]
        artist_list.append(artist_name)
    conn.close()
    return artist_list

def query_artist_handle_by_name(artist_name):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'select * from artists WHERE artist_name="{artist_name}"')
    r = c.fetchone()
    handle = r[4]
    conn.close()
    return handle

def query_artist_handle_by_id(artist_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'select * from artists WHERE artist_id="{artist_id}"')
    r = c.fetchone()
    handle = r[4]
    conn.close()
    return handle

# WRITE ARTIST DATA TO DB

def insert_new_artist_in_db(artist_data):
    if artist_data:
        artist_id = artist_data[0]
        artist_name = artist_data[1]
        following_count = artist_data[2]
        follower_count = artist_data[3]
        artist_handle = artist_data[4]
        try:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute(f'''INSERT INTO artists VALUES (
                        "{artist_id}", 
                        "{artist_name}", 
                        "{following_count}", 
                        "{follower_count}",
                        "{artist_handle}"
                        )
                    ''')
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
    else:
        print('ERROR: failed to write artist to db, no artist_data exists')

def update_artist_handle_in_db(artist_name, artist_handle):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'Update artists set artist_handle = "{artist_handle}" WHERE artist_name="{artist_name}"')
    conn.commit()
    conn.close()

# TRACK DATA AND FUNCTIONS

# CREATE TRACKS DB TABLE

def create_tracks_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE tracks (
                track_id Text,
                artist_id Text,
                track_title Text,
                track_duration Int,
                track_genre Text,
                track_mood Text,
                track_plays Int,
                track_faves Int,
                track_reposts Int,
                track_url
                FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
                )
            ''')
    conn.commit()
    conn.close()

# FETCH TRACK DATA FROM DB

def query_all_tracks():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('select * from tracks')
    r = c.fetchall()
    conn.close()
    return r

def query_x_tracks_in_db(x):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('select * from tracks')
    r = c.fetchmany(x)
    print(r)
    conn.close()

def query_tracks_by_artist(artist_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'select * from tracks WHERE artist_id="{artist_id}"')
    r = c.fetchall()
    conn.close()
    return r

def query_tracks_by_id(track_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'select * from tracks WHERE track_id="{track_id}"')
    r = c.fetchone()
    conn.close()
    return r

def query_track_url_by_id(track_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'select * from tracks WHERE track_id="{track_id}"')
    r = c.fetchone()
    url = r[9]
    conn.close()
    return url

def query_all_track_urls():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('select * from tracks')
    r = c.fetchall()
    urls = []
    for track in r:
        urls.append(track[9])
    conn.close()
    return urls

# WRITE TRACK DATA TO DB

def update_track_url_in_db(track_id, track_url):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'Update tracks set track_url = "{track_url}" WHERE track_id="{track_id}"')
    conn.commit()
    conn.close()
    print(f'track : {track_id} url : {track_url} successfully updated in db')

def insert_new_track_in_db(track_data):
    if track_data:
        track_id = track_data[0]
        artist_id = track_data[1]
        track_title = track_data[2]
        track_duration = track_data[3]
        track_genre = track_data[4]
        track_mood = track_data[5]
        track_plays = track_data[6]
        track_faves = track_data[7]
        track_reposts = track_data[8]
        track_url = track_data[9]
        print('THIS IS FROM DB FILE, artist_id = ' + artist_id)
        try:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute(f'''INSERT INTO tracks VALUES (
                        "{track_id}",
                        "{artist_id}",
                        "{track_title}",
                        "{track_duration}",
                        "{track_genre}",
                        "{track_mood}",
                        "{track_plays}",
                        "{track_faves}",
                        "{track_reposts}",
                        "{track_url}"
                        )
                    ''')
            conn.commit()
            conn.close()
            print(f'{track_title} data successfully written to db')
        except Exception as e:
            print(e)
    else:
        print('ERROR: failed to write track to db, no track_data exists')

# LIKED TRACKS TABLE AND FUNCTIONS

# CREATE LIKED TRACKS TABLE

def create_liked_tracks_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE liked_tracks (
                    bot_id Int NOT NULL,
                    track_id Text NOT NULL,
                    FOREIGN KEY (bot_id) REFERENCES bots (bot_id),
                    FOREIGN KEY (track_id) REFERENCES tracks (track_id)
                )
            ''')
    conn.commit()
    conn.close()

# WRITE LIKED TRACKS DATA TO DB

def insert_new_liked_track_in_db(bot_id, track_id):
    if bot_id:
        if track_id:
            try:
                conn = sqlite3.connect('data.db')
                c = conn.cursor()
                c.execute(f'''INSERT INTO liked_tracks VALUES (
                        "{bot_id}",
                        "{track_id}"
                        )
                    ''')
                conn.commit()
                conn.close()
                print(f'LIKED TRACK INSERT : Bot {bot_id} liked track {track_id} and was written to db')
            except Exception as e:
                print(e)
        else:
            print('LIKED TRACK INSERT ERROR: No track_id present for db to insert')
    else:
        print('LIKED TRACK INSERT ERROR: No bot_id present for db to insert')

# FETCH LIKED TRACKS DATA FROM DB

def query_liked_track_ids_by_bot_id(bot_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'select * from liked_tracks WHERE bot_id="{bot_id}"')
    r = c.fetchall()
    conn.close()
    return r

def query_bot_ids_by_liked_track_id(track_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'select * from liked_tracks WHERE track_id="{track_id}"')
    r = c.fetchall()
    conn.close()
    return r

def query_all_liked_tracks():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('select * from liked_tracks')
    r = c.fetchall()
    conn.close()
    return r

# REPOSTED TRACKS TABLE AND FUNCTIONS

# CREATE REPOSTED TRACKS TABLE

def create_track_reposts_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE reposted_tracks (
                    bot_id Int NOT NULL,
                    track_id Text NOT NULL,
                    FOREIGN KEY  (bot_id) REFERENCES bots (bot_id),
                    FOREIGN KEY (track_id) REFERENCES tracks (track_id)
                )
            ''')
    conn.commit()
    conn.close()
    
# WRITE REPOSTED TRACKS DATA TO DB

def insert_new_reposted_track_in_db(bot_id, track_id):
    if bot_id:
        if track_id:
            try:
                conn = sqlite3.connect('data.db')
                c = conn.cursor()
                c.execute(f'''INSERT INTO reposted_tracks VALUES (
                        "{bot_id}",
                        "{track_id}"
                        )
                    ''')
                conn.commit()
                conn.close()
                print(f'REPOSTED TRACK INSERT : Bot {bot_id} reposted track {track_id} and was written to db')
            except Exception as e:
                print(e)
        else:
            print('REPOSTED TRACK INSERT ERROR: No track_id present for db to insert')
    else:
        print('REPOSTED TRACK INSERT ERROR: No bot_id present for db to insert')

# FETCH REPOSTED TRACKS DATA FROM DB

def query_reposted_track_ids_by_bot_id(bot_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'select * from reposted_tracks WHERE bot_id="{bot_id}"')
    r = c.fetchall()
    conn.close()
    return r

def query_bot_ids_by_reposted_track_id(track_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'select * from reposted_tracks WHERE track_id="{track_id}"')
    r = c.fetchall()
    conn.close()
    return r

def query_all_reposted_tracks():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('select * from reposted_tracks')
    r = c.fetchall()
    conn.close()
    return r

# BOT ARTISTS FOLLOWING DATA AND FUNCTIONS

# CREATE BOT ARTISTS FOLLOWING TABLE

def create_bot_following_artists_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE bot_following_artists (
                    bot_id Text NOT NULL,
                    artist_id Text,
                    FOREIGN KEY (bot_id) REFERENCES bots (bot_id),
                    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
                )
            ''')
    conn.commit()
    conn.close()

# WRITE BOT FOLLOWING ARTISTS DATA TO DB

def insert_bot_new_artist_follow_in_db(bot_id, artist_id):
    if bot_id:
        if artist_id:
            try:
                conn = sqlite3.connect('data.db')
                c = conn.cursor()
                c.execute(f'''INSERT INTO bot_following_artists VALUES (
                            "{bot_id}",
                            "{artist_id}"
                        )
                    ''')
                conn.commit()
                conn.close()
            except Exception as e:
                print(e)
        else:
            print('BOT FOLLOW ARTIST INSERT ERROR : No artist_id present for db to insert')
    else:
        print('BOT FOLLOW ARTIST INSERT ERROR : No bot_id present for db to insert')

# FETCH BOT FOLLOWING ARTISTS DATA FROM DB

def query_bot_following_artists_by_bot_id(bot_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'select * from bot_following_artists WHERE bot_id="{bot_id}"')
    r = c.fetchall()
    return r

def query_bot_following_artists_by_artist_id(artist_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'select * from bot_following_artists WHERE artist_id="{artist_id}"')
    r = c.fetchall()
    return r

def query_all_following_artists_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('select * from bot_following_artists')
    r = c.fetchall()
    conn.close()
    return r

# DROP TABLES (BE CAREFUL WITH THIS!)

def drop_table(table_name):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f'DROP TABLE "{table_name}"')
    conn.commit()
    conn.close()
