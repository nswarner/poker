#!/usr/bin/python3

from random import randint


class Card:

    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    CARDS = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
             'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
             'Queen', 'King']

    suit = 0
    value = 0

    def __init__(self):
        self.suit = randint(0, 4)
        self.value = randint(0, 12)

    def __del__(self):
        pass

    @staticmethod
    def translate(g_card):
        suit = Card.SUITS[int(g_card.split(':')[0])]
        card = Card.CARDS[int(g_card.split(':')[1])]
        return (g_card + " of " + suit)

    def show(self):
        print("Suit: " + str(self.suit) + ", Value: " + str(self.value))

if (__name__ == '__main__'):
    print("Running Card class as main.")
    for i in range(0,10):
        card = Card()
        card.show()
