'''
Shuffle even probability for each permutation.
'''

import random


def shuffle(deck):
    '''
    Knuth's Algorithm P.
    '''
    N = len(deck)
    for i in range(N - 1):
        swap(deck, i, random.randrange(i, N))


def swap(deck, i, j):
    '''
    Swap elements i and j of a collection.
    '''
    deck[i], deck[j] = deck[j], deck[i]