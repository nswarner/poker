#!/usr/bin/python3

from card import Card


class Hand:
    hand = []

    def __init__(self):
        pass

    def __del__(self):
        pass

    def display_hand(self):
        for i in range(0, 2):
            print(Card.translate(self.hand[i]))

    def add_card(self, card):
        if (len(self.hand) < 2):
            self.hand.append(card)
        else:
            raise Exception('Hand already has two cards.')

    def end_hand(self, card):
        self.hand.clear()


if (__name__ == '__main__'):
    one_hand = Hand()
    one_hand.add_card("1:9")
    one_hand.add_card("1:12")
    one_hand.display_hand()
