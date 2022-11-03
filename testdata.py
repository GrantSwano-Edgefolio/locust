import random

# Add a list of Fund IDs to randomly select from
FUND_IDS = []


def get_random_fund():
    return random.choice(FUND_IDS)
