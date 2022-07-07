import random
from time import time
import os

path_to_txt = os.getcwd() + '\\Puzzles\\Ideas\\braille_record.txt'

def braille(pattern):
    print('-' * 9)
    c1 = 'x' if ('1' in pattern) else ' '
    c2 = 'x' if ('4' in pattern) else ' '
    print(f'| {c1} | {c2} |')
    print('-' * 9)
    c1 = 'x' if ('2' in pattern) else ' '
    c2 = 'x' if ('5' in pattern) else ' '
    print(f'| {c1} | {c2} |')
    print('-' * 9)
    c1 = 'x' if ('3' in pattern) else ' '
    c2 = 'x' if ('6' in pattern) else ' '
    print(f'| {c1} | {c2} |')
    print('-' * 9)

def prompt(num):
    print('-' * 40)
    print('\nWhat is this character?')
    braille(patterns[num])
    guess = input()
    
    if guess == letters[num]:
        print('\nCorrect!')
        return True
    else:
        print('\nIncorrect. The correct answer was ' + letters[num] + '.')
        return False

def start():
    nums = list(range(26))
    random.shuffle(nums)

    correct = 0
    missed = []

    start_time = time()

    for num in nums:
        if prompt(num):
            correct += 1
        else:
            missed.append(letters[num])

    end_time = time()
    elapsed_time = end_time - start_time

    print('*' * 40)
    print(f'Total Correct:     \t{correct}')
    print('Percentage Correct: \t', str(correct / 26))
    print('Missed Letters:')
    print(missed)

    print(f'\nElapsed Time (s): \t{elapsed_time}\n')

    if correct == 26:
        with open(path_to_txt, 'r') as f:
            best_time = float(f.readline().strip())
            if elapsed_time < best_time:
                print('New Record! By ' + str(best_time - elapsed_time) + ' seconds.')
                best_time = elapsed_time
            else:
                print('You were ' + str(elapsed_time - best_time) + ' seconds slower than the record')

        with open(path_to_txt, 'w') as f:
            f.write(str(best_time))

    if input('Again? (y)\n') == 'y':
        start()


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
patterns = [
    '1',        # a
    '12',       # b
    '14',       # c
    '145',      # d
    '15',       # e
    '124',      # f
    '1245',     # g
    '125',      # h
    '24',       # i
    '245',      # j
    '13',       # k
    '123',      # l
    '134',      # m
    '1345',     # n
    '135',      # o
    '1234',     # p
    '12345',    # q
    '1235',     # r
    '234',      # s
    '2345',     # t
    '136',      # u
    '1236',     # v
    '2456',     # w
    '1346',     # x
    '13456',    # y
    '1356',     # z
]

input("Press enter to start")
start()