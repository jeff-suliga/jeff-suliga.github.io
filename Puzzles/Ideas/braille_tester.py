import random
from time import time
import os

path_to_txt = os.getcwd() + '\\Puzzles\\Ideas\\braille_record.txt'

def records(elapsed_time):
    curr_times = []
    with open(path_to_txt, 'r') as f:
        i = 0
        for line in f.readlines():
            curr_times.append(float(line.strip()))
            i += 1
        if elapsed_time < curr_times[9]:
            if elapsed_time < curr_times[0]:
                print('New Record! By ' + str(curr_times[0] - elapsed_time) + ' seconds.')
            else:
                for i in range(1, 10):
                    if elapsed_time < curr_times[i]:
                        print('This time is now in position: ' + str(i + 1))
                        print('You were ' + str(elapsed_time - curr_times[0]) + ' seconds slower than the record')
                        print('You were ' + str(elapsed_time - curr_times[i-1]) + ' seconds slower than position ' + str(i))
                        print('\nCurrent Record: \t' + str(curr_times[0]))
                        print('Position ' + str(i) + ': \t\t' + str(curr_times[i-1]))
                        break
            curr_times.append(elapsed_time)
        else:
            print('You were ' + str(elapsed_time - curr_times[0]) + ' seconds slower than the record')
            print('You were ' + str(elapsed_time - curr_times[9]) + ' seconds slower than 10th place')

    curr_times.sort()
    with open(path_to_txt, 'w') as f:
        for i in range(9):
            f.write(str(curr_times[i]) + '\n')
        f.write(str(curr_times[9]))

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
        records(elapsed_time)

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