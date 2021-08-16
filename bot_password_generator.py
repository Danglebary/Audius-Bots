# INIT GENERAL IMPORTS
import random, string

# FUNCTION TO GENERATE RANDOM PASSWORD FOR BOT WITH 16 RANDOM CHARACTERS
def gen_bot_pass():
    pass_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = []
    for _ in range(16):
        password.append(random.choice(pass_chars))
    full_pass = ''.join(password)
    return full_pass