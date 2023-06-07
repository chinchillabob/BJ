import unittest
import playing_cards
import person
import table

class MyTest(unittest.TestCase):
    def test_create_deck(self):
        d = playing_cards.Deck([])
        d.add_decks(1)
        self.assertEqual(d.frequencyDistrib[9], 16)
        self.assertEqual(len(d.cards), d.len)
    def test_deck_pull(self):
        d = playing_cards.Deck([])
        d.add_decks(2)
        first_card = d.cards[0]
        freq_dist_t_0 = d.frequencyDistrib.copy()
        pulled_card = d.pull()
        self.assertEqual(first_card, pulled_card)
        self.assertEqual(freq_dist_t_0[pulled_card.gameValue() - 1] - 1, d.frequencyDistrib[pulled_card.gameValue() - 1])
    def test_pay(self):
        p1 = person.Player([], 100, 0)
        bet_size = 20
        p1.pay(-bet_size)
        self.assertEqual(p1.money, 100 - bet_size)
    def test_hand_value(self):
        c = [playing_cards.Card('6', 'C'), playing_cards.Card('A', 'D')]
        p1 = person.Player(c, 100, 0)
        self.assertEqual(7, p1.hand_value())
    def test_get_dealer_decision(self):
        c = [playing_cards.Card('A', 'C'), playing_cards.Card('6', 'D')]
        d = person.Dealer(c, [], [])
        d.construct_hit_on_soft_17_dealer()
        decision = d.get_decision()
        self.assertEqual('HIT', decision)
    def test_set_frequencyDistrib(self):
        cards = [playing_cards.Card('K', 'D'), playing_cards.Card('T', 'C')]
        deck = playing_cards.Deck(cards)
        deck.set_frequencyDistrib()
        self.assertEqual(2, deck.frequencyDistrib[9])
    def test_pull(self):
        deck = playing_cards.Deck([])
        deck.add_decks(1)
        deck.shuffle()
        pulled_card = deck.pull()
        self.assertEqual(51, deck.len)
        self.assertEqual(3, deck.frequencyDistrib[pulled_card.gameValue() - 1] % 4)
    def test_pull_card_with_val(self):
        deck = playing_cards.Deck([])
        deck.add_decks(1)
        deck.shuffle()
        deck.pull_card_with_val(10)
        self.assertEqual(51, deck.len)
        self.assertEqual(15, deck.frequencyDistrib[9])
    def test_deal_and_reset(self):
        t = table.Table(playing_cards.Deck([]) , [person.Player([], 100, 0)], person.Dealer([], [], []))
        t.deck.add_decks(2)
        t.dealer.construct_hit_on_soft_17_dealer()
        t.deal()
        for pers in t.players + [t.dealer]:
            self.assertEqual(len(pers.hand), 2)
        self.assertEqual(len(t.dealer.hand), 2)
    
    def test_get_e_greedy(self):
        t = table.Table(playing_cards.Deck([]) , [person.Player([], 100, 0)], person.Dealer([], [], []))
        t.deck.add_decks(2)
        t.dealer.construct_hit_on_soft_17_dealer()
        t.deal()
        selection = t.players[0].get_e_greedy_selection(t.dealer, t.deck, 0.1)
        self.assertTrue(selection in person.DECISION)

    def test_max_q_accum(self): 
        t = table.Table(playing_cards.Deck([]) , [person.Player([], 100, 0)], person.Dealer([], [], []))
        t.deck.add_decks(2)
        t.dealer.construct_hit_on_soft_17_dealer()
        t.deck.shuffle()
        t.deal()
        t.deck.add_decks(2)
        t.dealer.construct_hit_on_soft_17_dealer()
        print(t.players[0].max_q_accum(t.dealer, t.deck))
    
    """
    def test_q_table(self):
        p = person.Player([], 100, 0)
        print(f"len(p.q_table) {len(p.q_table)}") #q tables
        print(f"len(p.q_table[1]) {len(p.q_table[1])}") #true count
        print(f"len(p.q_table[1][24]) {len(p.q_table[1][24])}") #dealer card
        print(f"len(p.q_table[1][24][1]) {len(p.q_table[1][24][1])}") #player hand value
        print(f"len(p.q_table[1][24][1][0]) {len(p.q_table[1][24][1][0])}") #q values
    """
        

if __name__ == '__main__':
    unittest.main()