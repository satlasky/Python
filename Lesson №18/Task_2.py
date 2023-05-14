from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def calc_fabric(self):
        pass
class Coat(Cloth):
    fabric_reserve = 0.5

    def __init__(self, size):
        self.size = size

    @property
    def calc_fabric(self):
        return self.size / 6.5 + Coat.fabric_reserve


class Suit(Cloth):
    fabric_reserve = 0.3

    def __init__(self, height):
        self.height = height

    @property
    def calc_fabric(self):
        return self.height * 2 + Suit.fabric_reserve


coat1 = Coat(50)
suit1 = Suit(1.75)

coats_list = [Coat(44), Coat(48), Coat(52)]
suits_list = [Suit(1.70), Suit(1.75), Suit(1.80)]

print(coat1.calc_fabric)
print(suit1.calc_fabric)

total_fabric_for_coats = sum([coat.calc_fabric for coat in coats_list])
total_fabric_for_suits = sum([suit.calc_fabric for suit in suits_list])

print(total_fabric_for_coats)
print(total_fabric_for_suits)