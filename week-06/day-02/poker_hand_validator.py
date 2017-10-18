class Poker(object):

    def suit_of_card(self, input):
        suits = {"H": "heart", "D": "diamond", "C": "clover", "P": "pikes"}
        for i in suits:
            if input == i:
                return suits[i]

    def value_of_card(self, input):
        values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        for i in values:
            if input == i:
                return values[i]
        if input.isdigit() and int(input) >= 2 and int(input) <= 10:
            return int(input)
        return "Invalid Value Input"

    def color_of_card(self, input):
        if input == "C" or input == "P":
            return "black"
        elif input == "H" or input == "D":
            return "red"

    def create_card(self, input):
        return {"suit": self.suit_of_card(input[1]),
                 "value": self.value_of_card(input[0])}

    def user_hand(self, input):
        hand =[]
        cards = input.split(" ")
        for card in cards:
            hand.append(self.create_card(card))
        return hand

    def is_flush(self, hand):
        first_card = hand[1]["suit"] 
        for card in hand:
            if card["suit"] != first_card:
                return False
        return True

    def is_straight(self, hand): 
        hand = self.sort_hand(hand)
        for i in range(len(hand)-1):
            if hand[i]["value"]+1 != hand[i+1]["value"]:
                return False
        return True

    def is_straight_flush(self, hand):
        return self.is_flush(hand) and self.is_straight(hand)

    def is_royal_flush(self, hand):
        for card in hand:
            if not self.is_high_card(card):
                return False
        return self.is_straight_flush(hand)

    def sort_hand(self, hand):
        hand = sorted(hand, key=lambda card: card["value"])
        return hand

    def is_high_card(self, card):
        return card["value"] >= 10




poker = Poker()