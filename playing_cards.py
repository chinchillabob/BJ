import random

VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
SUITS = ['S', 'C', 'H', 'D']
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    #this is being used in player.splitable
    #returns card in game value
    #for an ace 1 is returned
    def gameValue(self):
        if self.value in ['2', '3', '4', '5', '6', '7', '8', '9']:
            return ord(self.value) - 48
        elif self.value == 'A':
            return 1
        else:
            return 10

class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.len = len(cards)
        self.frequencyDistrib = [0] * 10
    def set_frequencyDistrib(self):
        for card in self.cards:
            self.frequencyDistrib[card.val - 1] += 1
    def pull_card_with_val(self, val):
        idx = 0
        while idx < self.len:
            if self.cards[idx].value == val:
                self.cards.pop(idx)
                self.frequencyDistrib[self.cards[idx].value - 1] += -1
                self.len += -1
                break
            idx += 1
    def shuffle(self):
        random.shuffle(self.cards)
    def pull(self):
        self.len += -1
        self.frequencyDistrib[self.cards[0].val - 1] += -1
        return self.cards.pop(0)
    def add_decks(self, num_decks: int):
        self._addDecks_helper(num_decks)
        self.set_frequencyDistrib()
    def _addDecks_helper(self, num_decks: int):
        cards = []
        for v in VALUES:
            for s in SUITS:
                cards.append(Card(v, s))
        self.cards = self.cards + cards * num_decks