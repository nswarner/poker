#!/usr/bin/python3

from card import Card
from logger import Logger


class Hand:
    hand = None

    def __init__(self, num_cards = 2):
        Logger.log("Hand: Creating a new hand with cards: " + str(num_cards))
        self.hand = []
        for i in range(0, num_cards):
            Logger.log("Hand: Calling add_card(Card()).")
            self.add_card(Card())

    def __del__(self):
        pass

    def hand_to_string(self):
        Logger.log("Hand: Converting hand to string.")
        results = "[ "
        for i in range(0, 2):
            results += Card.translate(self.hand[i]) + " ], ["
        return results[:-3]

    def add_card(self, g_card):
        Logger.log("Hand: add_card(Card) called.")
        if (len(self.hand) < 2):
            self.hand.append(g_card)
        else:
            raise Exception('Hand already has two cards.')

    def end_hand(self, g_card):
        self.hand.clear()


if (__name__ == '__main__'):
    one_hand = Hand()
    one_hand.add_card("1:9")
    one_hand.add_card("1:12")
    one_hand.display_hand()
