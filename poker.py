#! python3
'''
Poker hands
'''

import random

mydeck = [r + s for r in '23456789TJQKA' for s in 'SHDC']


def deal(numhands, n=5, deck=mydeck):
    '''
    Shuffle the deck and deal out numhands n-cards hands.
    '''
    random.shuffle(deck)
    return [deck[n * i:n * (i + 1)] for i in range(numhands)]


def poker(hands):
    '''
    Return a list of winning hands: poker([hand,...]) => hand
    '''
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    '''
    Return a list of all items equal to the max of the iterable.
    '''
    key = key or (lambda x: x)
    result, maxval = [], None
    for elem in iterable:
        keyval = key(elem)
        if not result or keyval > maxval:
            result, maxval = [elem], keyval
        elif keyval == maxval:
            result.append(elem)
    return result


count_rankings = {
    (5, ): 10,
    (4, 1): 7,
    (3, 2): 6,
    (3, 1, 1): 3,
    (2, 2, 1): 2,
    (2, 1, 1, 1): 1,
    (1, 1, 1, 1, 1): 0
}


def hand_rank(hand):
    '''
    Return a value indicating how high the hand ranks.
    counts is the count of each rank; ranks lists corresponding ranks.
    E.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)

    '''
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for r, s in hand])) == 1
    return max(count_rankings[counts], 5 * flush + 4 * straight), ranks


def group(items):
    '''
    Return a list of [(count, x)...], highest count first, then highest x first.
    '''
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)


def unzip(pairs):
    return zip(*pairs)


def test():
    '''
    Test cases for the function in poker program
    '''
    sf = "6C 7C 8C 9C TC".split()  # straight flush
    fk = "9D 9H 9S 9C 7D".split()  # four of a kind
    fh = "TD TC TH 7C 7D".split()  # full house
    tp = "5S 5D 9H 9C 6S".split()  # two pairs
    s1 = "AS 2S 3S 4S 5C".split()  # A-5 straight
    s2 = "2C 3C 4C 5S 6S".split()  # 2-6 straight
    ah = "AS 2S 3S 4S 6C".split()  # A high
    sh = "2S 3S 4S 6D 7D".split()  # 7 high

    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([fh]) == [fh]
    assert poker([sf] + 99 * [fh]) == [sf]
    assert poker([s1, s2, ah, sh]) == [s2]
    assert poker([s1, ah, sh]) == [s1]

    assert hand_rank(sf) == (9, (10, 9, 8, 7, 6))
    assert hand_rank(fk) == (7, (9, 7))
    assert hand_rank(fh) == (6, (10, 7))

    return 'tests pass'


print(test())
