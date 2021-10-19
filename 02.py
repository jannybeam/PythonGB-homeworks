from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5

    def sum_consumption(self, all_coats):
        a = 0
        for coat in all_coats:
            a += coat.consumption
        return a

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return 2 * self.h + 0.3

    def sum_consumption(self, all_suits):
        b = 0
        for suit in all_suits:
            b += suit.consumption
        return b

coat = Coat(42)
suit = Suit(1.58)
suit_2 = Suit(1.71)
suit_3 = Suit(1.80)
list_suits = [suit, suit_2, suit_3]
print(coat.consumption)
print(suit.consumption)
print(suit.sum_consumption(list_suits))