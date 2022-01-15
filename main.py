# GENERAL IMPORTS
from multiprocessing import Pool

# CUSTOM IMPORTS
from custom_types import BotData
from database import query_first_x_bots
from bot_routines import bot_routine_one

# MULTI-THREADED MULTI-BOT PROCESS FUNCTION.

if __name__ == "__main__":
    import multiprocessing as mp

    bot_list: list[BotData] = query_first_x_bots(1)
    pool: Pool = mp.Pool(len(bot_list))
    results = pool.starmap(bot_routine_one, bot_list)
    print(results)
