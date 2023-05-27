import playing_cards
import person

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
    
