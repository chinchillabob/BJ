import person
import playing_cards
class Table:
    def __init__(self, deck: playing_cards.Deck, players: list[person.Player], dealer: person.Dealer):
        self.deck = deck
        self.players = players
        self.dealer = dealer
    
    def reset_hands(self):
        for player in self.players:
            player.hand = []
        self.dealer.hand = []
    
    def deal(self):
        for _ in range (0, 2):
            for p in self.players:
                p.hand.append(self.deck.pull())
        self.dealer.hand.append(self.deck.pull_hole_card())
        self.dealer.hand.append(self.deck.pull())

    