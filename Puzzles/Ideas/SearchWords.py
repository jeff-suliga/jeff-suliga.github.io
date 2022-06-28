def check(word):
    for letter in word:
        if letter not in soil_letters:
            return 0
    valid_words.append(word)

soil_letters = ['o', 'a', 'e', 'b', 'c', 'r']
valid_words = []

with open('Puzzles/Ideas/WordList.txt', encoding='utf-8') as wordlist:
    words = wordlist.readlines()

    for word in words:
        check(word.strip().lower())

with open('Puzzles/Ideas/Soil.txt', 'a') as out:
    for word in valid_words:
        out.write(word + '\n')