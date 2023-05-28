import unittest
import playing_cards
import person

class MyTest(unittest.TestCase):
    def test_create_deck(self):
        d = playing_cards.Deck([])
        d.add_decks(2)
        self.assertEqual(52*2, d.len)
    def test_deck_pull(self):
        d = playing_cards.Deck([])
        d.add_decks(2)
        first_card = d.cards[0]
        pulled_card = d.pull
        self.assertEqual(first_card, pulled_card)
    def test_pay(self):
        p1 = person.Player([], 100, 0)
        bet_size = 20
        p1.pay(-bet_size)
        self.assertEqual(p1.money, 100 - bet_size)
    def test_hand_value(self):
        c = [playing_cards.Card('6', 'C'), playing_cards.Card('A', 'D')]
        p1 = person.Player(c, 100, 0)
        self.assertEqual(7, p1.hand_value())
    def test_get_decision(self):
        c = [playing_cards.Card('A', 'C'), playing_cards.Card('6', 'D')]
        d = person.Dealer([], [], c)
        d.construct_hit_on_soft_17_dealer()
        decision = d.get_decision()
        self.assertEqual('HIT', decision)


if __name__ == '__main__':
    unittest.main()