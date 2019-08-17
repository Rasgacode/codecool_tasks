def hand_score(hand):
    poker_dict = {
    "55555": "five",
    "14444": "four",
    "11333": "three",
    "11122": "pair",
    "12222": "twopair",
    "22333": "fullhouse",
    "11111": "nothing"
    }
    return poker_dict["".join(sorted([str(hand.count(card)) for card in hand]))]
    
    

    