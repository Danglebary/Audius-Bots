import sys

def handle_api_error(data, e):
    print(f'ERROR: could not fetch {data} from Audius API')
    sys.exit(e)

def handle_resolve_data_error(data, e):
    print(f'ERROR: {data} could not be found in resolved data from Audius API')
    sys.exit(e)

def handle_db_insert_artist_error(data, e):
    print(f'ERROR: Artist data for {data} could not be written to database')
    sys.exit(e)

def handle_db_insert_track_error(data, e):
    print(f'ERROR: Track data for {data} could not be written to database')
    sys.exit(e)

def handle_db_insert_bot_error(data, e):
    print(f'ERROR: Bot data for {data} could not be written to database')
    sys.exit(e)

def handle_browser_element_xpath_keystroke_error(bot_name, data, e):
    print(f'{bot_name} : ERROR -> {data}')
    sys.exit(e)

def handle_browser_element_xpath_click_error(bot_name, data, e):
    print(f'{bot_name} : ERROR -> {data}')

def handle_browser_navigation_error(bot_name, data, e):
    print(f'{bot_name} : ERROR -> could not navigate to {data}')
    sys.exit(e)