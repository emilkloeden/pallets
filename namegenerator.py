import random

with open('adjectives.txt', 'r') as f:
    adjectives = [adjective[0].upper() + adjective[1:].strip() for adjective in f.readlines()]

with open('nouns.txt', 'r') as f:
    nouns = [noun[0].upper() + noun[1:].strip() for noun in f.readlines()]
    
def generate_name():
    return f"{random.choice(adjectives)} {random.choice(nouns)}"