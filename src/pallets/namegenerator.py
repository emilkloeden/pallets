import random

try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files

resources = files("pallets")
adjective_file_data = (resources / "resources" / "adjectives.txt").read_bytes().decode('utf-8')
noun_file_data = (resources / "resources" / "nouns.txt").read_bytes().decode('utf-8')
# with open('pallets', 'resources', 'adjectives.txt', 'r') as f:
adjectives = [adjective[0].upper() + adjective[1:].strip() for adjective in adjective_file_data.split('\n')]

# with open('pallets', 'resources', 'nouns.txt', 'r') as f:
nouns = [noun[0].upper() + noun[1:].strip() for noun in noun_file_data.split('\n')]
    
def generate_name():
    return f"{random.choice(adjectives)} {random.choice(nouns)}"