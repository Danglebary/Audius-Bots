# INITIAL NUMBER OF BOTS TO CREATE
init_nBots = 10
# INITIAL ARTISTS TO ADD
init_extra_artists = []
# SPECIAL ARTISTS (the one who will get more streams than others)
special_artists = []
# WEIGHT PERCENTAGE (NORMALIZED) TO CALCULATE SPECIAL ARTISTS STREAMING RATE
special_streaming_weight = 0.62
# MIN TOTAL STREAMS (extra and special artists) PER BOT PER LOOP
min_stream_per_loop = 180
# URLS
# BOT CREATION
bot_quick_name_url = 'https://www.name-generator.org.uk/quick/'
bot_username_url = 'https://jimpix.co.uk/words/username-generator.asp'
# SIGN_IN
sign_in_url = 'https://audius.co/signin'
# SIGN_UP
sign_up_url = 'https://audius.co/signup'
# XPATHS AND CLASS NAMES
# BOT CREATION
bot_quick_name_classname = 'name_heading'
bot_username_search_field_xPath = '//input[@type="text"]'
bot_username_search_button_xPath = '//button[@type="submit"]'
# SIGN_IN
sign_in_email_xPath = '//input[@name="email"]'
sign_in_password_xPath = '//input[@name="password"]'
# SIGN_UP
sign_up_email_xPath = '//input[@type="email"]'
sign_up_email_continue_xPath = '//button[@name="continue"]'
sign_up_password_one_xPath = '//input[@name="password"]'
sign_up_password_two_xPath = '//input[@name="confirmPassword"]'
sign_up_button_xPath = '//*[@id="page"]/div[2]/div[1]/form/div/div/button/span[1]'
sign_up_manual_button_xPath = '//*[@id="page"]/div[2]/div[1]/form/div/div/div[3]/div[1]/div/div[3]'
sign_up_username_xPath = '//input[@name="name"]'
sign_up_handle_xPath = '//input[@name="nickname"]'
sign_up_continue_button_xPath = '//button[@name="continue"]'
sign_up_choose_for_me_button_xPath = '//*[@id="page"]/div[2]/div[1]/form/div/div/div[3]/div[1]/div[2]/div/div/div/div[1]/div'
sign_up_submit_button_xPath = '//*[@id="page"]/div[2]/div[1]/form/div/div/button/span[1]'
# ARTIST FOLLOW ! not currently implemented fully !
artist_follow_button_xPath = ''
# TRACK LIKE
track_like_current_playing_xPath = '//*[@id="root"]/div/div[5]/div[2]/div/div[3]/div[1]/span/div'
track_like_from_track_page_xPath = '//button[@name="favorite"]'
# TRACK REPOST
track_repost_from_track_page_xPath = '//button[@name="repost"]'
# STREAM TRACK
track_play_buttom_xPath = '//button[@name="play"]'