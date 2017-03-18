#!/usr/bin/python3

from random import randint
from random import shuffle

from .card import Card
from .logger import Logger


class Deck:
    deck = []

    def __init__(self):
        Logger.log("Deck: Initializing the deck.")
        self.regenerate_deck()

    def __del__(self):
        pass

    def clear_deck(self):
        Logger.log("Deck: Clearing the deck.")
        self.deck.clear()

    def shuffle_cards(self):
        Logger.log("Deck: Shuffling the deck.")
        shuffle(self.deck)

    def get_card(self):
        Logger.log("Deck: Pulling card from the deck.")
        length = len(self.deck)
        rand_card = randint(0, length)
        return (self.deck.pop(rand_card))

    def regenerate_deck(self):
        Logger.log("Deck: Recreating the deck.")
        self.clear_deck()
        for i in range(0, 52):
            suit = i % 4
            card = i % 13
            card = Card(suit, card)
            self.deck.append(card)

    def display(self):
        show = ""
        for g_card in self.deck:
            show += Card.translate(g_card) + ", "
        return (show[:-2])


if (__name__ == '__main__'):
    print("Running Deck class as main.")
    deck = Deck()
    print(deck.display())
    deck.shuffle_cards()
    print(deck.display())
    deck.regenerate_deck()
    print(deck.display())
