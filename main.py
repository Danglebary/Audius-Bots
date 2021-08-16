# DB FUNCTION IMPORTS
from database import query_first_x_bots

# FUNCTION IMPORTS
from bot_routines import bot_routine_one

# MULTI-THREADED MULTI-BOT PROCESS FUNCTION.
# ! CAREFUL, NOT EXACTLY SURE HOW MANY BOTS SHOULD BE RAN AT A TIME !
# I USE 4 TO BE SAFE, AS THE ORIGINAL COMPUTER I WROTE THIS ON HAD A TOTAL OF 4 CORES.
# IN THEORY, IT SHOULD BE ABLE TO RUN UP TO 1 BOT PER THREAD OF A GIVEN CPU,
# BUT I HAVE NOT FULLY TESTED THIS.

if __name__ == "__main__":
    import multiprocessing as mp
    bot_list = query_first_x_bots(8)
    first_bot_set = [bot_list[0], bot_list[1], bot_list[2], bot_list[3]]
    second_bot_set = [bot_list[4], bot_list[5], bot_list[6], bot_list[7]]
    pool = mp.Pool(len(bot_list))
    results = pool.starmap(bot_routine_one, first_bot_set)
    print(results)