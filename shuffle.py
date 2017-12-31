'''
Shuffle even probability for each permutation.
'''

from random import randrange
import collections
import math


def shuffle(deck):
    '''
    Knuth's Algorithm P.
    '''
    N = len(deck)
    for i in range(N - 1):
        swap(deck, i, randrange(i, N))


def shuffle1(deck):
    '''
    Not a good algorithm.
    '''
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = randrange(N), randrange(N)
        swapped[i] = True
        swap(deck, i, j)


def shuffle2(deck):
    '''
    Another shuffle function for comparasion.
    '''
    N = len(deck)
    for i in range(N):
        swap(deck, i, randrange(N))


def swap(deck, i, j):
    '''
    Swap elements i and j of a collection.
    '''
    deck[i], deck[j] = deck[j], deck[i]


def test_shuffler(shuffler, deck='abcd', n=100000):
    counts = collections.defaultdict(int)
    for _ in range(n):
        inputs = list(deck)
        shuffler(inputs)
        counts[''.join(inputs)] += 1
    e = n * 1.0 / math.factorial(len(deck))
    ok = all(0.9 <= counts[item] / e <= 1.1 for item in counts)
    name = shuffler.__name__
    print('%s(%s)%s' % (name, deck, 'ok' if ok else '*** BAD ***'))
    for item, count in sorted(counts.items()):
        print('%s:%4.1f' % (item, count * 100.0 / n))


def test_shufflers(shufflers=[shuffle, shuffle1], decks=['abc', 'ab']):
    for deck in decks:
        for f in shufflers:
            test_shuffler(f, deck)


if __name__ == '__main__':
    test_shufflers()
