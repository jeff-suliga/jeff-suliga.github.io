"""
Sorts the words in the WordList.txt text file alphabetically.

Note that this will apply lower() to every string in the
words file, making every word lowercase
"""

WORDS = []

with open('WordList.txt', 'r') as file:
    for line in file:
        WORDS.append(line.strip().lower())

def splitList(values):
    size = len(values) // 2
    return values[:size], values[size:]

def combine(A, B):
    C = []
    while len(A) and len(B):
        a = A[0]
        b = B[0]
        if a < b:
            C.append(a)
            A.remove(a)
        else:
            C.append(b)
            B.remove(b)
    if len(A):
        C += A
    elif len(B):
        C+= B
    return C

def mergeSort(values):
    if len(values) == 1:
        return values
    A, B = splitList(values)
    return combine(mergeSort(A), mergeSort(B))

# merge sort the list
WORDS = mergeSort(WORDS)

with open('NewWordList.txt', 'w') as file:
    for word in WORDS:
        file.write(word + '\n')
