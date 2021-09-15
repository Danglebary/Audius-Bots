# GENERAL IMPORTS
from datetime import datetime, timedelta
from random import randint


# CHOOSE RANDOM AGE AND BIRTH DATE BETWEEN MIN AND MAX AGE RANGE,
# RETURN BIRTH DATE
def gen_birthdate(max_age: int) -> str:
    min_age: int = 18
    date_format: str = "%m-%d-%Y"
    birth_time: datetime = datetime.today() - timedelta(
        days=randint(365 * min_age, 365 * max_age)
    )
    birth_date: str = birth_time.strftime(date_format)
    return birth_date
