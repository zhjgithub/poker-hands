#! python3
'''
Poker hands
'''


def poker(hands):
    '''
    Return the best hand: poker([hand,...]) => hand
    '''
    return max(hands, key=abs)
