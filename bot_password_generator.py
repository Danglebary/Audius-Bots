# GENERAL IMPORTS
import random, string

# FUNCTION TO GENERATE RANDOM PASSWORD FOR BOT WITH 16 RANDOM CHARACTERS
def gen_bot_pass() -> str:
    pass_chars: str = "".join(
        [
            string.ascii_lowercase,
            string.ascii_uppercase,
            string.digits,
            string.punctuation,
        ]
    )
    password: list[str] = []
    for _ in range(16):
        password.append(random.choice(pass_chars))
    full_pass = "".join(password)
    return full_pass
