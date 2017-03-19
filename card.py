#!/usr/bin/python3

from random import randint

from logger import Logger


class Card:

    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    CARDS = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
             'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
             'Queen', 'King']

    suit = 0
    value = 0

    def __init__(self, suit = None, value = None):
        self.suit = randint(0, 3) if (not suit) else suit
        self.value = randint(0, 12) if (not value) else value

    def __del__(self):
        pass

    @staticmethod
    def translate(g_card):
        return Card.to_string(g_card)

    @staticmethod
    def to_string(g_card):
        Logger.log("Card: Printing card: [" + str(g_card.suit) + "][" + str(g_card.value) + "]")
        suit = Card.SUITS[g_card.suit]
        value = Card.CARDS[g_card.value]
        return (value + " of " + suit)

    def show(self):
        print("Suit: " + str(self.suit) + ", Value: " + str(self.value))

if (__name__ == '__main__'):
    print("Running Card class as main.")
    for i in range(0,10):
        card = Card()
        card.show()
