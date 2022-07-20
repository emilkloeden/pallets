with open('language_words.txt') as f:
    lines = [
        line.strip()
        for line in
        f.readlines()
    ]
    adjectives = sorted(list(set([
        line[5:-1] + "\n"
        for line in lines
        if "ADJ:" in line
    ])))

with open('adjectives.txt', 'w') as g:
    g.writelines(adjectives)
    
            