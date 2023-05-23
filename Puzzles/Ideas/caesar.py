from words.binary_search_words import wordInList, getWords

ALPHA = [*'abcdefghijklmnopqrstuvwxyz']
SIZE = len(ALPHA)

VOWELS = [*'aeiuoy']

def shift(word: str, shiftAmt: int):
    newWord = ''
    for letter in word:
        if letter in ALPHA:
            newWord += ALPHA[(ALPHA.index(letter) + shiftAmt) % SIZE]
        else:
            newWord += letter
    return newWord

WORDLIST = getWords()

count = 0    
for word in WORDLIST:
    for shiftAmt in range(1, 14):
        newWord = shift(word, shiftAmt)
        if wordInList(newWord):
            print(str(count) + '\t\t:\t', f'{word}\t\t{shiftAmt}->\t{newWord}')
            count += 1