#!/usr/bin/env python3

from sys import argv

script, dictpath, crosswordpath = argv

# Setting Min and Max length of a word
MIN_LEN = 4
MAX_LEN = 10

# Loading dictionary of words
def get_words():
    with open(dictpath) as f:
        words = f.read().split('\n')
        return words

# Parse crossword input
def get_crossword():
    crossword = []
    with open(crosswordpath) as f:
        for line in f:
            crossword.append(list(line[:-1]))
    return crossword

# 8 following functions are trying to find words that start from the current letter
def up(i, j):
    word = ''
    result = dict()
    for k in range(MAX_LEN):
        if i - k < 0:
            break
        try:
            word += crossword[i-k][j]
        except:
            break
        if (MIN_LEN <= len(word) <= MAX_LEN) and word.upper() in words:
            result[word] = [i+1, j+1, k+1, 'up']
    return result

def down(i, j):
    word = ''
    result = dict()
    for k in range(MAX_LEN):
        try:
            word += crossword[i+k][j]
        except:
            break
        if (MIN_LEN <= len(word) <= MAX_LEN) and word.upper() in words:
            result[word] = [i+1, j+1, k+1, 'down']
    return result

def right(i, j):
    word = ''
    result = dict()
    for k in range(MAX_LEN):
        try:
            word += crossword[i][j+k]
        except:
            break
        if (MIN_LEN <= len(word) <= MAX_LEN) and word.upper() in words:
            result[word] = [i+1, j+1, k+1, 'right']
    return result

def left(i, j):
    word = ''
    result = dict()
    for k in range(MAX_LEN):
        if j - k < 0:
            break
        try:
            word += crossword[i][j-k]
        except:
            break
        if (MIN_LEN <= len(word) <= MAX_LEN) and word.upper() in words:
            result[word] = [i+1, j+1, k+1, 'left']

    return result

def right_up(i, j):
    word = ''
    result = dict()
    for k in range(MAX_LEN):
        if i - k < 0:
            break
        try:
            word += crossword[i-k][j+k]
        except:
                break
        if (MIN_LEN <= len(word) <= MAX_LEN) and word.upper() in words:
            result[word] = [i+1, j+1, k+1, 'right_up']
    return result

def right_down(i, j):
    word = ''
    result = dict()
    for k in range(MAX_LEN):
        try:
            word += crossword[i+k][j+k]
        except:
            break
        if (MIN_LEN <= len(word) <= MAX_LEN) and word.upper() in words:
            result[word] = [i+1, j+1, k+1, 'right_down']
    return result

def left_up(i, j):
    word = ''
    result = dict()
    for k in range(MAX_LEN):
        if i - k < 0 or j - k < 0:
            break
        try:
            word += crossword[i-k][j-k]
        except:
            break
        if (MIN_LEN <= len(word) <= MAX_LEN) and word.upper() in words:
            result[word] = [i+1, j+1, k+1, 'left_up']
    return result

def left_down(i, j):
    word = ''
    result = dict()
    for k in range(MAX_LEN):
        if j - k < 0:
            break
        try:
            word += crossword[i+k][j-k]
        except:
            break
        if (MIN_LEN <= len(word) <= MAX_LEN) and word.upper() in words:
            result[word] = [i+1, j+1, k+1, 'left_down']

    return result

def work(crossword):
    result = []
    for i in range(len(crossword)):             # line
        for j in range(len(crossword)):         # column
            temp = [up(i, j), down(i, j), right(i, j), left(i, j),
              right_up(i, j), right_down(i, j), left_up(i, j), left_down(i, j)]
            for x in temp:
                if x:
                    result.append(x)
    final = dict()
    for x in result:
        keys = list(x)
        for key in keys:
            final[key] = x[key]
    return final

if __name__ == '__main__':
    words = get_words()
    crossword = get_crossword()
    print(work(crossword))
