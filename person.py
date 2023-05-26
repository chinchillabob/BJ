DECISION = ['HIT', 'STAND', 'SPLIT', 'DOUBLE', 'SURRENDER']
class Person:
    def __init__(self, hard_count_matrix, soft_count_matrix, hand):
        self.hard_count_matrix = hard_count_matrix,
        self.soft_count_matrix = soft_count_matrix,
        self.hand = hand
    
    def hand_value(self):
        accum = 0
        contains_ace = False
        for c in self.hand:
            accum += c.gameValue()
            if c.gameValue() == 1:
                contains_ace = True
        if contains_ace == True:
            return (accum, accum + 10)
        else:
            return (accum, 0)

class Dealer(Person):
    def __init__(self, hard_count_matrix, soft_count_matrix, hand):
        super().__init__(hard_count_matrix, soft_count_matrix, hand)

    def construct_hit_on_soft_17_dealer(self):
        self.hard_count_matrix =  [DECISION[0]] * 12 + [DECISION[1]] * 5
        self.soft_count_matrix = [DECISION[0]] * 6 + [DECISION[1]] * 4
    
    def get_decision(self):
        hv = self.hand_value()
        if hv[1] == 0 or hv[1] > 21:
            return self.hard_count_matrix[(hv[0] - 3)]
        else:
            return self.soft_count_matrix[hv[1] - 12]
    
    def get_dealer_showing_card(self):
        if len(self.hand) > 0:
            return self.hand(0)
        else:
            raise Exception("dealer hand must have a card to get showing card")

class Player(Person):
    def __init__(self, hard_count_matrix, soft_count_matrix, hand, money, split_matrix, deviations, position):
        super().__init__(hard_count_matrix, soft_count_matrix, hand)
        self.money = money
        self.split_matrix = split_matrix
        self.deviations = deviations
        self.position = position

    def pay(self, amount: int):
        self.money = self.money + amount

    def deviation_16vT(self, dealer_card, count):
        hv = self.hand_value()
        if not hv[1] == 0 and hv[0] == 16 and dealer_card.gameValue() == 10 and count >= 0:
            return DECISION[1]
        return None
    
    def deviation_15vT(self, dealer_card, count):
        hv = self.hand_value()
        if not hv[1] == 0 and hv[0] == 16 and dealer_card.gameValue() == 10 and count >= 4:
            return DECISION[1]
        return None
    
    def deviationTTv6(self, dealer_card, count):
        if len(self.hand) == 2 and self.hand[0].gameValue() == 10 and self.hand[1].gameValue() == 10 and dealer_card.gameValue() == 16 and count >= 0:
            return DECISION[2]
        return None 
    
    def deviationTTv5(self, dealer_card, count): 
        if len(self.hand) == 2 and self.hand[0].gameValue() == 10 and self.hand[1].gameValue() == 10 and dealer_card.gameValue() == 16 and count >= 4:
            return DECISION[2]
        return None 

    def deviation10v5(self, dealer_card, count):
        hv = self.hand_value()
        if hv[0] == 10 and hv[1] == 0 and dealer_card.gameValue() == 10 and count >= 4:
            return DECISION[3]
        return None 

    #deviations need to consider that hand_value() returns a tuple.
    #consider priority when it comes to split hands and associated hard count deviation
    def deviation12v3(self, dealer_card, count):
        if self.hand_value() == 12 and dealer_card.gameValue() == 3 and count >= 2:
            return DECISION[1]
        return None
    
    def deviation12v2(self, dealer_card, count):
        if self.hand_value() == 12 and dealer_card.gameValue() == 2 and count >= 3:
            return DECISION[1]
        return None
    
    def deviation12v2(self, dealer_card, count):
        if self.hand_value() == 12 and dealer_card.gameValue() == 2 and count >= 3:
            return DECISION[1]
        return None
    
    def deviation11vA(self, dealer_card, count):
        if self.hand_value() == 11 and dealer_card.gameValue() == 1 and count >= 1:
            return DECISION[3]
        return None

    def construct_illustrious_18(self):
        self.deviations = [self.deviation_16vT, self.deviation_15vT, ]

    def construct_hit_on_soft_17_dealer(self):
        self.hard_count_matrix = [([DECISION[0]] * 5) + ([DECISION[3]] * 2) + [DECISION[0]] + ([DECISION[1]] * 9),
                                  ([DECISION[0]] * 4) + ([DECISION[3]] * 3) + [DECISION[0]] + ([DECISION[1]] * 9),
                                  ([DECISION[0]] * 4) + ([DECISION[3]] * 3) + ([DECISION[1]] * 10),
                                  ([DECISION[0]] * 4) + ([DECISION[3]] * 3) + ([DECISION[1]] * 10),
                                  ([DECISION[0]] * 4) + ([DECISION[3]] * 3) + ([DECISION[1]] * 10),
                                  ([DECISION[0]] * 5) + ([DECISION[3]] * 2) + ([DECISION[0]] * 5) + ([DECISION[1]] * 5),
                                  ([DECISION[0]] * 5) + ([DECISION[3]] * 2) + ([DECISION[0]] * 5) + ([DECISION[1]] * 5),
                                  ([DECISION[0]] * 5) + ([DECISION[3]] * 2) + ([DECISION[0]] * 5) + ([DECISION[1]] * 5),
                                  ([DECISION[0]] * 6) + [DECISION[3]] + ([DECISION[0]] * 5) + ([DECISION[1]] * 5),
                                  ([DECISION[0]] * 6) + [DECISION[3]] + ([DECISION[0]] * 5) + ([DECISION[1]] * 5)
                                  ]
        self.soft_count_matrix = [([DECISION[0]] * 5) + [DECISION[3]] + ([DECISION[1]]*2)
                                  ([DECISION[0]] * 4) + ([DECISION[3]] * 2) + ([DECISION[1]]*2),
                                  ([DECISION[0]] * 2) + ([DECISION[3]] * 4) + ([DECISION[1]]*2),
                                  ([DECISION[3]] * 6) + ([DECISION[1]]*2),
                                  ([DECISION[3]] * 7) + [DECISION[1]],
                                  ([DECISION[0]] * 5) + ([DECISION[1]] * 3),
                                  ([DECISION[0]] * 5) + ([DECISION[1]] * 3),
                                  ([DECISION[0]] * 6) + ([DECISION[1]] * 2),
                                  ([DECISION[0]] * 6) + ([DECISION[1]] * 2),
                                  ([DECISION[0]] * 6) + ([DECISION[1]] * 2),
                                  ]
        self.split_matrix = [([DECISION[2]] * 2) + [DECISION[0]] + [DECISION[3]] + ([DECISION[2]] * 4) + [DECISION[1]] + [DECISION[2]],
                             ([DECISION[2]] * 2) + [DECISION[0]] + [DECISION[3]] + ([DECISION[2]] * 4) + [DECISION[1]] + [DECISION[2]],
                             ([DECISION[2]] * 2) + [DECISION[0]] + [DECISION[3]] + ([DECISION[2]] * 4) + [DECISION[1]] + [DECISION[2]],
                             ([DECISION[2]] * 3) + [DECISION[3]] + ([DECISION[2] * 4]) + [DECISION[1]] + [DECISION[2]],
                             ([DECISION[2]] * 3) + [DECISION[3]] + ([DECISION[2] * 4]) + [DECISION[1]] + [DECISION[2]],
                             ([DECISION[2]] * 2) + [DECISION[0]] + [DECISION[3]] + [DECISION[0]] + ([DECISION[2]] * 2) + ([DECISION[1]] * 2) + [DECISION[2]],
                             ([DECISION[0]] * 3) + [DECISION[3]] + ([DECISION[0]] * 2) + ([DECISION[2]] * 2) + ([DECISION[1]] * 2) + [DECISION[2]],
                             ([DECISION[0]] * 3) + [DECISION[3]] + ([DECISION[0]] * 2) + ([DECISION[2]] * 2) + ([DECISION[1]] * 2) + [DECISION[2]],
                             ([DECISION[0]] * 6) + [DECISION[2]] + ([DECISION[1]] * 2) + [DECISION[2]],
                             ([DECISION[0]] * 6) + [DECISION[2]] + ([DECISION[1]] * 2) + [DECISION[2]],
                             ]