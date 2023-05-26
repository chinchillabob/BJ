import unittest
import playing_cards
import person

class MyTest(unittest.TestCase):
    def test_card_game_value(self):
        v = playing_cards.Card('K', 'C').gameValue()
        self.assertEqual(10, v)
    def test_deck_shuffle(self):
        vs = [playing_cards.Card('1', 'C').gameValue(), playing_cards.Card('2', 'C').gameValue(), playing_cards.Card('3', 'C').gameValue()]
        d = playing_cards.Deck(vs)
        d.shuffle()
        print(f"deck with values [1,2,3] shuffled to {d.cards}")
    def test_deck_pull(self):
        vs = [playing_cards.Card('1', 'C').gameValue(), playing_cards.Card('2', 'C').gameValue(), playing_cards.Card('3', 'C').gameValue()]
        num_cards = len(vs)
        d = playing_cards.Deck(vs)
        first_card = vs[0]
        self.assertEqual(first_card, d.pull())
        self.assertEqual(num_cards - 1, len(d.cards))
    def test_add_decks(self):
        num_decks = 3
        d = playing_cards.Deck([])
        d.addDecks(num_decks)
        self.assertEqual(len(d.cards), num_decks * 52)
    def test_pay(self):
        p1 = person.Player([], [], [], 100, [], [], 0)
        bet_size = 20
        p1.pay(-20)
        self.assertEqual(p1.money, 100 - 20)
    def test_hand_value(self):
        c = [playing_cards.Card('6', 'C'), playing_cards.Card('A', 'D')]
        p1 = person.Player([], [], c, 100, [], [], 0)
        self.assertEqual((7, 17), p1.hand_value())
    def test_get_decision(self):
        c = [playing_cards.Card('A', 'C'), playing_cards.Card('6', 'D')]
        d = person.Dealer([], [], c)
        d.construct_hit_on_soft_17_dealer()
        decision = d.get_decision()
        self.assertEqual('HIT', decision)


if __name__ == '__main__':
    unittest.main()