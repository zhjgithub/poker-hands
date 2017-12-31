import poker


def hand_percentages(n=700 * 1000):
    '''
    Sample n random hands and print a table of percentages for each type of hand.
    It could be run very long time, so decrease the parameter.
    '''
    counts = [0] * 11
    for i in range(n // 10):
        for hand in poker.deal(10):
            ranking = poker.hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(11)):
        print('%d: %6.3f %%' % (i, 100.0 * counts[i] / n))


if __name__ == '__main__':
    hand_percentages()
