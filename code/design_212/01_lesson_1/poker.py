def deal(numhands, n=5):
    pass


def poker(hands):
    "return the highest ranked hand out of a list of hands"
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    m = iterable[iterable.index(max(iterable, key=key))]
    return [item for item in iterable if hand_rank(item) == hand_rank(m)]


def hand_rank(hand):
    "assign a rank to a given hand. returns a tupel (rank, tie breaker(s))"
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)


def card_ranks(hand):
    "extracts the card ranks of a hand as integers and returns them sorted in\
    descending order"
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def straight(ranks):
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    return len(set([s for r, s in hand])) == 1


def kind(n, ranks):
    for card in ranks:
        if ranks.count(card) == n:
            return card
    return None


def two_pair(ranks):
    first_match = kind(2, ranks)
    if first_match:
        second_match = kind(2, [rank for rank in ranks if rank != first_match])
        if second_match:
            return (first_match, second_match)
    return None


def test():
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split()

    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    assert card_ranks(sf) == [10,9,8,7,6]
    assert card_ranks(fk) == [9,9,9,9,7]
    assert card_ranks(fh) == [10,10,10,7,7]

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False

    assert flush(sf) == True
    assert flush(fk) == False

    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9, 5)

    return "tests pass"

print(poker([['6C', '7C', '8C', '9C', 'TC'], ['6D', '7D', '8D', '9D', 'TD'], ['9D', '9H', '9S', '9C', '7D'], ['TD', 'TC', 'TH', '7C', '7D']]))
