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
    Return hand rank
    '''
    return None


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

    return 'tests pass'


print test()
