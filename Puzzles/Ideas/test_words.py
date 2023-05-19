# ALPHA = [*'abcdefghijklmnopqrstuvwxyz']
ALPHA = [*'answer']

def compute(word: str):
    length = len(word)
    if length < 5 or length > 9:
        return False
    
    letters = []
    for letter in word:
        if letter in letters:
            return False
        elif letter not in ALPHA:
            return False
        letters.append(letter)
        
    return True

with open('WordList.txt', 'r', encoding='utf-8') as file:
    for line in file:
        word = line.strip()
        if compute(word):
            print(word)
