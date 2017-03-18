#!/usr/bin/python3

from random import shuffle


class Deck:
    deck = []

    def __init__(self):
        self.regenerate_deck()

    def __del__(self):
        pass

    def shuffle_cards(self):
        shuffle(self.deck)

    def regenerate_deck(self):
        self.deck.clear()
        for i in range(0, 52):
            suit = i % 4
            card = i % 13
            self.deck.append(str(suit) + ':' + str(card))

    def display(self):
        dshow = ""
        for card in self.deck:
            dshow += card
            dshow += ", "
        return (dshow[:-2])


if (__name__ == '__main__'):
    print("Running Deck class as main.")
    deck = Deck()
    print(deck.display())
    deck.shuffle_cards()
    print(deck.display())
    deck.regenerate_deck()
    print(deck.display())
