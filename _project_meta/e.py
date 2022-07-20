with open('language_words.txt') as f:
    lines = [
        line.strip()
        for line in
        f.readlines()
    ]
    nouns = sorted(list(set([
        line.replace("NOUN:","")[line.replace("NOUN:","").index(":")+ 1:-1] + "\n"
        for line in lines
        if "NOUN:" in line
    ])))

with open('nouns.txt', 'w') as g:
    g.writelines(nouns)
    
            