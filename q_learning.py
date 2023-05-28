import playing_cards
import person
import random

def get_q_row(player: person.Player, dealer: person.Dealer, deck: playing_cards.Deck):
    true_count = round(deck.runningCount / (deck.len/52))
    is_first_two = len(player.hand)
    is_soft = player.soft_hand
    is_splittable = player.splittable
    if is_splittable:
        return player.q_table[0][player.hand[0].gameValue - 1][dealer.dealer_card.gameValue - 1][true_count + abs(list(person.RANGE_TRUE_COUNT)[0])]
    elif is_soft and is_first_two:
        return player.q_table[1][player.hand_value - 2][dealer.dealer_card.gamerValue - 1][true_count + abs(list(person.RANGE_TRUE_COUNT)[0])]
    elif is_first_two:
        return player.q_table[2][player.hand_value - 5][dealer.dealer_card.gamerValue - 1][true_count + abs(list(person.RANGE_TRUE_COUNT)[0])]
    elif is_soft:
        return player.q_table[3][player.hand_value - 4][dealer.dealer_card.gamerValue - 1][true_count + abs(list(person.RANGE_TRUE_COUNT)[0])]
    else:
        return player.q_table[4][player.hand_value - 6][dealer.dealer_card.gamerValue - 1][true_count + abs(list(person.RANGE_TRUE_COUNT)[0])]
    
def e_greedy_selection(q_values, epsilon):
    r = random.uniform(0.0, 1.0)
    idx = 1
    max_q = q_values[0]
    max_q_idx = 0
    while idx < len(q_values):
        if q_values[idx] > max_q:
            max_q = q_values[idx]
            max_q_idx = idx
        idx += 1
    if r < epsilon:
        d = person.DECISION.copy()
        d.pop(max_q_idx)
        return random.choice(d)
    else:
        return person.DECISION[max_q_idx]