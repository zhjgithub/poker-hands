#! python3
'''
Poker hands
'''


def poker(hands):
    '''
    Return the best hand: poker([hand,...]) => hand
    '''
    return max(hands, key=hand_rank)


def hand_rank(hand):
    '''
    Return a value indicating the ranking of a hand.
    '''
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), kind(1, ranks))
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(hand):
    '''
    Return a list of the ranks, sorted with higher first.
    '''
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks


def straight(ranks):
    '''
    Return True if the ordered ranks form a 5-card straight.
    '''
    # return all(ranks[i] == ranks[i + 1] + 1 for i in range(len(ranks) - 1))
    return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5


def flush(hand):
    '''
    Return True if all the cards have the same suit.
    '''
    suits = [s for r, s in hand]
    # return len(set(suits)) == 1
    return suits.count(suits[0]) == len(suits)


def kind(kind_type, ranks):
    '''
    Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand.
    '''
    for rank in ranks:
        if ranks.count(rank) == kind_type:
            return rank


def two_pair(ranks):
    '''
    If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None.
    '''
    high_pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if high_pair and low_pair and high_pair != low_pair:
        return high_pair, low_pair


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

    fk_ranks = card_ranks(fk)
    tp_ranks = card_ranks(tp)

    assert kind(4, fk_ranks) == 9
    assert kind(3, fk_ranks) is None
    assert kind(2, fk_ranks) is None
    assert kind(1, fk_ranks) == 7

    assert two_pair(fk_ranks) is None
    assert two_pair(tp_ranks) == (9, 5)

    assert straight([9, 8, 7, 6, 5]) is True
    assert straight([9, 8, 8, 6, 5]) is False
    assert flush(sf) is True
    assert flush(fk) is False

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([fh]) == fh
    assert poker([sf] + 99 * [fh]) == sf
    assert poker([s1, s2, ah, sh]) == s2
    assert poker([s1, ah, sh]) == s1

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    return 'tests pass'


print test()