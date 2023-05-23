from binary_search_words import wordInList

nums = []
WORDS = []
WORDSCHECK = []

with open('WordList.txt', 'r') as file:
    for line in file:
        WORDS.append(line.strip())

with open('RandomNumbers.txt', 'r') as file:
    for line in file:
        num = int(line.strip())
        nums.append(num)
        WORDSCHECK.append(WORDS[num])

valid = True
for word in WORDSCHECK:
    if not wordInList(word):
        valid = False
print(valid)