import random
DECISION = ['HIT', 'STAND', 'DOUBLE', 'SURRENDER', 'SPLIT']
RANGE_TRUE_COUNT = range(-12, 13)
Q_INIT_POLICY = random.uniform(-1, 1)

class Person:
    def __init__(self, hand):
        self.hand = hand
    def hand_value(self):
        accum = 0 
        for card in self.hand:
            accum += card.gameValue()



class Dealer(Person):
    def __init__(self, hard_count_matrix, soft_count_matrix, hand):
        super.__init__(hand)
        self.hard_count_matrix = hard_count_matrix
        self.soft_count_matrix = soft_count_matrix

    def construct_hit_on_soft_17_dealer(self):
        self.hard_count_matrix =  [DECISION[0]] * 13 + [DECISION[1]] * 5
        self.soft_count_matrix = [DECISION[0]] * 6 + [DECISION[1]] * 4
    
    def get_decision(self):
        hv = self.hand_value()
        if self.soft_hand:
            self.soft_count_matrix[hv - 2]
        else:
            self.hard_count_matrix[hv - 4]
    def dealer_card(self):
        if len(self.hand) > 0:
            return self.hand[0]
        else:
            raise Exception("dealer hand must have a card to get showing card")

class Player(Person):
    def __init__(self, hand, money, position):
        super().__init__(hand)
        self.money = money
        self.position = position
        self.q_table = self.init_q_table()
    
    """q_table[0] == splittable [q_value][player_card_val - 1][ dealer_card_val - 1][true count]
    q_table[1] == first_two [q_value][]
    q_table[2] == soft [q_value][player_hand_val - 13][dealer_card_val - 1][true count]
    """
    def init_q_table(self):
        q_splittable = [[[[Q_INIT_POLICY for _ in DECISION] for _ in range(0, 10)] for _ in range(0, 10)] for _ in RANGE_TRUE_COUNT]
        q_soft_firt_two = [[[[Q_INIT_POLICY for _ in DECISION[:-1]] for _ in range(12, 22)] for _ in range(0, 10)] for _ in RANGE_TRUE_COUNT]
        q_first_two = [[[[Q_INIT_POLICY for _ in DECISION[:-1]] for _ in range(5, 22)] for _ in range(0, 10)] for _ in RANGE_TRUE_COUNT]
        q_soft = [[[[Q_INIT_POLICY for _ in DECISION[:2]] for _ in range(13, 22)] for _ in range(0, 10)] for _ in RANGE_TRUE_COUNT]
        q_hard = [[[[Q_INIT_POLICY for _ in DECISION[:2]] for _ in range(6, 22)] for _ in range(0, 10)] for _ in RANGE_TRUE_COUNT]
        return [q_splittable, q_soft_firt_two, q_first_two, q_soft, q_hard]
    

    def pay(self, amount: int):
        self.money = self.money + amount

    def soft_hand(self):
        for card in self.hand:
            if card.gameValue() == 1:
                if self.hand_value <= 10:
                    return True
        return False
    
    def splittable(self):
        if len(self.hand) == 2 and self.hand[0].gameValue() == self.hand[1].gameValue():
            return True
        else:
            return False