import random

AMOUNT = 100000
WORDS = []

with open('WordList.txt', 'r') as file:
    for line in file:
        WORDS.append(line.strip())

with open('RandomNumbers.txt', 'w') as file:
    for i in range(AMOUNT):
        file.write(str(random.randint(0, len(WORDS) - 1)) + '\n')