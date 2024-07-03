import random


def get_random_character():
    with open('static/heroes.txt', 'r') as f:
        characters = f.readlines()
    return random.choice(characters).strip()
