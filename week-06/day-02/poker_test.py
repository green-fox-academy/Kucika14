import unittest
from poker_hand_validator import *

class PokerTest(unittest.TestCase):

    def test_suit_of_card(self):
         self.assertEqual(poker.suit_of_card("H"),"heart")
    
    def test_suit_of_card_second(self):
        self.assertEqual(poker.suit_of_card("D"),"diamond")

    def test_card_value_is_2_when_char_2(self):
        self.assertEqual(poker.value_of_card("2"), 2)

    def test_card_value_is_valid(self):
        self.assertEqual(poker.value_of_card("3"), 3)

    def test_card_value_is_invaid(self):
        self.assertEqual(poker.value_of_card("11"), "Invalid Value Input")

    def test_card_suits_value(self):
        self.assertEqual(poker.value_of_card("J"), 11 )

    def test_card_color_red_when_heart(self):
        self.assertEqual(poker.color_of_card("H"), "red")

    def test_correct_card_created_from_h2_string(self):
        card = poker.create_card("2H")
        self.assertEqual(card["value"], 2)
        self.assertEqual(card["suit"], "heart")
        
    def test_two_card(self):
        hand = poker.user_hand("2H 3D")
        self.assertEqual(hand[0]["value"], 2)
        self.assertEqual(hand[1]["value"], 3)

    def test_flush(self):
        hand = poker.user_hand("2H 3H 5H 9H KH")
        self.assertEqual(poker.is_flush(hand), True)
    
    def test_is_high_card(self):
        card = poker.create_card("KH")
        self.assertEqual(poker.is_high_card(card), True)

    def test_is_straight(self):
        hand = poker.user_hand("4H 3H 2H 5H 6C")
        self.assertEqual(poker.is_straight(hand), True)

    def test_is_straight_flush(self):
        hand = poker.user_hand("4H 3H 2H 5H 6H")
        self.assertEqual(poker.is_straight_flush(hand), True)
        
    def test_is_royal_flush(self):
        hand = poker.user_hand("TH JH QH KH AH")
        self.assertEqual(poker.is_royal_flush(hand), True)


if __name__ == '__main__':
    unittest.main()