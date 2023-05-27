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
        if self.value == 'A':
            return 1
        elif self.value in ['2', '3', '4', '5', '6', '7', '8', '9']:
            return ord(self.value) - 48
        else:
            return 10

class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.len = len(cards)
        self.frequencyDistrib = [0] * 10
        self.runningCount = 0
    def set_frequencyDistrib(self):
        for card in self.cards:
            self.frequencyDistrib[card.gameValue  - 1] += 1
    def pull_card_with_val(self, val):
        idx = 0
        while idx < self.len:
            if self.cards[idx].value == val:
                self.cards.pop(idx)
                self.frequencyDistrib[val - 1] -= 1
                self.len -= 1
                if val == 1 or val == 10:
                    self.runningCount -= 1
                elif val <= 6:
                    self.runningCount += 1
                break
            idx += 1
        raise Exception(f"no more cards to pull of value {val}")
    def shuffle(self):
        random.shuffle(self.cards)
    def pull(self):
        if self.len == 0:
            raise ValueError("cannot pull from empty deck")
        self.len -= 1
        card_v = self.cards[0].gameValue
        self.frequencyDistrib[card_v - 1] -= 1
        if card_v == 1 or card_v == 10:
            self.runningCount -= 1 
        elif card_v <= 6:
            self.runningCount += 1
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