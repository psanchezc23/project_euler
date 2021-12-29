import os
import time


CARDS_ORDER = [
    "A",
    "K",
    "Q",
    "J",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2"
]
N_CARDS = len(CARDS_ORDER)
CARDS_VALUE = dict(zip(CARDS_ORDER, range(N_CARDS)[::-1]))


def _is_royal(numbers_occurrences):
    return set(numbers_occurrences.keys()) == set(CARDS_ORDER[:5])


def _is_straight(numbers_occurrences):
    if len(numbers_occurrences.keys()) == 5:
        cards_values = [CARDS_VALUE[c] for c in numbers_occurrences.keys()]
        return max(cards_values) - min(cards_values) == 4
    return False


def _is_four_of_a_kind(numbers_occurrences):
    if len(numbers_occurrences.keys()) != 2:
        return False
    return any([v == 4 for v in numbers_occurrences.values()])


def _is_full_house(numbers_occurrences):
    if len(numbers_occurrences.keys()) != 2:
        return False
    return any([v == 3 for v in numbers_occurrences.values()])


def _is_three_of_a_kind(numbers_occurrences):
    if len(numbers_occurrences.keys()) != 3:
        return False
    return any([v == 3 for v in numbers_occurrences.values()])


def _is_two_pairs(numbers_occurrences):
    return len([k for k, v in numbers_occurrences.items() if v == 2]) == 2


def _is_one_pairs(numbers_occurrences):
    return len([k for k, v in numbers_occurrences.items() if v == 2]) == 1


def _get_ordered_cards_values(numbers_occurrences, hand_score):
    """
    Ordered cards values following poker rules for ties:
    - Royal Flush, Straight Flush, Flush, Straight and High Card ordered from
    highest to lowest card number.
    - Four of a Kind ordered as AAAAB.
    - Full house ordered as AAABB.
    - Three of a Kind ordered as AAABC where BC are ordered from highest to
    lowest card number.
    - Two pairs ordered as AABBC where AABB are ordered from highest to lowest
    card number.
    - One pair ordered as AABCD where BCD are ordered from highest to lowest
    card number.

    :param numbers_occurrences: Dictionary with the card numbers of the hand
    and their number of occurrences.
    :type numbers_occurrences: dict[int]
    :param hand_score: Hand score.

    :return: ordered cards values following poker rules for ties.
    :rtype: list[int]
    """

    # Royal Flush, Straight Flush, Flush, Straight and High Card order
    if hand_score in [9, 8, 5, 4, 0]:
        ordered_cards = []
        for c in CARDS_ORDER:
            if c in numbers_occurrences:
                ordered_cards.append(c)

    # Four of a kind
    elif hand_score == 7:
        ordered_cards = \
            [k for k, v in numbers_occurrences.items() if v == 4] * 4
        ordered_cards += [k for k, v in numbers_occurrences.items() if v == 1]

    # Full house
    elif hand_score == 6:
        ordered_cards = \
            [k for k, v in numbers_occurrences.items() if v == 3] * 3
        ordered_cards += \
            [k for k, v in numbers_occurrences.items() if v == 2] * 2

    # Three of a kind
    elif hand_score == 3:
        ordered_cards = \
            [k for k, v in numbers_occurrences.items() if v == 3] * 3
        for c in CARDS_ORDER:
            if numbers_occurrences.get(c):
                ordered_cards.append(c)

    # Two pairs
    elif hand_score == 2:
        ordered_cards = []
        single_card = ""
        for c in CARDS_ORDER:
            if numbers_occurrences.get(c, 0) == 2:
                ordered_cards += [c] * 2
            elif c in numbers_occurrences:
                single_card = c
        ordered_cards.append(single_card)

    # One pair
    else:
        ordered_cards = \
            [k for k, v in numbers_occurrences.items() if v == 2] * 2
        for c in CARDS_ORDER:
            if numbers_occurrences.get(c, 0) == 1:
                ordered_cards.append(c)

    ordered_cards_values = [CARDS_VALUE[c] for c in ordered_cards]
    return ordered_cards_values


def _get_hand(cards):
    """
    - 0. High Card: Highest value card.
    - 1. One Pair: Two cards of the same value.
    - 2. Two Pairs: Two different pairs.
    - 3. Three of a Kind: Three cards of the same value.
    - 4. Straight: All cards are consecutive values.
    - 5. Flush: All cards of the same suit.
    - 6. Full House: Three of a kind and a pair.
    - 7. Four of a Kind: Four cards of the same value.
    - 8. Straight Flush: All cards are consecutive values of same suit.
    - 9. Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

    :param cards: String with cards of both players

    :return score: Score for player's hand
    :rtype score: int
    :return cards_values: Ordered cards values following the poker rules.
    :rtype cards_values: List[int]
    """

    numbers_occurrences = {}
    flush = True
    first_suit = cards[0][1]
    for number, suit in cards:
        numbers_occurrences[number] = numbers_occurrences.get(number, 0) + 1
        flush &= first_suit == suit

    # Same suit (Flush, Straight Flush, Royal Flush)
    hand_score = 0
    if flush and _is_royal(numbers_occurrences):
        hand_score = 9
    elif flush and _is_straight(numbers_occurrences):
        hand_score = 8
    elif _is_four_of_a_kind(numbers_occurrences):
        hand_score = 7
    elif _is_full_house(numbers_occurrences):
        hand_score = 6
    elif flush:
        hand_score = 5
    elif _is_straight(numbers_occurrences):
        hand_score = 4
    elif _is_three_of_a_kind(numbers_occurrences):
        hand_score = 3
    elif _is_two_pairs(numbers_occurrences):
        hand_score = 2
    elif _is_one_pairs(numbers_occurrences):
        hand_score = 1

    cards_values = _get_ordered_cards_values(numbers_occurrences, hand_score)
    return hand_score, cards_values


def _is_player_1_winner(cards):
    hand_1_score, hand_1_cards_values = _get_hand(cards[:5])
    hand_2_score, hand_2_cards_values = _get_hand(cards[5:])

    if hand_1_score > hand_2_score:
        return 1

    elif hand_1_score == hand_2_score:
        for card_1, card_2 in zip(hand_1_cards_values, hand_2_cards_values):
            if card_1 > card_2:
                return 1
            elif card_2 > card_1:
                return 0
    return 0


def exercise_054():
    """
    In the card game poker, a hand consists of five cards and are ranked, from
    lowest to highest, in the following way:

    - High Card: Highest value card.
    - One Pair: Two cards of the same value.
    - Two Pairs: Two different pairs.
    - Three of a Kind: Three cards of the same value.
    - Straight: All cards are consecutive values.
    - Flush: All cards of the same suit.
    - Full House: Three of a kind and a pair.
    - Four of a Kind: Four cards of the same value.
    - Straight Flush: All cards are consecutive values of same suit.
    - Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

    The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

    If two players have the same ranked hands then the rank made up of the
    highest value wins; for example, a pair of eights beats a pair of fives
    (see example 1 below). But if two ranks tie, for example, both players
    have a pair of queens, then highest cards in each hand are compared (see
    example 4 below); if the highest cards tie then the next highest cards are
    compared, and so on.

    Consider the following five hands dealt to two players:

    Hand	Player 1	 	   Player 2	 	        Winner
    1	 	5H 5C 6S 7S KD     2C 3S 8S 8D TD       Player 2
            Pair of Fives      Pair of Eights

    2	 	5D 8C 9S JS AC     2C 5C 7D 8S QH       Player 1
            Highest card Ace   Highest card Queen

    3	 	2D 9C AS AH AC     3D 6D 7D TD QD       Player 2
            Three Aces         Flush with Diamonds

    4	 	4D 6S 9H QH QC     3D 6D 7H QD QS       Player 1
            Pair of Queens     Pair of Queens
            Highest card Nine  Highest card Seven

    5	 	2H 2D 4C 4D 4S     3C 3D 3S 9S 9D       Player 1
            Full House         Full House
            With Three Fours   with Three Threes

    The file, poker.txt, contains one-thousand random hands dealt to two
    players. Each line of the file contains ten cards (separated by a single
    space): the first five are Player 1's cards and the last five are Player
    2's cards. You can assume that all hands are valid (no invalid characters
    or repeated cards), each player's hand is in no specific order, and in
    each hand there is a clear winner.

    How many hands does Player 1 win?

    :return: Number of hands that Player 1 wins
    :rtype: int
    """

    file_path = os.path.join(
        os.path.dirname(__file__), "files/exercise_054.txt"
    )
    wins_player_1 = 0
    with open(file_path, "r") as f:
        for line in f.readlines():
            cards = line.replace("\n", "").split(" ")
            wins_player_1 += _is_player_1_winner(cards)
    return wins_player_1


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_054())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))
