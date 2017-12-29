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


def card_ranks(hand):
    '''
    Return card ranks.
    '''
    return []


def straight(ranks):
    '''
    Return true if ranks are straight.
    '''
    return True


def flush(hand):
    '''
    Return true if hand is flush.
    '''
    return True


def kind(type, ranks):
    '''
    Return type of a kind number.
    '''
    return 0


def test():
    '''
    Test cases for the function in poker program
    '''
    sf = "6C 7C 8C 9C TC".split()  # straight flush
    fk = "9D 9H 9S 9C 7D".split()  # four of a kind
    fh = "TD TC TH 7C 7D".split()  # full house

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([fh]) == fh
    assert poker([sf] + 99 * [fh]) == sf

    return 'tests pass'


print test()
