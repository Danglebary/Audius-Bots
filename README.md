# Audius_Bots

Multi-threaded web scraping and automation tool for block-chain streaming service Audius.co.

This project was a test to see if somewhat more "life-like" streaming bots could be made and used for streaming on the Audius platform. The bots stream more than just one artist, and more than just the targeted "Special artists", as to seem more human. Currently setup to stream the "Special artists" for 62% of all uptime, randomly selecting songs from other artists to play in between. The more robust and diverse the catalog of extra artists, the more genuine the bots will seem.

# Disclaimers:

* The database has been excluded from this repository, and will need to be created and populated before running in order to function.
* Because this program uses selenium and send_keys to operate, the machine you run this on will not be usable while the program is running, or else the processes could get off-track. Best to run on a machine you don't plan on using for a few hours.
* This repository is being shared as-is. I do not currently have plans to update it very regularly as it is not a program I run for personal gain, but was created more as a proof-of-concept.

# Getting started:

* Make sure selenium is installed
* Create an sqlite3 database named "data.db" in root directory
* Open "config.py"
    * Set "init_nBots" to the number of bots you would like to initially create
    * Add Audius artist usernames to the list "init_extra_artists", this is a list of all artists outside of the special artists, the more artists the better.
    * Add Audius artist usernames to the list "special_artists", this is a list of the artists you would like to stream more than others.
* Run "initial_setup.py" to complete setup
* Run main program by running "main.py"
* Periodically run "sync_db_tracks_for_all_artists" function from the file "sync_db_data" to get updated track-lists for each artist. Then run "sync_track_urls_to_db" function from the file of the same name to update track urls as well.
