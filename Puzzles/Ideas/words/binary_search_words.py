ALPHA = [*'abcdefghijklmnopqrstuvwxyz']
ALPHA_START = [] # This will hold the index of the first word in WordList that begins with each letter
WORDS = []

ALPHA_START.append(0) # The first word in WordList is the first word to start with 'a'
with open('WordList.txt', 'r') as file:
    i = 0
    idx = 0
    searching = ALPHA[i]
    for line in file:
        word = line.strip().lower()
        WORDS.append(word)
        if not word[0] == searching:
            i += 1
            ALPHA_START.append(idx)
            searching = ALPHA[i]
        idx += 1

def binary(low: int, high: int, target: str):
    mid = (low + high) // 2
    if WORDS[mid] == target:
        return mid
    if mid == low:
        return -1 if WORDS[high] != target else high
    
    return binary(low, mid - 1, target) if target < WORDS[mid] else binary(mid + 1, high, target)

def find(word: str):
    pos = ALPHA.index(word[0])
    low = ALPHA_START[pos]
    high = ALPHA_START[pos + 1] - 1 if pos < 25 else 456969
    return binary(low, high, word)

def wordInList(word: str):
    return find(word) != -1

def getWords():
    return WORDS
