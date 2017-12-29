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
